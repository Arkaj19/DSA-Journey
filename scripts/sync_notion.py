#!/usr/bin/env python3
"""
DSA Notion -> GitHub daily sync.

Pulls a small, randomized batch (1-3) of the OLDEST not-yet-uploaded
questions from a Notion database, writes them as nicely formatted
markdown files into solutions/<Difficulty>/, regenerates the README
stats, commits + pushes, and finally marks those questions as
"Uploaded to GitHub" back in Notion (so it's never repeated).

Designed to run once a day from a GitHub Actions cron job.

Required environment variables:
    NOTION_TOKEN            - Notion internal integration token
    NOTION_DATA_SOURCE_ID   - Data source ID of the "DSA Questions Log"
                               (collection://<this-id> in Notion)

Optional:
    MIN_PER_DAY (default 1)
    MAX_PER_DAY (default 3)
"""

import json
import os
import random
import re
import subprocess
import sys
from datetime import datetime, timezone

import requests
from markdownify import markdownify as html_to_markdown

NOTION_TOKEN = os.environ["NOTION_TOKEN"]
DATA_SOURCE_ID = os.environ["NOTION_DATA_SOURCE_ID"]
MIN_PER_DAY = int(os.environ.get("MIN_PER_DAY", "1"))
MAX_PER_DAY = int(os.environ.get("MAX_PER_DAY", "3"))

NOTION_VERSION = "2025-09-03"
API_BASE = "https://api.notion.com/v1"
HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": NOTION_VERSION,
    "Content-Type": "application/json",
}

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOLUTIONS_DIR = os.path.join(REPO_ROOT, "solutions")
MANIFEST_PATH = os.path.join(REPO_ROOT, "manifest.json")
README_PATH = os.path.join(REPO_ROOT, "README.md")

STATS_START = "<!-- STATS:START -->"
STATS_END = "<!-- STATS:END -->"
RECENT_START = "<!-- RECENT:START -->"
RECENT_END = "<!-- RECENT:END -->"


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "untitled"


def load_manifest():
    if os.path.exists(MANIFEST_PATH):
        with open(MANIFEST_PATH, "r") as f:
            return json.load(f)
    return {"entries": []}


def save_manifest(manifest):
    with open(MANIFEST_PATH, "w") as f:
        json.dump(manifest, f, indent=2)


def query_unposted_questions(page_size=25):
    """Fetch oldest-first, not-yet-uploaded questions from Notion."""
    url = f"{API_BASE}/data_sources/{DATA_SOURCE_ID}/query"
    body = {
        "filter": {
            "property": "Uploaded to GitHub",
            "checkbox": {"equals": False},
        },
        "sorts": [{"property": "Solved On", "direction": "ascending"}],
        "page_size": page_size,
    }
    resp = requests.post(url, headers=HEADERS, json=body)
    resp.raise_for_status()
    return resp.json().get("results", [])


def get_page_blocks(page_id):
    blocks = []
    url = f"{API_BASE}/blocks/{page_id}/children"
    params = {"page_size": 100}
    while True:
        resp = requests.get(url, headers=HEADERS, params=params)
        resp.raise_for_status()
        data = resp.json()
        blocks.extend(data.get("results", []))
        if not data.get("has_more"):
            break
        params["start_cursor"] = data.get("next_cursor")
    return blocks


def rich_text_to_plain(rich_text_list):
    return "".join(rt.get("plain_text", "") for rt in rich_text_list)


def blocks_to_markdown(blocks):
    """Very small, purpose-built block -> markdown converter.
    Handles the block types typically found in these Notion pages:
    paragraphs, headings, bulleted/numbered lists, and code blocks."""
    lines = []
    for block in blocks:
        btype = block.get("type")
        data = block.get(btype, {})

        if btype == "code":
            code_text = rich_text_to_plain(data.get("rich_text", []))
            lang = data.get("language", "") or ""
            lines.append(f"```{lang}\n{code_text}\n```")
        elif btype == "paragraph":
            text = rich_text_to_plain(data.get("rich_text", []))
            if text.strip():
                lines.append(text)
        elif btype in ("heading_1", "heading_2", "heading_3"):
            level = {"heading_1": "##", "heading_2": "###", "heading_3": "####"}[btype]
            text = rich_text_to_plain(data.get("rich_text", []))
            lines.append(f"{level} {text}")
        elif btype == "bulleted_list_item":
            text = rich_text_to_plain(data.get("rich_text", []))
            lines.append(f"- {text}")
        elif btype == "numbered_list_item":
            text = rich_text_to_plain(data.get("rich_text", []))
            lines.append(f"1. {text}")
        elif btype == "quote":
            text = rich_text_to_plain(data.get("rich_text", []))
            lines.append(f"> {text}")
        elif btype == "divider":
            lines.append("---")
        # skip empty/unsupported block types silently
    return "\n\n".join(lines).strip()


def fetch_leetcode_statement(link: str) -> str | None:
    """Fetch the official problem statement via LeetCode's public GraphQL API.
    Returns markdown, or None if it can't be fetched (premium-only question,
    network hiccup, bad URL, etc.) — callers must handle that gracefully."""
    match = re.search(r"leetcode\.com/problems/([^/]+)/?", link)
    if not match:
        return None
    slug = match.group(1)
    try:
        resp = requests.post(
            "https://leetcode.com/graphql",
            json={
                "query": "query q($titleSlug: String!) { question(titleSlug: $titleSlug) { content isPaidOnly } }",
                "variables": {"titleSlug": slug},
            },
            headers={
                "Content-Type": "application/json",
                "Referer": f"https://leetcode.com/problems/{slug}/",
            },
            timeout=15,
        )
        resp.raise_for_status()
        question = resp.json().get("data", {}).get("question")
        if not question or question.get("isPaidOnly") or not question.get("content"):
            return None
        return html_to_markdown(question["content"], heading_style="ATX").strip()
    except (requests.RequestException, ValueError, KeyError):
        return None


def fetch_gfg_statement(link: str) -> str | None:
    """Best-effort scrape of a GeeksforGeeks problem page. GFG's markup shifts
    over time and has anti-bot friction, so this is allowed to fail silently."""
    try:
        resp = requests.get(link, timeout=15, headers={"User-Agent": "Mozilla/5.0"})
        resp.raise_for_status()
        match = re.search(
            r'class="problems_problem_content[^"]*"[^>]*>(.*?)</div>\s*</div>',
            resp.text,
            re.DOTALL,
        )
        if not match:
            return None
        return html_to_markdown(match.group(1), heading_style="ATX").strip()
    except (requests.RequestException, ValueError):
        return None


def fetch_problem_statement(link: str, platform: str) -> str | None:
    if not link:
        return None
    if "leetcode.com" in link:
        return fetch_leetcode_statement(link)
    if "geeksforgeeks.org" in link:
        return fetch_gfg_statement(link)
    return None


def extract_property_values(props):
    def get_title(p):
        arr = p.get("title", [])
        return rich_text_to_plain(arr) if arr else "Untitled"

    def get_select(p):
        sel = p.get("select")
        return sel.get("name") if sel else None

    def get_multi_select(p):
        return [o.get("name") for o in p.get("multi_select", [])]

    def get_url(p):
        return p.get("url") or ""

    def get_created_time(p):
        return p.get("created_time")

    question = get_title(props.get("Question", {}))
    difficulty = get_select(props.get("Difficulty", {})) or "Unsorted"
    platform = get_select(props.get("Platform", {})) or "Other"
    topics = get_multi_select(props.get("Topics", {}))
    confidence = get_multi_select(props.get("Confidence Score", {}))
    link = get_url(props.get("Link", {}))
    solved_on = get_created_time(props.get("Solved On", {}))

    return {
        "question": question,
        "difficulty": difficulty,
        "platform": platform,
        "topics": topics,
        "confidence": confidence,
        "link": link,
        "solved_on": solved_on,
    }


def format_file_content(meta, body_markdown, counter, statement_markdown=None):
    solved_date = meta["solved_on"][:10] if meta["solved_on"] else "unknown"
    topics_str = ", ".join(meta["topics"]) if meta["topics"] else "—"
    confidence_str = ", ".join(meta["confidence"]) if meta["confidence"] else "—"
    link_line = f"[Problem link]({meta['link']})" if meta["link"] else "_No link recorded_"

    header = (
        f"# {counter:03d}. {meta['question']}\n\n"
        f"| | |\n"
        f"|---|---|\n"
        f"| **Platform** | {meta['platform']} |\n"
        f"| **Difficulty** | {meta['difficulty']} |\n"
        f"| **Topics** | {topics_str} |\n"
        f"| **Solved on** | {solved_date} |\n"
        f"| **How I got there** | {confidence_str} |\n"
        f"| **Link** | {link_line} |\n\n"
        f"---\n\n"
    )

    sections = []
    if statement_markdown:
        sections.append("## Problem\n\n" + statement_markdown)
    elif meta["link"]:
        sections.append(
            "## Problem\n\n_Couldn't auto-fetch the statement (paid-only question, "
            f"or the source page changed). See the [original link]({meta['link']})._"
        )
    else:
        sections.append(
            "## Problem\n\n_No link was recorded for this one, so the statement "
            "couldn't be fetched automatically._"
        )

    if body_markdown.strip():
        sections.append("## My Notes & Solution\n\n" + body_markdown)
    else:
        sections.append("## My Notes & Solution\n\n_No notes or code captured for this one yet._")

    return header + "\n\n".join(sections) + "\n"


def write_solution_file(meta, body_markdown, counter, statement_markdown=None):
    diff_folder = meta["difficulty"] if meta["difficulty"] in ("Easy", "Medium", "Hard") else "Unsorted"
    folder = os.path.join(SOLUTIONS_DIR, diff_folder)
    os.makedirs(folder, exist_ok=True)
    slug = slugify(meta["question"])
    filename = f"{counter:03d}-{slug}.md"
    path = os.path.join(folder, filename)
    # avoid collisions
    n = 1
    while os.path.exists(path):
        n += 1
        filename = f"{counter:03d}-{slug}-{n}.md"
        path = os.path.join(folder, filename)
    content = format_file_content(meta, body_markdown, counter, statement_markdown)
    with open(path, "w") as f:
        f.write(content)
    rel_path = os.path.relpath(path, REPO_ROOT)
    return rel_path


DIFFICULTY_EMOJI = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴", "Unsorted": "⚪"}


def regenerate_readme(manifest):
    entries = manifest["entries"]
    total = len(entries)

    by_difficulty = {}
    by_topic = {}
    by_platform = {}
    for e in entries:
        by_difficulty[e["difficulty"]] = by_difficulty.get(e["difficulty"], 0) + 1
        by_platform[e["platform"]] = by_platform.get(e["platform"], 0) + 1
        for t in e["topics"]:
            by_topic[t] = by_topic.get(t, 0) + 1

    # Badges
    badges = (
        f"![Total Solved](https://img.shields.io/badge/Total%20Solved-{total}-blue?style=flat-square)\n"
        f"![Easy](https://img.shields.io/badge/Easy-{by_difficulty.get('Easy', 0)}-brightgreen?style=flat-square) "
        f"![Medium](https://img.shields.io/badge/Medium-{by_difficulty.get('Medium', 0)}-yellow?style=flat-square) "
        f"![Hard](https://img.shields.io/badge/Hard-{by_difficulty.get('Hard', 0)}-red?style=flat-square)\n"
    )

    diff_table = "| Difficulty | Count |\n|---|---|\n"
    for d in ("Easy", "Medium", "Hard", "Unsorted"):
        if by_difficulty.get(d):
            diff_table += f"| {DIFFICULTY_EMOJI.get(d, '')} {d} | {by_difficulty[d]} |\n"

    top_topics = sorted(by_topic.items(), key=lambda x: -x[1])[:12]
    topic_table = "| Topic | Count |\n|---|---|\n"
    for t, c in top_topics:
        topic_table += f"| {t} | {c} |\n"

    stats_block = (
        f"{badges}\n"
        f"### Breakdown by difficulty\n\n{diff_table}\n"
        f"### Top topics\n\n{topic_table}\n"
        f"_Last synced: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}_\n"
    )

    recent = sorted(entries, key=lambda e: e["uploaded_at"], reverse=True)[:15]
    recent_lines = []
    for e in recent:
        recent_lines.append(
            f"- [{e['question']}]({e['path']}) — {DIFFICULTY_EMOJI.get(e['difficulty'], '')} "
            f"{e['difficulty']} · {e['platform']} · _added {e['uploaded_at'][:10]}_"
        )
    recent_block = "\n".join(recent_lines) if recent_lines else "_Nothing synced yet._"

    if not os.path.exists(README_PATH):
        scaffold = README_TEMPLATE
        with open(README_PATH, "w") as f:
            f.write(scaffold)

    with open(README_PATH, "r") as f:
        readme = f.read()

    readme = re.sub(
        f"{re.escape(STATS_START)}.*?{re.escape(STATS_END)}",
        f"{STATS_START}\n{stats_block}\n{STATS_END}",
        readme,
        flags=re.DOTALL,
    )
    readme = re.sub(
        f"{re.escape(RECENT_START)}.*?{re.escape(RECENT_END)}",
        f"{RECENT_START}\n{recent_block}\n{RECENT_END}",
        readme,
        flags=re.DOTALL,
    )

    with open(README_PATH, "w") as f:
        f.write(readme)


README_TEMPLATE = f"""# 🧠 DSA Revision Vault

A living archive of every problem I've solved, synced automatically from my
personal Notion tracker. New problems trickle in daily — this repo is meant
to be a place I actually want to come back and revisit, not a dump.

Each file has the problem context, my notes, and the exact solution I wrote.

{STATS_START}
{STATS_END}

## 🆕 Recently added

{RECENT_START}
{RECENT_END}

## 📂 Structure

```
solutions/
  Easy/
  Medium/
  Hard/
```

Every file is numbered in the order I originally solved it, so browsing a
folder top-to-bottom retraces my actual learning path.

---
_This repo is synced automatically once a day via GitHub Actions from a
Notion database — see `scripts/sync_notion.py`._
"""


def mark_uploaded(page_id):
    url = f"{API_BASE}/pages/{page_id}"
    body = {"properties": {"Uploaded to GitHub": {"checkbox": True}}}
    resp = requests.patch(url, headers=HEADERS, json=body)
    resp.raise_for_status()


def run(cmd):
    print(f"$ {' '.join(cmd)}")
    subprocess.run(cmd, check=True, cwd=REPO_ROOT)


def main():
    candidates = query_unposted_questions()
    if not candidates:
        print("Nothing to sync today — Notion queue is empty.")
        return

    batch_size = min(random.randint(MIN_PER_DAY, MAX_PER_DAY), len(candidates))
    batch = candidates[:batch_size]

    manifest = load_manifest()
    counter = len(manifest["entries"])

    written = []
    for page in batch:
        counter += 1
        page_id = page["id"]
        meta = extract_property_values(page["properties"])
        blocks = get_page_blocks(page_id)
        body_md = blocks_to_markdown(blocks)
        statement_md = fetch_problem_statement(meta["link"], meta["platform"])
        rel_path = write_solution_file(meta, body_md, counter, statement_md)

        entry = {
            "page_id": page_id,
            "question": meta["question"],
            "difficulty": meta["difficulty"],
            "platform": meta["platform"],
            "topics": meta["topics"],
            "solved_on": meta["solved_on"],
            "path": rel_path,
            "uploaded_at": datetime.now(timezone.utc).isoformat(),
        }
        manifest["entries"].append(entry)
        written.append((page_id, meta["question"]))

    save_manifest(manifest)
    regenerate_readme(manifest)

    # Commit + push
    run(["git", "add", "-A"])
    diff_check = subprocess.run(
        ["git", "diff", "--cached", "--quiet"], cwd=REPO_ROOT
    )
    if diff_check.returncode == 0:
        print("No file changes detected, skipping commit.")
        return

    titles = ", ".join(q for _, q in written)
    commit_msg = f"Add {len(written)} solution(s): {titles}"
    run(["git", "-c", "user.name=github-actions[bot]",
         "-c", "user.email=github-actions[bot]@users.noreply.github.com",
         "commit", "-m", commit_msg])
    run(["git", "push"])

    # Only mark as uploaded in Notion AFTER a successful push
    for page_id, _ in written:
        mark_uploaded(page_id)

    print(f"Synced {len(written)} question(s): {titles}")


if __name__ == "__main__":
    try:
        main()
    except requests.HTTPError as e:
        print(f"Notion API error: {e.response.status_code} {e.response.text}", file=sys.stderr)
        sys.exit(1)

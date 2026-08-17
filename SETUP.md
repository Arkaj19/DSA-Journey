# Setup

One-time setup, then it runs itself.

## 1. Create a Notion integration

1. Go to https://www.notion.so/my-integrations → **New integration**.
2. Name it whatever (e.g. "DSA GitHub Sync"), pick your workspace, Internal integration.
3. Copy the **Internal Integration Token** (starts with `ntn_` or `secret_`) — you'll need it in step 3.
4. Open your **DSA Planner** database in Notion → **DSA Questions Log** data source → `•••` menu (top right) → **Connections** → add your new integration. Without this the integration can't see the database.

## 2. Get the Data Source ID

Your "DSA Questions Log" data source ID is:

```
a196d510-9535-4a3c-b8b9-588bfa7ab310
```

(This is fixed — no need to look it up again unless you recreate the database.)

## 3. Add repo secrets

In your GitHub repo: **Settings → Secrets and variables → Actions → New repository secret**

| Name | Value |
|---|---|
| `NOTION_TOKEN` | the integration token from step 1 |
| `NOTION_DATA_SOURCE_ID` | `a196d510-9535-4a3c-b8b9-588bfa7ab310` |

## 4. Allow Actions to push commits

**Settings → Actions → General → Workflow permissions** → select **"Read and write permissions"** → Save.

(Without this, the workflow can check things out but can't push the daily commit.)

## 5. Push these files to your repo

Copy this whole folder's contents into the root of your GitHub repo and push:

```
your-repo/
├── .github/workflows/daily-sync.yml
├── scripts/sync_notion.py
├── requirements.txt
├── manifest.json
├── README.md
└── SETUP.md   (delete this once you're done, or keep it for reference)
```

## 6. Test it

Go to the **Actions** tab in your repo → **Daily DSA Sync from Notion** → **Run workflow**
(this uses the `workflow_dispatch` trigger, so you don't have to wait for the cron).

Check that:
- 1-3 new files appeared under `solutions/<Difficulty>/`
- `README.md` stats updated
- The corresponding question(s) in Notion now have **Uploaded to GitHub** checked

If all that looks right, you're done — it'll run daily on its own from here,
working through your 113-question backlog first (oldest solved first) and
then keeping pace with whatever you log going forward.

## Notes

- The cron in `daily-sync.yml` runs at 14:30 UTC. GitHub's scheduler can be a
  few minutes late during high load — that's normal and won't break the streak.
- If a day's run finds an empty queue (you're all caught up), it just does
  nothing and exits cleanly — no empty commits.
- Batch size is random between 1 and 3 per day (configurable via `MIN_PER_DAY`
  / `MAX_PER_DAY` env vars in the workflow file).

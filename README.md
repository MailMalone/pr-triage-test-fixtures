# QueueLite

A tiny in-memory task queue used to test pull-request triage.

## Run

```powershell
python -c "from queuelite import add_task, list_tasks; add_task('write tests'); print(list_tasks())"
```

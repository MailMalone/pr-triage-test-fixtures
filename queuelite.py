"""A tiny in-memory task queue."""

_tasks: list[str] = []


def add_task(title: str) -> int:
    """Add a task and return the number of queued tasks."""
    _tasks.append(title)
    return len(_tasks)


def list_tasks() -> list[str]:
    """Return a copy of queued task titles."""
    return list(_tasks)

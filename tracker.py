tasks = []


def add_task(title):
    """Add a task with the status open. A blank title raises ValueError."""
    if not title.strip():
        raise ValueError("A task needs a title.")
    task = {"title": title, "status": "open"}
    tasks.append(task)
    return task

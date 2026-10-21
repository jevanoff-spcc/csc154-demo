tasks = []


def add_task(title):
    """Add a task with the status open. An empty title is rejected."""
    if not title.strip():
        print("Error: a task needs a title.")
        return None
    task = {"title": title.strip(), "status": "open"}
    tasks.append(task)
    return task

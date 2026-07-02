# backend/app/core/task_constants.py

TASK_STATUS_TODO = "todo"
TASK_STATUS_IN_PROGRESS = "in_progress"
TASK_STATUS_DONE = "done"

ALLOWED_TASK_STATUSES = [
    TASK_STATUS_TODO,
    TASK_STATUS_IN_PROGRESS,
    TASK_STATUS_DONE
]


# STRICT WORKFLOW RULES
VALID_STATUS_FLOW = {
    TASK_STATUS_TODO: [TASK_STATUS_IN_PROGRESS],
    TASK_STATUS_IN_PROGRESS: [TASK_STATUS_DONE],
    TASK_STATUS_DONE: []
}


def validate_status_transition(current_status: str, new_status: str) -> bool:
    """
    Enforces strict workflow:
    todo → in_progress → done
    """

    return new_status in VALID_STATUS_FLOW.get(current_status, [])
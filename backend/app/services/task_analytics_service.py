def get_project_health(project_id: int):
    """
    Temporary analytics logic (mock version)
    """

    return {
        "project_id": project_id,
        "health_score": 82,
        "status": "GOOD",
        "tasks_completed": 14,
        "tasks_pending": 6,
        "risk_level": "LOW"
    }
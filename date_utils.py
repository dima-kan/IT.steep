from datetime import date


def days_until_deadline(deadline_str: str) -> int:
    deadline_date = date.fromisoformat(deadline_str)
    return (deadline_date - date.today()).days

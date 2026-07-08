from datetime import datetime
from zoneinfo import ZoneInfo


def should_run():

    now = datetime.now(
        ZoneInfo("Asia/Kolkata")
    )

    minutes = now.hour * 60 + now.minute

    # Morning: 9:15 - 9:44
    if 9 * 60 + 15 <= minutes < 9 * 60 + 45:
        return True

    # Afternoon: 3:30 - 3:59
    if 15 * 60 + 30 <= minutes < 16 * 60:
        return True

    return False

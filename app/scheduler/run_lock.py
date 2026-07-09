from datetime import datetime
from zoneinfo import ZoneInfo

from app.database.mongo import run_lock


def current_session():

    now = datetime.now(ZoneInfo("Asia/Kolkata"))

    if now.hour < 12:
        return "morning"

    return "afternoon"


def already_ran():

    today = datetime.now(
        ZoneInfo("Asia/Kolkata")
    ).strftime("%Y-%m-%d")

    session = current_session()

    record = run_lock.find_one({
        "date": today
    })

    if not record:
        return False

    return record.get(session, False)


def mark_run():

    today = datetime.now(
        ZoneInfo("Asia/Kolkata")
    ).strftime("%Y-%m-%d")

    session = current_session()

    run_lock.update_one(

        {
            "date": today
        },

        {
            "$set": {
                session: True
            }
        },

        upsert=True

    )

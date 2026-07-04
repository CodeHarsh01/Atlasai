from app.telegram.sender import send_message
from app.reports.weekly import generate_weekly_report


def notify_weekly():

    message = generate_weekly_report()

    send_message(message)
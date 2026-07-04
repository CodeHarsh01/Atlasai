from app.journal.filters import get_weekly_trades
from app.analytics.performance import calculate_performance
from app.reports.formatter import format_weekly_report


def generate_weekly_report():

    weekly = get_weekly_trades()

    stats = calculate_performance(weekly)

    return format_weekly_report(stats)
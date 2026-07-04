def format_weekly_report(stats):

    if stats["total_trades"] == 0:

        return (
            "📈 ATLAS WEEKLY REPORT\n\n"
            "No completed trades this week."
        )

    best = stats["best_trade"]
    worst = stats["worst_trade"]

    return (

        "📈 ATLAS WEEKLY REPORT\n\n"

        "━━━━━━━━━━━━━━━━━━\n"

        f"📊 Total Trades : {stats['total_trades']}\n"
        f"✅ Wins : {stats['wins']}\n"
        f"❌ Losses : {stats['losses']}\n"
        f"➖ Break-even : {stats['breakevens']}\n"
        f"🎯 Win Rate : {stats['win_rate']}%\n\n"

        "━━━━━━━━━━━━━━━━━━\n"

        f"💰 Net Profit : ₹{stats['net_profit']}\n"
        f"📈 Net Return : {stats['net_return']}%\n"
        f"💼 Capital Traded : ₹{stats['total_capital']}\n\n"

        "━━━━━━━━━━━━━━━━━━\n"

        f"🏆 Best Trade\n"
        f"{best['symbol']} ({best['pnl_percent']}%)\n\n"

        f"📉 Worst Trade\n"
        f"{worst['symbol']} ({worst['pnl_percent']}%)\n\n"

        "━━━━━━━━━━━━━━━━━━\n"

        f"⏳ Avg Holding : {stats['average_holding_days']} Days\n"
        f"🔥 Best Win Streak : {stats['largest_win_streak']}\n"
        f"📉 Worst Loss Streak : {stats['largest_loss_streak']}"

    )
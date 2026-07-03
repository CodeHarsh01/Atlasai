from app.telegram.sender import send_message

from app.telegram.formatter import (

    format_buy_alert,

    format_sell_alert,

    format_summary

)


def notify_buys(positions):

    message = format_buy_alert(

        positions

    )

    if message:

        send_message(message)


def notify_sells(positions):

    message = format_sell_alert(

        positions

    )

    if message:

        send_message(message)


def notify_summary(open_positions):

    message = format_summary(

        open_positions

    )

    send_message(message)
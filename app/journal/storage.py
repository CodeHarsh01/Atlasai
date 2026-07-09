from app.database.mongo import trades


def load_trades():

    return list(

        trades.find(

            {},

            {

                "_id": 0

            }

        )

    )


def save_trades(all_trades):

    trades.delete_many({})

    if all_trades:

        trades.insert_many(all_trades)


def add_trade(trade):

    trades.insert_one(trade)

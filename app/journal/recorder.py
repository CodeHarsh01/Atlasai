from app.journal.storage import (
    load_journal,
    save_journal
)


def record_trade(position):

    journal = load_journal()

    journal.append(position)

    save_journal(journal)
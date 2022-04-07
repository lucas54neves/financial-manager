from datetime import datetime

from utils.return_current_month_and_year import return_current_month_and_year


def separate_transactions_into_past_present_and_future(transactions):
    month, year = return_current_month_and_year()

    before = f"{year}-{int(month)}-1"
    before = datetime.strptime(before, "%Y-%m-%d").date()

    after = f"{year}-{int(month)+1}-1"
    after = datetime.strptime(after, "%Y-%m-%d").date()

    past_transactions = transactions[transactions["date"] < str(before)]
    present_transactions = transactions[
        (transactions["date"] >= str(before)) & (transactions["date"] < str(after))
    ]
    future_transactions = transactions[transactions["date"] >= str(after)]

    return past_transactions, present_transactions, future_transactions

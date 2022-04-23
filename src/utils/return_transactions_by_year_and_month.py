from datetime import datetime


def return_transactions_by_year_and_month(transactions, year, month):
    before = f"{year}-{int(month)}-1"
    before = datetime.strptime(before, "%Y-%m-%d").date()

    after = f"{year}-{int(month)+1}-1"
    after = datetime.strptime(after, "%Y-%m-%d").date()

    return transactions[
        (transactions["column_date"] >= str(before)) & (transactions["column_date"] < str(after))
    ]

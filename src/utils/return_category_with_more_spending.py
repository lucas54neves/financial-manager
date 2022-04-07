def return_category_with_more_spending(transactions):
    category_transactions = transactions.groupby(by=["category"])[
        "installment_value"
    ].sum()

    return category_transactions.idxmax(), category_transactions.max()

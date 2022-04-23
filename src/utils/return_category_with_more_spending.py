def return_category_with_more_spending(transactions):
    category_transactions = transactions.groupby(by=["column_category"])[
        "column_installment_value"
    ].sum()

    return category_transactions.idxmax(), category_transactions.max()

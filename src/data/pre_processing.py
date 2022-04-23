def pre_processing_apply(transaction):
    year = transaction["column_date"].year
    month = transaction["column_date"].month

    transaction["column_period"] = f"{year}|{month if month > 9 else ('0' + str(month))}"

    return transaction


def pre_processing(data):
    new_data = data.copy()

    new_data = new_data.apply(
        pre_processing_apply,
        axis=1,
    )

    return new_data

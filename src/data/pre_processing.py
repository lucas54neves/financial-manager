def pre_processing_apply(transaction):
    year = transaction["date"].year
    month = transaction["date"].month

    transaction["period"] = f"{year}|{month if month > 9 else ('0' + str(month))}"

    return transaction


def pre_processing(data):
    new_data = data.copy()

    new_data.rename(
        columns={
            "Data": "date",
            "Categoria": "category",
            "Valor parcela": "installment_value",
            "Descrição": "description",
        },
        inplace=True,
    )

    new_data = new_data.apply(
        pre_processing_apply,
        axis=1,
    )

    return new_data

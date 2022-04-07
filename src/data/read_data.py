import pandas as pd


def read_data(filename="src/data/data.xlsx"):
    return pd.read_excel(
        filename,
    )

from datetime import datetime

import plotly.express as px
import streamlit as st
from utils.convert_numeric_month_to_string import convert_numeric_month_to_string
from utils.return_current_month_and_year import return_current_month_and_year


def format_period(row):
    month_as_int = int(row["Period"].split("|")[1])
    month_as_string = convert_numeric_month_to_string(month_as_int)
    year = row["Period"].split("|")[0]

    row["Period"] = f"{month_as_string} {year}"

    return row


def display_expense_history_report(transactions):
    st.header("Expense history report")

    periods = [
        "Last three months",
        "Last six months",
        "Last year",
    ]

    periods_option = st.selectbox(
        "Period",
        periods,
        index=0,
    )

    current_month, current_year = return_current_month_and_year()

    if periods_option == "Last three months":
        month = current_month - 3

        if month < 1:
            month += 12
            year = current_year - 1
        else:
            year = current_year
    elif periods_option == "Last six months":
        month = current_month - 6

        if month < 1:
            month += 12
            year = current_year - 1
        else:
            year = current_year
    # if periods_option == "Last year":
    else:
        month = current_month
        year = current_year - 1

    before = f"{year}-{int(month)}-1"
    before = datetime.strptime(before, "%Y-%m-%d").date()

    after = f"{current_year}-{int(current_month)+1}-1"
    after = datetime.strptime(after, "%Y-%m-%d").date()

    _transactions = transactions[
        (transactions["date"] >= str(before)) & (transactions["date"] < str(after))
    ]

    _transactions = (
        _transactions.groupby("period").sum()["installment_value"].reset_index()
    )

    _transactions.rename(
        columns={
            "installment_value": "Total expenses",
            "period": "Period",
        },
        inplace=True,
    )

    _transactions = _transactions.apply(
        lambda row: format_period(row),
        axis=1,
    )

    fig = px.line(
        _transactions,
        x="Period",
        y="Total expenses",
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

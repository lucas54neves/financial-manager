from datetime import datetime

import plotly.express as px
import streamlit as st
from utils.convert_numeric_month_to_string import convert_numeric_month_to_string
from utils.return_current_month_and_year import return_current_month_and_year
from utils.translate_words import translate_words


def format_period(row, language):
    month_as_int = int(row["column_period"].split("|")[1])
    month_as_string = convert_numeric_month_to_string(month_as_int, language,)
    year = row["column_period"].split("|")[0]

    row["column_period"] = f"{month_as_string} {year}"

    return row


def display_expense_history_report(transactions, language):
    st.header(translate_words("expense_history_report_title", language,))

    periods = [
        translate_words("last_three_months", language,),
        translate_words("last_six_months", language,),
        translate_words("last_year", language,),
    ]

    periods_option = st.selectbox(
        translate_words("period_selectbox_option", language,),
        periods,
        index=0,
    )

    current_month, current_year = return_current_month_and_year()

    if periods_option == translate_words("last_three_months", language,):
        month = current_month - 3

        if month < 1:
            month += 12
            year = current_year - 1
        else:
            year = current_year
    elif periods_option == translate_words("last_six_months", language,):
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
        (transactions["column_date"] >= str(before)) & (transactions["column_date"] < str(after))
    ]

    _transactions = (
        _transactions.groupby("column_period").sum()["column_installment_value"].reset_index()
    )

    _transactions = _transactions.apply(
        lambda row: format_period(row, language,),
        axis=1,
    )

    _transactions.rename(
        columns={
            "column_installment_value": translate_words("column_total_expenses", language,),
            "column_period": translate_words("column_period", language,),
        },
        inplace=True,
    )

    fig = px.line(
        _transactions,
        x=translate_words("column_period", language,),
        y=translate_words("column_total_expenses", language,),
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

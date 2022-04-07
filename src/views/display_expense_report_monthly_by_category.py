import plotly.express as px
import streamlit as st
from utils.convert_numeric_month_to_string import convert_numeric_month_to_string
from utils.convert_string_month_to_numeric import convert_string_month_to_numeric
from utils.format_money import format_money
from utils.return_available_months_and_years import return_available_months_and_years
from utils.return_category_with_more_spending import return_category_with_more_spending
from utils.return_current_month_and_year import return_current_month_and_year
from utils.return_total_amount import return_total_amount
from utils.return_transactions_by_year_and_month import (
    return_transactions_by_year_and_month,
)


def display_expense_report_monthly_by_category(transactions):
    st.header("Expense report monthly by category")

    col1, col2 = st.columns([3, 1])

    with col2:
        current_month, current_year = return_current_month_and_year()
        chart_option = st.selectbox(
            "Chart",
            ["Bar chart", "Pie chart"],
        )

        years_and_month = return_available_months_and_years(transactions)

        years = list(years_and_month.keys())

        years_option = st.selectbox(
            "Year",
            years,
            index=years.index(current_year),
        )

        _months = [
            convert_numeric_month_to_string(month)
            for month in years_and_month[years_option]
        ]

        months_option = st.selectbox(
            "Month",
            _months,
            index=years_and_month[years_option].index(current_month),
        )

        _months_option = convert_string_month_to_numeric(months_option)

        _transactions_by_period = return_transactions_by_year_and_month(
            transactions,
            years_option,
            _months_option,
        )

    with col1:
        _transactions = (
            _transactions_by_period.groupby("category")
            .sum()["installment_value"]
            .reset_index()
        )

        transactions_for_chart = _transactions.rename(
            columns={
                "category": "Category",
                "installment_value": "Total expenses",
            },
        )

        if chart_option == "Bar chart":
            fig = px.bar(
                transactions_for_chart,
                title="Amount spent by category",
                x="Category",
                y="Total expenses",
            )
        # if chart_option == "Pie chart":
        else:
            fig = px.pie(
                transactions_for_chart,
                title="Amount spent by category",
                values="Total expenses",
                names="Category",
            )

        total_amount = return_total_amount(_transactions)

        (
            category_with_more_spending,
            _,
        ) = return_category_with_more_spending(_transactions)

        st.plotly_chart(
            fig,
            use_container_width=True,
        )
        st.write(f"Total amount: {format_money(total_amount)}")
        st.write(f"Category with more spending: {category_with_more_spending}")

    with st.expander("Transactions from period"):
        hide_table_row_index = """
            <style>
            tbody th {display:none}
            .blank {display:none}
            </style>
            """

        st.markdown(hide_table_row_index, unsafe_allow_html=True)

        transactions_for_table = _transactions_by_period[
            [
                "description",
                "installment_value",
                "date",
                "category",
            ]
        ]

        transactions_for_table = transactions_for_table.rename(
            columns={
                "category": "Category",
                "installment_value": "Expense",
                "description": "Description",
                "date": "Date",
            },
        )

        transactions_for_table["Expense"] = transactions_for_table.apply(
            lambda row: format_money(row["Expense"]),
            axis=1,
        )
        transactions_for_table["Date"] = transactions_for_table.apply(
            lambda row: row["Date"].strftime("%d/%m/%Y"),
            axis=1,
        )

        st.table(transactions_for_table)

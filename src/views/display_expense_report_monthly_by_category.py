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
from utils.translate_words import translate_words


def display_expense_report_monthly_by_category(transactions, language):
    st.header(
        translate_words(
            "expense_history_report_monthly_by_category_title",
            language,
        ),
    )

    col1, col2 = st.columns([3, 1])

    with col2:
        current_month, current_year = return_current_month_and_year()
        chart_option = st.selectbox(
            translate_words("chart", language),
            [
                translate_words("bar_chart", language),
                translate_words("pie_chart", language),
            ],
        )

        years_and_month = return_available_months_and_years(transactions)

        years = list(years_and_month.keys())

        years_option = st.selectbox(
            translate_words("year_selectbox_option", language),
            years,
            index=years.index(current_year),
        )

        _months = [
            convert_numeric_month_to_string(month, language)
            for month in years_and_month[years_option]
        ]

        months_option = st.selectbox(
            translate_words(
                "month_selectbox_option",
                language,
            ),
            _months,
            index=years_and_month[years_option].index(
                current_month
                if years_option == current_year
                else years_and_month[years_option][0]
            ),
        )

        _months_option = convert_string_month_to_numeric(months_option, language)

        _transactions_by_period = return_transactions_by_year_and_month(
            transactions,
            years_option,
            _months_option,
        )

    with col1:
        _transactions = (
            _transactions_by_period.groupby("column_category")
            .sum()["column_installment_value"]
            .reset_index()
        )

        transactions_for_chart = _transactions.rename(
            columns={
                "column_category": translate_words(
                    "column_category",
                    language,
                ),
                "column_installment_value": translate_words(
                    "column_total_expenses",
                    language,
                ),
            },
        )

        if chart_option == translate_words("bar_chart", language):
            fig = px.bar(
                transactions_for_chart,
                title=translate_words(
                    "title_chart_by_category",
                    language,
                ),
                x=translate_words(
                    "column_category",
                    language,
                ),
                y=translate_words(
                    "column_total_expenses",
                    language,
                ),
            )
        # if chart_option == "Pie chart":
        else:
            fig = px.pie(
                transactions_for_chart,
                title=translate_words(
                    "title_chart_by_category",
                    language,
                ),
                values=translate_words(
                    "column_total_expenses",
                    language,
                ),
                names=translate_words(
                    "column_category",
                    language,
                ),
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
        st.write(
            f"{translate_words('total_spent_in_the_month', language)}: {format_money(total_amount)}"
        )
        st.write(
            f"{translate_words('category_with_more_spending', language)}: {category_with_more_spending}"
        )

    with st.expander(translate_words("transactions_from_period", language)):
        hide_table_row_index = """
            <style>
            tbody th {display:none}
            .blank {display:none}
            </style>
            """

        st.markdown(hide_table_row_index, unsafe_allow_html=True)

        transactions_for_table = _transactions_by_period[
            [
                "column_description",
                "column_installment_value",
                "column_date",
                "column_category",
            ]
        ]

        transactions_for_table[
            "column_installment_value"
        ] = transactions_for_table.apply(
            lambda row: format_money(row["column_installment_value"]),
            axis=1,
        )
        transactions_for_table["column_date"] = transactions_for_table.apply(
            lambda row: row["column_date"].strftime("%d/%m/%Y"),
            axis=1,
        )

        transactions_for_table = transactions_for_table.rename(
            columns={
                "column_category": translate_words(
                    "column_category",
                    language,
                ),
                "column_installment_value": translate_words(
                    "column_expense",
                    language,
                ),
                "column_description": translate_words(
                    "column_description",
                    language,
                ),
                "column_date": translate_words(
                    "column_date",
                    language,
                ),
            },
        )

        st.table(transactions_for_table)

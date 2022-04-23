from data.pre_processing import pre_processing
from data.read_data import read_data
from views.display_expense_history_report import display_expense_history_report
from views.display_expense_report_monthly_by_category import (
    display_expense_report_monthly_by_category,
)
from views.display_sidebar import display_sidebar
from views.display_title import display_title


def main():
    data = read_data()
    data = pre_processing(data)

    language = display_sidebar()
    display_title(language)
    display_expense_history_report(data, language)
    display_expense_report_monthly_by_category(data, language)


main()

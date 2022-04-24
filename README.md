# financial-manager

Financial organizer using the Streamlit lib for data visualization.

## App access

The app's deployment was done on Heroku and can be accessed at [this link](https://neves-financial-organizer.herokuapp.com/).

## Data analyzed

The data used for analysis was randomly generated through [this script](https://github.com/lucas54neves/financial-organizer/blob/main/src/data/generate_data.py).

## Features

The app has two reports, an expense history report and an expense report monthly by category.

### Expense history report

The expense history report displays a line graph of apend by past periods. There is the option to display spending for the last three months, the last six months and the last year (last twelve months).

![Expense history report](https://github.com/lucas54neves/financial-organizer/blob/main/.github/images/expense_history_report.png)

### Expense report monthly by category

The expense report monthly by category displays spend by each category in a specific month. There is the option to choose between a bar chart and a pie chart. You can choose any month from the database.

![Expense history report 1](https://github.com/lucas54neves/financial-organizer/blob/main/.github/images/expense_report_monthly_by_category_1.png)

![Expense history report 2](https://github.com/lucas54neves/financial-organizer/blob/main/.github/images/expense_report_monthly_by_category_2.png)

The total spend for the month and the category with the highest spend are displayed below the graph.

![Total spend for the month and the category with the highest spend](https://github.com/lucas54neves/financial-organizer/blob/main/.github/images/expense_report_monthly_by_category_3.png)

All transactions for the month are displayed at the end.

![All transactions for the month](https://github.com/lucas54neves/financial-organizer/blob/main/.github/images/expense_report_monthly_by_category_4.png)

### Language option

There is an option to choose the display language. It is possible to choose between Portuguese and English.

![Language option](https://github.com/lucas54neves/financial-organizer/blob/main/.github/images/languages.png)

## Development

### To run locally

```
python3 -m venv venv
source venv/bin/active
pip install -r requirements.txt
streamlit run src/main.py
```

## Versions

### 0.1.0

-   [x] Expense history report.
-   [x] Expense report monthly by category.
-   [x] Display language option between English and Portuguese.

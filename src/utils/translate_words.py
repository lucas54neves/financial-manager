def translate_words(word, language):
    words = {
        "column_description": {
            "English": "Description",
            "Portuguese": "Descrição",
        },
        "column_purchase_place": {
            "English": "Purchase place",
            "Portuguese": "Local de compra",
        },
        "column_total_amount": {
            "English": "Total amount",
            "Portuguese": "Valor total",
        },
        "column_card": {
            "English": "Card",
            "Portuguese": "Cartão",
        },
        "column_date": {
            "English": "Date",
            "Portuguese": "Data",
        },
        "column_category": {
            "English": "Category",
            "Portuguese": "Categoria",
        },
        "column_is_installment": {
            "English": "Is installment",
            "Portuguese": "É parcelada",
        },
        "column_current_installment": {
            "English": "Current installment",
            "Portuguese": "Parcela atual",
        },
        "column_total_installment": {
            "English": "Total installment",
            "Portuguese": "Total de parcelas",
        },
        "column_installment_value": {
            "English": "Installment value",
            "Portuguese": "Valor da parcela",
        },
        "column_period": {
            "English": "Period",
            "Portuguese": "Período",
        },
        "title": {
            "English": "Financial Organizer",
            "Portuguese": "Organizador Financeiro",
        },
        "last_three_months": {
            "English": "Last three months",
            "Portuguese": "Últimos três meses",
        },
        "last_six_months": {
            "English": "Last six months",
            "Portuguese": "Últimos seis meses",
        },
        "last_year": {
            "English": "Last year",
            "Portuguese": "Último ano",
        },
        "period_selectbox_option": {
            "English": "Period",
            "Portuguese": "Período",
        },
        "column_total_expenses": {
            "English": "Total expenses",
            "Portuguese": "Total de gastos",
        },
        "expense_history_report_title": {
            "English": "Expense history report",
            "Portuguese": "Relatório do histórico de gastos",
        },
        "months": {
            "English": "Expense history report",
            "Portuguese": "Relatório do histórico de gastos",
        },
        "january": {
            "English": "January",
            "Portuguese": "Janeiro",
        },
        "february": {
            "English": "February",
            "Portuguese": "Fevereiro",
        },
        "march": {
            "English": "March",
            "Portuguese": "Março",
        },
        "april": {
            "English": "April",
            "Portuguese": "Abril",
        },
        "may": {
            "English": "May",
            "Portuguese": "Maio",
        },
        "june": {
            "English": "June",
            "Portuguese": "Junho",
        },
        "july": {
            "English": "July",
            "Portuguese": "Julho",
        },
        "august": {
            "English": "August",
            "Portuguese": "Agosto",
        },
        "september": {
            "English": "September",
            "Portuguese": "Setembro",
        },
        "october": {
            "English": "October",
            "Portuguese": "Outubro",
        },
        "november": {
            "English": "November",
            "Portuguese": "Novembro",
        },
        "december": {
            "English": "December",
            "Portuguese": "Dezembro",
        },
        "expense_history_report_monthly_by_category_title": {
            "English": "Expense report monthly by category",
            "Portuguese": "Relatório de gastos mensais por categoria",
        },
        "chart": {
            "English": "Chart",
            "Portuguese": "Gráfico",
        },
        "bar_chart": {
            "English": "Bar chart",
            "Portuguese": "Gráfico de barras",
        },
        "pie_chart": {
            "English": "Pie chart",
            "Portuguese": "Gráfico de pizza",
        },
        "year_selectbox_option": {
            "English": "Year",
            "Portuguese": "Ano",
        },
        "month_selectbox_option": {
            "English": "Month",
            "Portuguese": "Mês",
        },
        "title_chart_by_category": {
            "English": "Amount spent by category",
            "Portuguese": "Gastos por categoria",
        },
        "total_spent_in_the_month": {
            "English": "Total spent in the month",
            "Portuguese": "Total gasto no mês",
        },
        "category_with_more_spending": {
            "English": "Category with more spending",
            "Portuguese": "Categoria com maior gasto",
        },
        "transactions_from_period": {
            "English": "Transactions from period",
            "Portuguese": "Transações do período",
        },
        "column_expense": {
            "English": "Expense",
            "Portuguese": "Despesa",
        },
    }

    return words[word][language]

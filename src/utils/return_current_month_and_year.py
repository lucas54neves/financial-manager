from datetime import datetime


def return_current_month_and_year():
    today = datetime.today()
    
    month = today.month
    year = today.year

    return month, year

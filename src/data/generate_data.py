from datetime import date, datetime
from random import randint, random

import pandas as pd
import requests


def generate_word(number_of_words, is_description=True):
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = requests.get(word_site)
    words = response.content.splitlines()

    description = []

    for _ in range(number_of_words):
        description.append(words[randint(0, len(words) - 1)].decode("utf-8"))

    if is_description:
        description[0] = description[0].capitalize()
    else:
        description = [value.capitalize() for value in description]

    return " ".join(description)


def generate_description():
    number_of_words = randint(2, 5)

    return generate_word(number_of_words)


def generate_purchase_place():
    number_of_words = randint(2, 5)

    return generate_word(number_of_words, False)


def generate_category():
    categories = [
        "residential_accounts",
        "education",
        "market",
        "home",
        "health",
        "transport",
        "bars_and_restaurants",
        "purchases",
        "personal_cares",
        "work_expenses",
        "domestic_servants",
        "family",
        "taxes",
        "leisure",
        "other_expenses",
        "tv_internet_phone",
        "bank_charges",
        "trip",
    ]

    return categories[randint(0, len(categories) - 1)]


def generate_boolean():
    return randint(0, 1)


def generate_amount():
    return round(random() * 10 ** (randint(1, 3)), 2)


def generate_date():
    date_now = datetime.now()

    return date(
        randint(
            date_now.year - 10,
            date_now.year + 5,
        ),
        randint(
            1,
            12,
        ),
        randint(
            1,
            28,
        ),
    )


def show_progress(max, index):
    taxa = f"{'0' if (index/max*100) < 10 else ''}{(index/max*100):.2f}%"
    interval = f"{index}/{max}"

    print(f"Progress: {taxa} {interval}")


def generate_data(number_of_rows=50):
    data = []

    for i in range(1, number_of_rows):
        description = generate_description()
        purchase_place = generate_purchase_place()
        total_amount = generate_amount()
        card = generate_boolean()
        random_date = generate_date()
        category = generate_category()
        is_installment = generate_boolean() if card else 0

        if is_installment:
            total_installment = randint(1, 12)
            installment_value = 400 / total_installment

            for current_installment in range(1, total_installment + 1):
                data.append(
                    {
                        "description": description,
                        "purchase_place": purchase_place,
                        "total_amount": total_amount,
                        "card": card,
                        "date": random_date,
                        "category": category,
                        "is_installment": is_installment,
                        "current_installment": current_installment,
                        "total_installment": total_installment,
                        "installment_value": installment_value,
                    }
                )

        else:
            total_installment = 1
            current_installment = 1
            installment_value = total_amount

            data.append(
                {
                    "description": description,
                    "purchase_place": purchase_place,
                    "total_amount": total_amount,
                    "card": card,
                    "date": random_date,
                    "category": category,
                    "is_installment": is_installment,
                    "current_installment": current_installment,
                    "total_installment": total_installment,
                    "installment_value": installment_value,
                }
            )

        show_progress(
            number_of_rows,
            i,
        )

    return pd.DataFrame(data)


data = generate_data(2000)
data.to_excel(
    f"src/data/{int(datetime.now().timestamp() * 1000000)}-data.xlsx",
    index=False,
)

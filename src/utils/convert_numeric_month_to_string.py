from utils.translate_words import translate_words


def convert_numeric_month_to_string(numeric_month, language):
    months = {
        1: translate_words("january", language),
        2: translate_words("february", language),
        3: translate_words("march", language),
        4: translate_words("april", language),
        5: translate_words("may", language),
        6: translate_words("june", language),
        7: translate_words("july", language),
        8: translate_words("august", language),
        9: translate_words("september", language),
        10: translate_words("october", language),
        11: translate_words("november", language),
        12: translate_words("december", language),
    }

    return months[numeric_month]

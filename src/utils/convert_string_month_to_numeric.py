from utils.translate_words import translate_words


def convert_string_month_to_numeric(string_month, language):
    months = {
        translate_words("january", language): 1,
        translate_words("february", language): 2,
        translate_words("march", language): 3,
        translate_words("april", language): 4,
        translate_words("may", language): 5,
        translate_words("june", language): 6,
        translate_words("july", language): 7,
        translate_words("august", language): 8,
        translate_words("september", language): 9,
        translate_words("october", language): 10,
        translate_words("november", language): 11,
        translate_words("december", language): 12,
    }

    return months[string_month]

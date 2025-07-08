# pylint: disable=missing-docstring

# TODO: add some currency rates
RATES = {
    "USDEUR": 0.85,
    "GBPEUR": 1.13,
    "CHFEUR": 0.86,
    "EURGBP": 0.885
}

def convert(amount, currency):
    """returns the converted amount in the given currency
    amount is a tuple like (100, "EUR")
    currency is a string
    """

    value, from_currency = amount

    if from_currency == currency:
        return round(value)

    key = from_currency + currency
    if key in RATES:
        rate = RATES[key]
        return round(value * rate)

    inverse_key = currency + from_currency
    if inverse_key in RATES:
        rate = RATES[inverse_key]
        return round(value / rate)
    else:
        return None


print(convert((100, "USD"), "EUR"))
print(convert((100, "EUR"), "GBP"))
print(convert((100, "GBP"), "EUR"))
print(convert((100, "EUR"), "EUR"))

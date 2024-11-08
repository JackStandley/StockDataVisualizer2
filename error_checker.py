import re

def validate_symbol(symbol):
    return bool(re.match(r"^[A-Z]{1,5}$", symbol))
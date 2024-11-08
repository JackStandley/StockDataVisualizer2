#
#store key program data and provide
api_key = "U4LDC0DB6CQ3FO68"
_stock_symbol = None
_stock_data = None
_chart_type = None
_time_series = None
_start_date = None
_end_date = None

#getters and setters
def set_stock_symbol(symbol):
    global _stock_symbol
    _stock_symbol = symbol

def set_stock_data(data):
    global _stock_data
    _stock_data = data

def set_chart_type(chart_type):
    global _chart_type
    _chart_type = chart_type

def set_time_series(series):
    global _time_series
    _time_series = series

def set_dates(start, end):
    global _start_date, _end_date
    _start_date, _end_date = start, end

def get_api_key():
    return api_key

def get_stock_symbol():
    return _stock_symbol

def get_stock_data():
    return _stock_data

def get_chart_type():
    return _chart_type

def get_time_series():
    return _time_series

def get_start_date():
    return _start_date

def get_end_date():
    return _end_date
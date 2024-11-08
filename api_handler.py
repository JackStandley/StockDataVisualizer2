import requests
from app_data import get_time_series, get_stock_symbol, get_api_key, set_stock_data

def fetch_stock_data():
    interval = "&interval=15min" if get_time_series() == "TIME_SERIES_INTRADAY" else ""
    url = f"https://www.alphavantage.co/query?function={get_time_series()}&symbol={get_stock_symbol()}{interval}&apikey={get_api_key()}"
    response = requests.get(url)
    data = response.json()
    set_stock_data(data)
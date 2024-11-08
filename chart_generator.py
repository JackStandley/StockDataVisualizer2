
import pygal
from pygal.style import Style
from datetime import datetime
from app_data import get_stock_data, get_stock_symbol, get_start_date, get_end_date, get_chart_type

def generate_chart(chart_type):
    stock_data = get_stock_data()
    if not stock_data:
        print("No stock data retrieved. Check if API data is being fetched correctly.")
        return None
    print("Stock data successfully received")

    #intitialize chart
    chart = pygal.Bar() if chart_type == "Bar" else pygal.Line()
    data_points = extract_data_points(stock_data)
    if data_points and data_points["dates"]:
        chart.title = f"Stock Data for {get_stock_symbol()}: {get_start_date()} to {get_end_date()}"
        chart.x_labels = [datetime.strptime(date, "%Y-%m-%d").strftime("%b %d") for date in data_points["dates"]]
    
        #add series for each type of stock data
        chart.add("Open", data_points["Open"])
        chart.add("High", data_points["High"])
        chart.add("Low", data_points["Low"])
        chart.add("Close", data_points["Close"])

        #return the chart as an SVG string
        return chart.render(is_unicode=True)
    else:
        print("No data available within the selected date range.")
        return None

def extract_data_points(stock_json):
    try:
        time_series_key = next(key for key in stock_json if "Time Series" in key)
    except StopIteration:
        print("Time series data not found in API response.")
        return None

    stock_data = stock_json[time_series_key]
    start_date = datetime.strptime(get_start_date(), "%Y-%m-%d")
    end_date = datetime.strptime(get_end_date(), "%Y-%m-%d")
    
    data_points = {"dates": [], "Open": [], "High": [], "Low": [], "Close": []}
    for date_str, values in sorted(stock_data.items()):
        date = datetime.strptime(date_str, "%Y-%m-%d")
        if start_date <= date <= end_date:
            data_points["dates"].append(date_str)
            data_points["Open"].append(float(values["1. open"]))
            data_points["High"].append(float(values["2. high"]))
            data_points["Low"].append(float(values["3. low"]))
            data_points["Close"].append(float(values["4. close"]))

    return data_points

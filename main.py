
from app_data import set_stock_symbol, set_chart_type, set_time_series, set_dates, get_chart_type
from api_handler import fetch_stock_data
from chart_generator import generate_chart

def run_chart_generation(symbol, chart_type, time_series, start, end):
    # Set values based on passed parameters
    set_stock_symbol(symbol)
    set_chart_type(chart_type)
    set_time_series(time_series)
    set_dates(start, end)

    # Fetch and generate chart
    fetch_stock_data()
    try:
        generate_chart(get_chart_type())
        print("Chart generated successfully.")
    except ValueError as e:
        print(f"Error generating chart: {e}")

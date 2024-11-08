from flask import Flask, render_template, request, jsonify, flash, redirect
from main import run_chart_generation  # Import the function to generate the chart
import csv  # Import the csv module to handle CSV files

# Initialize the Flask app
app = Flask(__name__)
app.config["DEBUG"] = True  # Enable debug mode for detailed error logs during development
app.config['SECRET_KEY'] = 'your secret key'  # Set a secret key for session management and flash messages

# Define the main route for the application
@app.route('/')
def index():
    return render_template('index.html', chart_svg=None)

# Define an API route to retrieve stock symbols from a CSV file
@app.route('/api/symbols')
def get_symbols():
    symbols = []
    with open('stocks.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)  #read the CSV file as a dictionary
        for row in csv_reader:
            symbols.append(row['Symbol'])  #append each symbol to the list
    return jsonify(symbols)  #return the list of symbols as a JSON response

#define a route to handle chart generation requests
@app.route('/generate_chart', methods=['POST'])
def generate_chart():
    try:
        symbol = request.form.get('symbol')
        chart_type = request.form.get('chartType')
        time_series = request.form.get('timeSeries')
        start_date = request.form.get('startDate')
        end_date = request.form.get('endDate')

        svg_chart = run_chart_generation(symbol, chart_type, time_series, start_date, end_date)

        #render it on the main page
        if svg_chart:
            return render_template('index.html', chart_svg=svg_chart)
        else:
            flash("Error generating chart data.")
            return redirect('/')
    except Exception as e:
        
        flash(f'Error generating chart: {e}')
        return redirect('/')
    
if __name__ == '__main__':
    app.run(host="0.0.0.0") 

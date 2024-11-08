# app.py

from flask import Flask, render_template, request, jsonify, flash, redirect
from main import run_chart_generation  # Import the modified function from main.py
import csv

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SECRET_KEY'] = 'your secret key'

@app.route('/')
def index():
    return render_template('index.html', chart_svg=None)  # Include an optional chart_svg parameter

@app.route('/api/symbols')
def get_symbols():
    symbols = []
    with open('stocks.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            symbols.append(row['Symbol'])
    return jsonify(symbols)

@app.route('/generate_chart', methods=['POST'])
def generate_chart():
    try:
        symbol = request.form.get('symbol')
        chart_type = request.form.get('chartType')
        time_series = request.form.get('timeSeries')
        start_date = request.form.get('startDate')
        end_date = request.form.get('endDate')

        # Generate chart SVG
        svg_chart = run_chart_generation(symbol, chart_type, time_series, start_date, end_date)

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

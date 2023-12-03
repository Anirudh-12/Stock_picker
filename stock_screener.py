# Import necessary libraries
import csv

from flask import Flask, render_template, request
import yfinance as yf
from nsetools import Nse

# Create a Flask web application
app = Flask(__name__)


# Function to get all NSE stock symbols
# Function to get all NSE stock symbols


# Function to get stock data from Yahoo Finance
def get_stock_data(symbol):
    try:
        stock = yf.Ticker(symbol)
        data = stock.info
        return data
    except:
        return None


# Function to filter stocks based on user input
def filter_stocks(stocks, filters):
    filtered_stocks = []

    for stock in stocks:
        include_stock = True

        for filter_name, filter_range in filters.items():
            # Check if the filter name is present in the stock dictionary
            if filter_name not in stock:
                include_stock = False
                break

            stock_value = stock[filter_name]

            # Check if the stock value is within the specified range
            if not (float(filter_range[0]) <= float(stock_value) <= float(filter_range[1])):
                include_stock = False
                break

        if include_stock:
            filtered_stocks.append(stock)

    return filtered_stocks



# Route for the home page
@app.route('/')
def home():
    # Sample Indian stock data for testing

    # Sample stock data
    myFile = open('data.csv', 'r')
    reader = csv.DictReader(myFile)
    sample_indian_stocks = list(reader)


    return render_template('index.html', stocks=sample_indian_stocks)


# Route to handle form submission
# Route to handle form submission
@app.route('/results', methods=['POST'])
def results():
    # Get user input from the form
    filters = {}

    # Iterate through form data to extract filter values
    for key, value in request.form.items():
        print(value)
        if key.startswith('filter_name_'):
            filter_name = value
            print(filter_name)

            filter_index = key.split('_')[-1]
            min_value = request.form.get(f'filter_min_{filter_index}', '')
            max_value = request.form.get(f'filter_max_{filter_index}', '')

            # Skip filters with empty values
            if min_value or max_value:
                filters[filter_name] = (
                float(min_value) if min_value else 0, float(max_value) if max_value else float('inf'))

    # Get a list of all NSE stock symbols

    # Get a list of all NSE stock symbols
    # Get stock data for all NSE stocks
    # Sample stock data
    myFile = open('data.csv', 'r')
    reader = csv.DictReader(myFile)
    all_stocks = list(reader)


    # Filter stocks based on user input
    filtered_stocks = filter_stocks(all_stocks, filters)

    # Render the index.html template with the results
    return render_template('index.html', stocks=filtered_stocks)


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)

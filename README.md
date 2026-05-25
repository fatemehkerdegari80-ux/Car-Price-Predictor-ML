# Car Price Predictor

This is a Python project that scrapes car data from TrueCar and uses Machine Learning to predict prices.

## How it Works
1. **Scraping:** It gets car information (Price, Mileage, Year) from TrueCar.com based on the model you enter.
2. **Database:** It saves the data into a MySQL database named `cars_information`.
3. **Machine Learning:** It uses a Decision Tree model to estimate your car's price based on its mileage and year.

## Requirements
You need to install these libraries:
- `requests`
- `beautifulsoup4`
- `mysql-connector-python`
- `scikit-learn`

## Setup
1. Create a MySQL database named `cars_information`.
2. Create two tables: `price` and `milesyear`.
3. Run the script: `python your_script_name.py`

## Features
- Real-time data scraping.
- SQL Database integration.
- Simple AI for price estimation.

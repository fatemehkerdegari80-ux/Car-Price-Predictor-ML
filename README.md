# 🚗 Car Price Estimator

A Python project that estimates the price of a used car based on its **mileage** and **year of manufacture** using:

- Web scraping (TrueCar)
- MySQL database storage
- Decision Tree Machine Learning model (scikit-learn)

---

## 🚀 Overview

This project collects real-world used car data from the web, stores it in a database, and trains a model to predict car prices.

### Workflow:

1. Scrape car listings from TrueCar
2. Extract:
   - Price
   - Mileage
   - Year
3. Store data in MySQL
4. Train a Decision Tree model
5. Predict price based on user input

---

## 🧠 Features

- 🌐 Web scraping using `requests` and `BeautifulSoup`
- 🗄️ MySQL database integration
- 🤖 Machine Learning using `DecisionTreeClassifier`
- 📊 Real-world data-driven predictions
- 🧩 Simple interactive CLI interface (Persian prompts)

---

## ⚙️ Technologies Used

- Python
- requests
- BeautifulSoup (bs4)
- regex (`re`)
- MySQL (`mysql.connector`)
- scikit-learn (`DecisionTreeClassifier`)

---

## 📥 Input

User provides:

- Car model (for scraping)
- Mileage (کارکرد)
- Year (سال ساخت)

---

## 📤 Output

- Estimated car price based on trained model

Example:

```
قيمت احتمالي ماشين شما: 25000
```

---

## 🛠️ How It Works

### 1. Web Scraping

- Fetches pages from:
  ```
  https://www.truecar.com/used-cars-for-sale/listings/<model>/?page=<n>
  ```
- Extracts:
  - Price using regex
  - Mileage
  - Year

---

### 2. Data Storage

- Stores scraped data in MySQL tables:
  - `price`
  - `milesyear`

---

### 3. Model Training

- Reads data from database
- Builds dataset:
  - `X = [mileage, year]`
  - `y = price`
- Trains a Decision Tree classifier

---

### 4. Prediction

- Takes user input
- Predicts price using trained model

---

## 🗃️ Database Structure

### Table: price
| Column |
|--------|
| price  |

### Table: milesyear
| Column |
|--------|
| miles  |
| year   |

---

## ▶️ How to Run

1. Install dependencies:

```bash
pip install requests beautifulsoup4 mysql-connector-python scikit-learn
```

2. Setup MySQL database:

```sql
CREATE DATABASE cars_information;

CREATE TABLE price (
    price INT
);

CREATE TABLE milesyear (
    miles INT,
    year INT
);
```

3. Run the script:

```bash
python script.py
```

---

## 💡 Applications

- Car price estimation tools
- Data-driven pricing analysis
- Learning web scraping + ML pipelines
- Educational projects


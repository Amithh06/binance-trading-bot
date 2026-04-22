# Binance Futures Testnet Trading Bot

## 📌 Overview

This project is a Python-based CLI trading bot that interacts with Binance Futures Testnet (USDT-M).
It allows users to place MARKET, LIMIT, and STOP-LIMIT orders with proper validation, logging, and structured architecture.

The goal of this project is to demonstrate API integration, clean code structure, and handling of real-world trading constraints.

---

## 🚀 Features

* Place **Market Orders** (instant execution)
* Place **Limit Orders** (execute at target price)
* Place **Stop-Limit Orders** (trigger-based execution) 
* Supports both **BUY** and **SELL**
* CLI-based interface using `argparse`
* Input validation and error handling
* Logging of API requests, responses, and errors
* Modular and reusable code structure

---

## 🛠️ Tech Stack

* Python 3.x
* python-binance
* python-dotenv

---

## 📁 Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── bot.log
│
├── cli.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```
git clone <your-repo-url>
cd trading_bot
```

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```
API_KEY=your_api_key
API_SECRET=your_secret_key
```

---

## ▶️ Usage

### ✅ Market Order

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
```

### ✅ Limit Order

```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 80000
```

### ✅ Stop-Limit Order (Bonus)

```
python cli.py --symbol BTCUSDT --side SELL --type STOP --quantity 0.002 --price 77000 --stop_price 77500
```

---

## 📊 Output

The CLI displays:

* Order summary
* Order response (orderId, status, executedQty, avgPrice)
* Success / pending status message

---

## 📁 Logging

Logs are stored in:

```
logs/bot.log
```

Logs include:

* API request parameters
* API responses
* Errors and exceptions

---

## ⚠️ Assumptions

* Uses Binance Futures Testnet (no real funds involved)
* Minimum order value ≥ 100 USDT (exchange constraint)
* User has sufficient test balance

---

## 🧠 Design Highlights

* Separation of concerns (client, orders, validators, CLI)
* Reusable API client wrapper
* Input validation before API calls
* Error handling for API and runtime issues
* Logging for debugging and traceability

---

## 🔮 Future Improvements

* Cancel order functionality
* Auto "sell all" feature
* Stop-loss / trailing stop
* Web-based UI dashboard
* Strategy-based trading (grid, scalping, etc.)

---

## ✅ Conclusion

This project demonstrates practical API integration, clean architecture, and handling of real-world trading scenarios.
It can be extended into a full-featured trading system.

---

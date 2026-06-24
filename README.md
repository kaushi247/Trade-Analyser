# 📈 Trade Analyzer Dashboard

A Flask-based web application that helps traders analyze their trading performance using CSV files. The dashboard provides profit analytics, risk assessment, behavioral insights, sector-wise performance, strategy evaluation, and interactive visualizations.

## 🚀 Live Demo

https://trade-analyser-cphv.onrender.com

---

## ✨ Features

### 📊 Trading Analytics
- Total Profit Calculation
- Win Rate Analysis
- Best Performing Stock
- Worst Performing Stock
- Average Holding Time
- Total Trades Counter

### 🛡 Risk Analysis
- Profit Factor Calculation
- Risk Rating System
- Performance Comparison
- Trading Discipline Assessment

### 🧠 AI Trading Insights
- AI Trading Coach
- Behaviour Analysis
- Trading Companion Q&A
- Personalized Trading Suggestions

### 🏢 Sector Analysis
- Best Sector Identification
- Worst Sector Identification
- Sector-wise Profit Breakdown
- Interactive Sector Performance Chart

### 📈 Strategy Analysis
- Best Trading Strategy
- Worst Trading Strategy
- Strategy Profit Distribution
- Interactive Pie Chart Visualization

### 📋 Data Visualization
- Interactive Plotly Charts
- Responsive Dashboard
- Bootstrap UI Design
- CSV Upload Support

---

## 🛠 Tech Stack

### Backend
- Python
- Flask
- Pandas

### Frontend
- HTML5
- CSS3
- Bootstrap 5

### Data Visualization
- Plotly

### Deployment
- Render
- Gunicorn

---

## 📂 Project Structure

```text
Trade-Analyzer/
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
├── Procfile
├── .gitignore
├── README.md
└── sample_trades.csv
```

---

## 📥 CSV Format

The uploaded CSV file must contain the following columns:

| Column | Description |
|----------|-------------|
| Stock | Stock Name |
| Sector | Industry Sector |
| Strategy | Trading Strategy |
| BuyPrice | Buy Price |
| SellPrice | Sell Price |
| Quantity | Quantity Purchased |
| HoldingHours | Holding Duration |

Example:

```csv
Stock,Sector,Strategy,BuyPrice,SellPrice,Quantity,HoldingHours
TCS,IT,Intraday,3500,3700,10,2
INFY,IT,Swing,1400,1450,15,5
RELIANCE,Energy,Intraday,2500,2450,20,8
HDFC,Banking,Swing,1600,1700,10,3
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/kaushi247/Trade-Analyser.git
cd Trade-Analyser
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## 🎯 Key Metrics Generated

- Total Profit
- Win Rate
- Profit Factor
- Risk Rating
- Average Holding Time
- Best/Worst Stock
- Best/Worst Sector
- Best/Worst Strategy
- Trading Behaviour Analysis

---

## 📸 Dashboard Highlights

- Interactive Plotly Charts
- AI Trading Coach
- Behaviour Analysis
- Risk Rating System
- Sector Performance Analytics
- Strategy Distribution Insights
- Trading Companion Chat
- Performance Comparison Metrics

---

## 🔮 Future Improvements

- PDF Report Generation
- Dark Mode
- Portfolio Analytics
- Monthly Profit Tracking
- Trade Journal
- AI-Powered Recommendations
- Multi-CSV Comparison

---

## 👨‍💻 Author

**Kaushalendra Singh**

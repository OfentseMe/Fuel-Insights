# ⛽ Petrol Spending Tracker

A personal fuel spending analysis dashboard to help you understand your petrol habits, save money, and make smarter fuel decisions.

## 🚀 Overview

The Petrol Spending Tracker is designed for individuals who want to gain insights into their fuel spending patterns, identify cost-saving opportunities, and track their consumption habits over time.

### Key Features

- **📊 Personal Dashboard** - Track your total spending, fuel consumption, and visit frequency
- **🔍 Smart Insights** - Discover your spending patterns and get personalized recommendations
- **📋 Data Management** - View and export your fuel transaction history
- **🎯 Clean Interface** - Easy-to-use design that makes data analysis simple
- **📈 Spending Predictions** - See forecasted fuel costs for better budgeting

## 🏗️ Architecture

```
petrol-analytics/
├── app.py              # Main application entry point
├── config.py           # Configuration and styling
├── data_loader.py      # Data processing and business logic
├── charts.py           # Professional visualization components
├── pages.py            # Dashboard page components
├── requirements.txt    # Python dependencies
├── Spend.xlsx         # Data source (Excel format) - provide your own
└── README.md          # Documentation
```

## 📋 Requirements

- Python 3.8+
- Streamlit 1.28+
- Pandas 2.0+
- Plotly 5.0+
- Scikit-learn 1.3+

## 🚀 Quick Start

### 1. Installation

```bash
# Clone the repository
git clone <repository-url>
cd petrol-analytics

# Install dependencies
pip install -r requirements.txt
```

### 2. Data Setup

Place your Excel file named `Spend.xlsx` in the project root with the following columns:
- `date` - Transaction date
- `station` - Fuel station name
- `price` - Total amount spent
- `litres` - Fuel volume purchased
- `liter_price` - Price per litre
- `attendant` - Service attendant (optional)
- `time` - Transaction time (optional)

### 3. Launch Dashboard

```bash
streamlit run app.py
```

The dashboard will be available at `http://localhost:8501`

## 📊 Dashboard Pages

### Personal Dashboard
- **Spending Summary** - Total spent, litres purchased, average price per litre, visit count
- **Spending Trends** - See how your fuel spending changes over time
- **Station Comparison** - Find out which stations you use most and their costs
- **Price Tracking** - Monitor fuel price changes at your regular stations
- **Consumption Patterns** - Understand your fuel usage habits

### Smart Insights
- **Spending Analysis** - Automated insights about your fuel habits
- **Future Predictions** - 30-day spending forecasts to help with budgeting
- **Efficiency Metrics** - Monthly averages and consumption patterns
- **Money-Saving Tips** - Recommendations to reduce fuel costs

### Data Management
- **Transaction History** - View all your fuel purchases in detail
- **Export Data** - Download your data as CSV or JSON files
- **Data Summary** - Quick overview of your fuel spending records

## 🎯 Personal Benefits

### Save Money
- **Find Cheaper Stations** - Identify which fuel stations offer the best value
- **Track Price Changes** - Monitor fuel price trends to time your fill-ups
- **Budget Planning** - Use spending predictions to plan your monthly fuel budget
- **Spending Awareness** - Understand exactly where your fuel money goes

### Understand Your Habits
- **Consumption Patterns** - See how much fuel you actually use
- **Visit Frequency** - Track how often you fill up and identify patterns
- **Seasonal Trends** - Discover if your fuel usage changes throughout the year
- **Station Preferences** - Learn which stations you visit most often

### Make Better Decisions
- **Data-Driven Choices** - Use real data instead of guesswork
- **Trend Analysis** - Spot patterns in your spending and consumption
- **Future Planning** - Predict upcoming fuel costs for better budgeting
- **Easy Tracking** - Simple interface makes monitoring your habits effortless

## 🔧 Technical Features

### Data Processing
- **Automated Cleaning** - Intelligent data preprocessing and validation
- **Error Handling** - Robust error management and user feedback
- **Performance Optimization** - Efficient data caching and processing
- **Scalability** - Designed to handle large datasets


### Analytics Engine
- **Predictive Modeling** - Linear regression for spending forecasts
- **Statistical Analysis** - Comprehensive KPI calculations
- **Trend Detection** - Automated pattern recognition
- **Business Intelligence** - Strategic insights generation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/enhancement`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to branch (`git push origin feature/enhancement`)
5. Create Pull Request


## 📞 Support

For technical support or business inquiries:
- Create an issue in the repository
- Contact Ofentse Menwe

---

**Petrol Spending Tracker** - Take control of your fuel spending with data-driven insights.

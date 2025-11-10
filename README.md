# ⛽ Petrol Analytics Dashboard

A professional business intelligence platform for fuel spending analysis, forecasting, and strategic insights.

## 🚀 Overview

The Petrol Analytics Dashboard is an enterprise-grade solution designed for investors, fleet managers, and business analysts to gain deep insights into fuel spending patterns, optimize costs, and make data-driven decisions.

### Key Features

- **📊 Executive Dashboard** - Real-time KPIs and performance metrics
- **🔍 Business Intelligence** - Advanced analytics and 30-day forecasting
- **📋 Data Management** - Comprehensive data export and management tools
- **🎯 Professional UI** - Investor-ready presentation with modern design
- **📈 Predictive Analytics** - Machine learning-powered spending forecasts

## 🏗️ Architecture

```
petrol-analytics/
├── app.py              # Main application entry point
├── config.py           # Configuration and styling
├── data_loader.py      # Data processing and business logic
├── charts.py           # Professional visualization components
├── pages.py            # Dashboard page components
├── requirements.txt    # Python dependencies
├── Spend.xlsx         # Data source (Excel format)
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

### Executive Dashboard
- **KPI Cards** - Total investment, fuel volume, average rates, transactions
- **Trend Analysis** - Smooth spending patterns over time
- **Station Performance** - Comparative analysis of service providers
- **Price Analytics** - Fuel price trends and volatility
- **Consumption Patterns** - Volume analysis and efficiency metrics

### Business Intelligence
- **Strategic Insights** - Automated business intelligence
- **Predictive Forecasting** - 30-day spending predictions using ML
- **Performance Metrics** - Monthly averages and efficiency indicators
- **Cost Optimization** - Recommendations for expense reduction

### Data Management
- **Dataset Overview** - Comprehensive data statistics
- **Detailed Records** - Formatted transaction history
- **Export Options** - CSV and JSON download capabilities
- **Data Quality** - Validation and completeness metrics

## 🎯 Business Value

### For Investors
- **ROI Analysis** - Clear visibility into fuel investment returns
- **Risk Assessment** - Price volatility and market exposure analysis
- **Growth Projections** - Data-driven forecasting for budget planning
- **Performance Benchmarking** - Comparative analysis across time periods

### For Fleet Managers
- **Cost Optimization** - Identify most cost-effective fuel stations
- **Consumption Monitoring** - Track fuel efficiency and usage patterns
- **Budget Planning** - Accurate forecasting for operational expenses
- **Vendor Analysis** - Performance comparison of fuel suppliers

### For Business Analysts
- **Advanced Analytics** - Machine learning-powered insights
- **Data Export** - Seamless integration with existing systems
- **Custom Filtering** - Flexible analysis by year, month, and station
- **Professional Reporting** - Investor-ready visualizations

## 🔧 Technical Features

### Data Processing
- **Automated Cleaning** - Intelligent data preprocessing and validation
- **Error Handling** - Robust error management and user feedback
- **Performance Optimization** - Efficient data caching and processing
- **Scalability** - Designed to handle large datasets

### Visualization
- **Interactive Charts** - Professional Plotly-based visualizations
- **Responsive Design** - Optimized for desktop and mobile viewing
- **Custom Styling** - Professional color schemes and branding
- **Export Ready** - High-quality charts suitable for presentations

### Analytics Engine
- **Predictive Modeling** - Linear regression for spending forecasts
- **Statistical Analysis** - Comprehensive KPI calculations
- **Trend Detection** - Automated pattern recognition
- **Business Intelligence** - Strategic insights generation

## 🎨 Customization

### Styling
Modify `config.py` to customize:
- Color schemes and branding
- Chart configurations
- Layout parameters
- Professional themes

### Analytics
Extend `data_loader.py` to add:
- Custom KPI calculations
- Advanced statistical models
- Additional data sources
- Business rule implementations

### Visualizations
Enhance `charts.py` with:
- New chart types
- Interactive features
- Custom styling options
- Export capabilities

## 📈 Performance

- **Fast Loading** - Optimized data caching with Streamlit
- **Responsive UI** - Smooth interactions and real-time updates
- **Scalable Architecture** - Modular design for easy maintenance
- **Professional Quality** - Enterprise-grade code standards

## 🔒 Security

- **Data Privacy** - Local data processing, no external transmission
- **Input Validation** - Robust error handling and data validation
- **Safe Operations** - No destructive operations on source data
- **Audit Trail** - Comprehensive logging and monitoring

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/enhancement`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to branch (`git push origin feature/enhancement`)
5. Create Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For technical support or business inquiries:
- Create an issue in the repository
- Contact the development team
- Review documentation and examples

---

**Petrol Analytics Dashboard** - Transforming fuel data into business intelligence.
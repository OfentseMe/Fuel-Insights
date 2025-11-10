import pandas as pd
import streamlit as st
from datetime import datetime, timedelta
import numpy as np
from sklearn.linear_model import LinearRegression

@st.cache_data
def load_petrol_data():
    """Load and preprocess petrol spending data from Excel file."""
    try:
        df = pd.read_excel('Spend.xlsx')
        df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
        
        if 'date' in df.columns:
            df['date'] = pd.to_datetime(df['date'], errors='coerce')
            df['year'] = df['date'].dt.year
            df['month_name'] = df['date'].dt.strftime('%B')
            df['month_num'] = df['date'].dt.month
            df['quarter'] = df['date'].dt.quarter
        
        # Calculate additional metrics
        if 'price' in df.columns and 'litres' in df.columns:
            df['cost_per_litre'] = df['price'] / df['litres']
        
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

def filter_data(df, year=None, month=None, station=None):
    """Apply filters to the dataset."""
    filtered_df = df.copy()
    
    if year and 'year' in df.columns:
        filtered_df = filtered_df[filtered_df['year'] == year]
    
    if month and month != 'All Months' and 'month_name' in df.columns:
        filtered_df = filtered_df[filtered_df['month_name'] == month]
    
    if station and station != 'All Stations' and 'station' in df.columns:
        filtered_df = filtered_df[filtered_df['station'] == station]
    
    return filtered_df

def calculate_kpis(df):
    """Calculate key performance indicators."""
    kpis = {}
    
    if not df.empty:
        kpis['total_spent'] = df['price'].sum() if 'price' in df.columns else 0
        kpis['total_litres'] = df['litres'].sum() if 'litres' in df.columns else 0
        kpis['avg_price_per_litre'] = df['liter_price'].mean() if 'liter_price' in df.columns else 0
        kpis['total_visits'] = len(df)
        kpis['avg_spend_per_visit'] = kpis['total_spent'] / kpis['total_visits'] if kpis['total_visits'] > 0 else 0
        
        # Monthly averages
        if 'date' in df.columns:
            months_span = (df['date'].max() - df['date'].min()).days / 30.44
            kpis['monthly_spend'] = kpis['total_spent'] / months_span if months_span > 0 else 0
            kpis['monthly_visits'] = kpis['total_visits'] / months_span if months_span > 0 else 0
    
    return kpis

def generate_predictions(df, days_ahead=30):
    """Generate spending predictions using linear regression."""
    if df.empty or 'date' not in df.columns or 'price' not in df.columns or len(df) < 3:
        return pd.DataFrame()
    
    try:
        df_pred = df.dropna(subset=['date', 'price']).copy().sort_values('date')
        if len(df_pred) < 3:
            return pd.DataFrame()
            
        df_pred['days_since_start'] = (df_pred['date'] - df_pred['date'].min()).dt.days
        
        X = df_pred[['days_since_start']].values
        y = df_pred['price'].values
        
        model = LinearRegression()
        model.fit(X, y)
        
        last_day = df_pred['days_since_start'].max()
        future_days = np.arange(last_day + 1, last_day + days_ahead + 1).reshape(-1, 1)
        future_prices = model.predict(future_days)
        
        future_dates = [df_pred['date'].max() + timedelta(days=i) for i in range(1, days_ahead + 1)]
        
        return pd.DataFrame({
            'date': future_dates,
            'predicted_price': np.maximum(future_prices, 0)
        })
    except Exception:
        return pd.DataFrame()

def get_insights(df):
    """Generate business insights from the data."""
    insights = []
    
    if df.empty:
        return insights
    
    # Station analysis
    if 'station' in df.columns and 'price' in df.columns:
        station_spending = df.groupby('station')['price'].sum().sort_values(ascending=False)
        top_station = station_spending.index[0]
        top_station_pct = (station_spending.iloc[0] / station_spending.sum()) * 100
        insights.append(f"🏆 Primary Station: {top_station} ({top_station_pct:.1f}% of total spend)")
    
    # Price trends
    if 'liter_price' in df.columns:
        avg_price = df['liter_price'].mean()
        price_volatility = df['liter_price'].std()
        insights.append(f"⛽ Average Fuel Price: R{avg_price:.2f}/L (±R{price_volatility:.2f})")
    
    # Consumption patterns
    if 'litres' in df.columns:
        avg_litres = df['litres'].mean()
        total_litres = df['litres'].sum()
        insights.append(f"📊 Consumption: {total_litres:.0f}L total, {avg_litres:.1f}L average per visit")
    
    # Frequency analysis
    if 'date' in df.columns and len(df) > 1:
        date_range = (df['date'].max() - df['date'].min()).days
        frequency = len(df) / (date_range / 7) if date_range > 0 else 0
        insights.append(f"📅 Visit Frequency: {frequency:.1f} times per week")
    
    return insights
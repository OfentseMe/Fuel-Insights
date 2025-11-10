import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from datetime import datetime, timedelta
import numpy as np
from sklearn.linear_model import LinearRegression

# Custom CSS
def load_css():
    st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(90deg, #FF6B6B, #4ECDC4);
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
        text-align: center;
    }
    .metric-title {
        color: white;
        font-size: 14px;
        margin-bottom: 10px;
        opacity: 0.9;
    }
    .metric-value {
        color: white;
        font-size: 28px;
        font-weight: bold;
        margin: 0;
    }
    .insight-box {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        color: white;
    }
    .tab-container {
        display: flex;
        justify-content: flex-end;
        margin-bottom: 2rem;
    }
    .tab-button {
        background: #f0f2f6;
        border: none;
        padding: 10px 20px;
        margin: 0 5px;
        border-radius: 20px;
        cursor: pointer;
        transition: all 0.3s;
    }
    .tab-button.active {
        background: linear-gradient(90deg, #FF6B6B, #4ECDC4);
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

@st.cache_data
def load_data():
    try:
        df = pd.read_excel('Spend.xlsx')
        df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
        
        if 'date' in df.columns:
            df['date'] = pd.to_datetime(df['date'], errors='coerce')
            df['year'] = df['date'].dt.year
            df['month_name'] = df['date'].dt.strftime('%B')
            df['month_num'] = df['date'].dt.month
        
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

def create_predictions(df):
    if 'date' in df.columns and 'price' in df.columns and len(df) > 5:
        df_pred = df.copy()
        df_pred['days'] = (df_pred['date'] - df_pred['date'].min()).dt.days
        
        X = df_pred[['days']].values
        y = df_pred['price'].values
        
        model = LinearRegression()
        model.fit(X, y)
        
        future_days = np.arange(df_pred['days'].max() + 1, df_pred['days'].max() + 31).reshape(-1, 1)
        future_prices = model.predict(future_days)
        
        future_dates = [df['date'].max() + timedelta(days=i) for i in range(1, 31)]
        
        return pd.DataFrame({
            'date': future_dates,
            'predicted_price': future_prices
        })
    return pd.DataFrame()

def dashboard_page(df_filtered):
    # KPIs
    st.markdown("### 📊 Key Performance Indicators")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_spent = df_filtered['price'].sum() if 'price' in df_filtered.columns else 0
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">💰 Total Spent</div>
            <div class="metric-value">R{total_spent:,.0f}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        total_litres = df_filtered['litres'].sum() if 'litres' in df_filtered.columns else 0
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">⛽ Total Litres</div>
            <div class="metric-value">{total_litres:,.0f}L</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        avg_price_per_litre = df_filtered['liter_price'].mean() if 'liter_price' in df_filtered.columns else 0
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">📊 Avg Price/L</div>
            <div class="metric-value">R{avg_price_per_litre:.2f}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        total_visits = len(df_filtered)
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">🚗 Total Visits</div>
            <div class="metric-value">{total_visits}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        if 'date' in df_filtered.columns and 'price' in df_filtered.columns:
            fig_time = go.Figure()
            fig_time.add_trace(go.Scatter(
                x=df_filtered['date'], 
                y=df_filtered['price'],
                mode='lines',
                line=dict(color='#FF6B6B', width=3, shape='spline', smoothing=1.3),
                name='Spending'
            ))
            fig_time.update_layout(
                title="💸 Spending Over Time",
                showlegend=False,
                height=400,
                xaxis_title="Date",
                yaxis_title="Amount (R)"
            )
            st.plotly_chart(fig_time, use_container_width=True)
    
    with col2:
        if 'station' in df_filtered.columns and 'price' in df_filtered.columns:
            station_spending = df_filtered.groupby('station')['price'].sum().sort_values(ascending=False)
            fig_station = px.bar(x=station_spending.index, y=station_spending.values, 
                               title="🏪 Spending by Station", color=station_spending.values)
            fig_station.update_layout(showlegend=False, height=400)
            st.plotly_chart(fig_station, use_container_width=True)
    
    col3, col4 = st.columns(2)
    
    with col3:
        if 'date' in df_filtered.columns and 'liter_price' in df_filtered.columns:
            fig_price = px.scatter(df_filtered, x='date', y='liter_price', 
                                 title="📈 Price per Litre Trends", color='station')
            fig_price.update_layout(showlegend=False, height=400)
            st.plotly_chart(fig_price, use_container_width=True)
    
    with col4:
        if 'date' in df_filtered.columns and 'litres' in df_filtered.columns:
            fig_litres = px.bar(df_filtered, x='date', y='litres', 
                              title="⛽ Fuel Consumption", color='litres')
            fig_litres.update_layout(showlegend=False, height=400)
            st.plotly_chart(fig_litres, use_container_width=True)

def insights_page(df_filtered):
    st.markdown("### 🔍 Key Insights & Predictions")
    
    # Insights
    insights = []
    
    if 'station' in df_filtered.columns and 'price' in df_filtered.columns:
        favorite_station = df_filtered.groupby('station')['price'].sum().idxmax()
        insights.append(f"🏆 **Favorite Station**: {favorite_station}")
    
    if 'liter_price' in df_filtered.columns:
        avg_price = df_filtered['liter_price'].mean()
        max_price = df_filtered['liter_price'].max()
        min_price = df_filtered['liter_price'].min()
        insights.append(f"💰 **Price Range**: R{min_price:.2f} - R{max_price:.2f} per litre")
    
    if 'date' in df_filtered.columns:
        days_tracked = (df_filtered['date'].max() - df_filtered['date'].min()).days
        avg_visits_per_month = len(df_filtered) / (days_tracked / 30) if days_tracked > 0 else 0
        insights.append(f"📅 **Visit Frequency**: {avg_visits_per_month:.1f} visits per month")
    
    if 'litres' in df_filtered.columns:
        avg_litres = df_filtered['litres'].mean()
        insights.append(f"⛽ **Average Fill**: {avg_litres:.1f} litres per visit")
    
    for insight in insights:
        st.markdown(f"""
        <div class="insight-box">
            {insight}
        </div>
        """, unsafe_allow_html=True)
    
    # Predictions
    st.markdown("### 🔮 Spending Predictions")
    predictions = create_predictions(df_filtered)
    
    if not predictions.empty:
        fig_pred = go.Figure()
        fig_pred.add_trace(go.Scatter(
            x=predictions['date'], 
            y=predictions['predicted_price'],
            mode='lines',
            line=dict(color='#4ECDC4', width=3, shape='spline', smoothing=1.3),
            name='Predicted'
        ))
        fig_pred.update_layout(
            title="📊 Predicted Spending (Next 30 Days)",
            showlegend=False,
            xaxis_title="Date",
            yaxis_title="Predicted Amount (R)"
        )
        st.plotly_chart(fig_pred, use_container_width=True)
        
        total_predicted = predictions['predicted_price'].sum()
        st.markdown(f"""
        <div class="insight-box">
            🎯 **Predicted Monthly Spending**: R{total_predicted:,.0f}
        </div>
        """, unsafe_allow_html=True)

def raw_data_page(df_filtered):
    st.markdown("### 📋 Raw Data")
    
    # Format data for display
    display_df = df_filtered.copy()
    if 'price' in display_df.columns:
        display_df['price'] = display_df['price'].apply(lambda x: f"R{x:.2f}")
    if 'liter_price' in display_df.columns:
        display_df['liter_price'] = display_df['liter_price'].apply(lambda x: f"R{x:.2f}")
    if 'litres' in display_df.columns:
        display_df['litres'] = display_df['litres'].apply(lambda x: f"{x:.1f}L")
    
    st.dataframe(display_df, use_container_width=True, height=600)
    
    # Download button
    csv = df_filtered.to_csv(index=False)
    st.download_button(
        label="📥 Download CSV",
        data=csv,
        file_name="petrol_data.csv",
        mime="text/csv"
    )

def main():
    st.set_page_config(page_title="⛽ Petrol Dashboard", layout="wide")
    load_css()
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>⛽ Petrol Spending Analytics</h1>
        <p>Discover insights from your fuel spending data</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load data
    df = load_data()
    if df.empty:
        st.error("No data found. Please check your Excel file.")
        return
    
    # Page Navigation (Top Right)
    col1, col2 = st.columns([3, 1])
    with col2:
        page = st.selectbox("", ["📊 Dashboard", "🔍 Insights", "📋 Raw Data"], label_visibility="collapsed")
    
    # Sidebar Filters
    st.sidebar.header("🔧 Filters")
    
    # Year Filter
    if 'year' in df.columns:
        years = st.sidebar.selectbox(
            "📅 Select Year",
            options=sorted(df['year'].unique())
        )
        df_year = df[df['year'] == years]
    else:
        df_year = df
    
    # Month Filter
    if 'month_name' in df_year.columns:
        available_months = df_year.sort_values('month_num')['month_name'].unique()
        selected_month = st.sidebar.selectbox(
            "📆 Select Month",
            options=['All Months'] + list(available_months)
        )
        
        if selected_month != 'All Months':
            df_filtered = df_year[df_year['month_name'] == selected_month]
        else:
            df_filtered = df_year
    else:
        df_filtered = df_year
    
    # Station Filter
    if 'station' in df.columns:
        stations = st.sidebar.selectbox(
            "🏪 Select Station",
            options=['All Stations'] + list(df['station'].unique())
        )
        
        if stations != 'All Stations':
            df_filtered = df_filtered[df_filtered['station'] == stations]
    
    # Display selected page
    if page == "📊 Dashboard":
        dashboard_page(df_filtered)
    elif page == "🔍 Insights":
        insights_page(df_filtered)
    elif page == "📋 Raw Data":
        raw_data_page(df_filtered)

if __name__ == "__main__":
    main()
import streamlit as st
from data_loader import calculate_kpis, generate_predictions, get_insights
from charts import *

def render_kpi_cards(kpis):
    """Render KPI cards with professional styling."""
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">💰 Total Investment</div>
            <div class="metric-value">R{kpis.get('total_spent', 0):,.0f}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">⛽ Fuel Volume</div>
            <div class="metric-value">{kpis.get('total_litres', 0):,.0f}L</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">📊 Average Rate</div>
            <div class="metric-value">R{kpis.get('avg_price_per_litre', 0):.2f}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">🚗 Transactions</div>
            <div class="metric-value">{kpis.get('total_visits', 0)}</div>
        </div>
        """, unsafe_allow_html=True)

def dashboard_page(df_filtered):
    """Main dashboard page with executive summary."""
    st.markdown("## 📊 Executive Dashboard")
    
    # Calculate and display KPIs
    kpis = calculate_kpis(df_filtered)
    render_kpi_cards(kpis)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Main charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        fig_trend = create_spending_trend_chart(df_filtered)
        st.plotly_chart(fig_trend, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        fig_station = create_station_comparison_chart(df_filtered)
        st.plotly_chart(fig_station, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Secondary charts
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        fig_price = create_price_analysis_chart(df_filtered)
        st.plotly_chart(fig_price, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col4:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        fig_consumption = create_consumption_chart(df_filtered)
        st.plotly_chart(fig_consumption, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Monthly overview
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    fig_monthly = create_monthly_summary_chart(df_filtered)
    st.plotly_chart(fig_monthly, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

def analytics_page(df_filtered):
    """Advanced analytics and predictions page."""
    st.markdown("## 🔍 Business Intelligence & Forecasting")
    
    # Key insights
    insights = get_insights(df_filtered)
    
    if insights:
        st.markdown("### 💡 Strategic Insights")
        for insight in insights:
            st.markdown(f"""
            <div class="insight-card">
                {insight}
            </div>
            """, unsafe_allow_html=True)
    
    # Predictions section
    st.markdown("### 🔮 Predictive Analytics")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        predictions = generate_predictions(df_filtered)
        predictions = generate_predictions(df_filtered)
        if not predictions.empty:
            st.markdown('<div class="chart-container">', unsafe_allow_html=True)
            fig_pred = create_prediction_chart(predictions)
            st.plotly_chart(fig_pred, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.info("Insufficient data for reliable predictions. Need at least 3 data points.")
    
    with col2:
        if not predictions.empty:
            total_predicted = predictions['predicted_price'].sum()
            avg_predicted = predictions['predicted_price'].mean()
            
            st.markdown(f"""
            <div class="insight-card">
                <h4>📈 30-Day Forecast</h4>
                <p><strong>Total Expected:</strong> R{total_predicted:,.0f}</p>
                <p><strong>Daily Average:</strong> R{avg_predicted:.0f}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Performance metrics
    kpis = calculate_kpis(df_filtered)
    if kpis.get('monthly_spend', 0) > 0:
        st.markdown("### 📊 Performance Metrics")
        
        col3, col4 = st.columns(2)
        
        with col3:
            st.markdown(f"""
            <div class="insight-card">
                <h4>💰 Monthly Averages</h4>
                <p><strong>Spending:</strong> R{kpis.get('monthly_spend', 0):,.0f}</p>
                <p><strong>Visits:</strong> {kpis.get('monthly_visits', 0):.1f}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown(f"""
            <div class="insight-card">
                <h4>🎯 Efficiency Metrics</h4>
                <p><strong>Cost per Visit:</strong> R{kpis.get('avg_spend_per_visit', 0):.0f}</p>
                <p><strong>Volume per Visit:</strong> {kpis.get('total_litres', 0) / kpis.get('total_visits', 1):.1f}L</p>
            </div>
            """, unsafe_allow_html=True)

def data_page(df_filtered):
    """Data export and detailed view page."""
    st.markdown("## 📋 Data Management")
    
    if df_filtered.empty:
        st.warning("⚠️ No data available with current filters.")
        return
    
    # Data summary
    st.markdown("### 📊 Dataset Overview")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Records", len(df_filtered))
    
    with col2:
        date_range = "N/A"
        if 'date' in df_filtered.columns:
            start_date = df_filtered['date'].min().strftime('%Y-%m-%d')
            end_date = df_filtered['date'].max().strftime('%Y-%m-%d')
            date_range = f"{start_date} to {end_date}"
        st.metric("Date Range", date_range)
    
    with col3:
        stations = df_filtered['station'].nunique() if 'station' in df_filtered.columns else 0
        st.metric("Unique Stations", stations)
    
    # Data table
    st.markdown("### 📄 Detailed Records")
    
    # Show raw data without formatting for better display
    st.dataframe(df_filtered, use_container_width=True, height=500)
    
    # Export options
    st.markdown("### 📥 Export Options")
    
    col1, col2 = st.columns(2)
    
    with col1:
        csv = df_filtered.to_csv(index=False)
        st.download_button(
            label="📊 Download CSV",
            data=csv,
            file_name=f"petrol_data_{df_filtered['date'].min().strftime('%Y%m%d') if 'date' in df_filtered.columns else 'export'}.csv",
            mime="text/csv"
        )
    
    with col2:
        json_data = df_filtered.to_json(orient='records', date_format='iso')
        st.download_button(
            label="📋 Download JSON",
            data=json_data,
            file_name=f"petrol_data_{df_filtered['date'].min().strftime('%Y%m%d') if 'date' in df_filtered.columns else 'export'}.json",
            mime="application/json"
        )
"""
Petrol Analytics Dashboard
Professional fuel spending analysis and forecasting platform
"""

import streamlit as st
from config import CSS_STYLES
from data_loader import load_petrol_data, filter_data
from pages import dashboard_page, analytics_page, data_page

def main():
    """Main application entry point."""
    # Page configuration
    st.set_page_config(
        page_title="Petrol Analytics Dashboard",
        page_icon="⛽",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Load custom CSS
    st.markdown(CSS_STYLES, unsafe_allow_html=True)
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>⛽ Petrol Analytics Dashboard</h1>
        <p>Professional Fuel Spending Analysis & Business Intelligence Platform</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load data
    df = load_petrol_data()
    
    if df.empty:
        st.error("❌ No data available. Please ensure 'Spend.xlsx' is in the application directory.")
        st.info("📁 Expected file format: Excel file with columns for date, station, price, litres, etc.")
        return
    
    # Navigation
    col1, col2 = st.columns([4, 1])
    with col2:
        st.markdown('<div class="page-nav">', unsafe_allow_html=True)
        page = st.selectbox(
            "",
            ["📊 Executive Dashboard", "🔍 Business Intelligence", "📋 Data Management"],
            label_visibility="collapsed"
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Sidebar filters
    with st.sidebar:
        st.markdown('<div class="filter-section">', unsafe_allow_html=True)
        st.header("🎛️ Analytics Filters")
        
        # Year filter
        if 'year' in df.columns:
            years = sorted(df['year'].unique(), reverse=True)
            selected_year = st.selectbox("📅 Financial Year", years)
            df_year = df[df['year'] == selected_year]
        else:
            df_year = df
            selected_year = None
        
        # Month filter
        if 'month_name' in df_year.columns:
            available_months = df_year.sort_values('month_num')['month_name'].unique()
            selected_month = st.selectbox(
                "📆 Reporting Period",
                ['All Months'] + list(available_months)
            )
        else:
            selected_month = 'All Months'
        
        # Station filter
        if 'station' in df.columns:
            stations = ['All Stations'] + sorted(df['station'].unique())
            selected_station = st.selectbox("🏪 Service Provider", stations)
        else:
            selected_station = 'All Stations'
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Data summary in sidebar
        st.markdown("### 📈 Quick Stats")
        filtered_preview = filter_data(df, selected_year, selected_month, selected_station)
        
        if not filtered_preview.empty:
            total_records = len(filtered_preview)
            total_spend = filtered_preview['price'].sum() if 'price' in filtered_preview.columns else 0
            
            st.metric("Records", f"{total_records:,}")
            st.metric("Total Value", f"R{total_spend:,.0f}")
            
            if 'date' in filtered_preview.columns:
                date_range = (filtered_preview['date'].max() - filtered_preview['date'].min()).days
                st.metric("Period (Days)", date_range)
    
    # Apply filters
    df_filtered = filter_data(df, selected_year, selected_month, selected_station)
    
    # Render selected page
    if page == "📊 Executive Dashboard":
        dashboard_page(df_filtered)
    elif page == "🔍 Business Intelligence":
        analytics_page(df_filtered)
    elif page == "📋 Data Management":
        data_page(df_filtered)
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: #6C757D; padding: 1rem;'>"
        "Petrol Analytics Dashboard | Professional Business Intelligence Platform"
        "</div>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
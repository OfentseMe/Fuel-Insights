import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from config import COLORS, CHART_CONFIG

def create_spending_trend_chart(df):
    """Create smooth spending trend line chart."""
    if df.empty or 'date' not in df.columns or 'price' not in df.columns:
        return go.Figure()
    
    df_sorted = df.sort_values('date')
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df_sorted['date'],
        y=df_sorted['price'],
        mode='lines+markers',
        line=dict(
            color=COLORS['primary'],
            width=CHART_CONFIG['line_style']['width'],
            shape=CHART_CONFIG['line_style']['shape'],
            smoothing=CHART_CONFIG['line_style']['smoothing']
        ),
        marker=dict(size=8, color=COLORS['primary']),
        name='Spending',
        hovertemplate='<b>%{x}</b><br>Amount: R%{y:.2f}<extra></extra>'
    ))
    
    fig.update_layout(
        title=dict(text="💸 Spending Trend Analysis", font=dict(size=20, color=COLORS['text'])),
        **CHART_CONFIG['layout'],
        xaxis_title="Date",
        yaxis_title="Amount (R)",
        showlegend=False
    )
    
    return fig

def create_station_comparison_chart(df):
    """Create station spending comparison chart."""
    if 'station' not in df.columns or 'price' not in df.columns:
        return go.Figure()
    
    station_data = df.groupby('station')['price'].sum().sort_values(ascending=True)
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=station_data.values,
        y=station_data.index,
        orientation='h',
        marker=dict(
            color=station_data.values,
            colorscale='Blues',
            showscale=False
        ),
        hovertemplate='<b>%{y}</b><br>Total: R%{x:,.2f}<extra></extra>'
    ))
    
    fig.update_layout(
        title=dict(text="🏪 Station Performance Comparison", font=dict(size=20, color=COLORS['text'])),
        **CHART_CONFIG['layout'],
        xaxis_title="Total Spending (R)",
        yaxis_title="Station",
        showlegend=False
    )
    
    return fig

def create_price_analysis_chart(df):
    """Create fuel price analysis chart."""
    if 'date' not in df.columns or 'liter_price' not in df.columns:
        return go.Figure()
    
    fig = go.Figure()
    
    # Add price trend line
    fig.add_trace(go.Scatter(
        x=df['date'],
        y=df['liter_price'],
        mode='lines+markers',
        line=dict(color=COLORS['accent'], width=3),
        marker=dict(size=6, color=COLORS['accent']),
        name='Price per Litre',
        hovertemplate='<b>%{x}</b><br>Price: R%{y:.2f}/L<extra></extra>'
    ))
    
    # Add average line
    avg_price = df['liter_price'].mean()
    fig.add_hline(
        y=avg_price,
        line_dash="dash",
        line_color=COLORS['secondary'],
        annotation_text=f"Average: R{avg_price:.2f}/L"
    )
    
    fig.update_layout(
        title=dict(text="📈 Fuel Price Analysis", font=dict(size=20, color=COLORS['text'])),
        **CHART_CONFIG['layout'],
        xaxis_title="Date",
        yaxis_title="Price per Litre (R)",
        showlegend=False
    )
    
    return fig

def create_consumption_chart(df):
    """Create fuel consumption chart."""
    if 'date' not in df.columns or 'litres' not in df.columns:
        return go.Figure()
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=df['date'],
        y=df['litres'],
        marker=dict(
            color=df['litres'],
            colorscale='Viridis',
            showscale=False
        ),
        hovertemplate='<b>%{x}</b><br>Litres: %{y:.1f}L<extra></extra>'
    ))
    
    fig.update_layout(
        title=dict(text="⛽ Fuel Consumption Pattern", font=dict(size=20, color=COLORS['text'])),
        **CHART_CONFIG['layout'],
        xaxis_title="Date",
        yaxis_title="Litres",
        showlegend=False
    )
    
    return fig

def create_prediction_chart(predictions_df):
    """Create spending predictions chart."""
    if predictions_df.empty:
        return go.Figure()
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=predictions_df['date'],
        y=predictions_df['predicted_price'],
        mode='lines+markers',
        line=dict(
            color=COLORS['success'],
            width=CHART_CONFIG['line_style']['width'],
            shape=CHART_CONFIG['line_style']['shape'],
            smoothing=CHART_CONFIG['line_style']['smoothing']
        ),
        marker=dict(size=8, color=COLORS['success']),
        name='Predicted Spending',
        hovertemplate='<b>%{x}</b><br>Predicted: R%{y:.2f}<extra></extra>'
    ))
    
    fig.update_layout(
        title=dict(text="🔮 30-Day Spending Forecast", font=dict(size=20, color=COLORS['text'])),
        **CHART_CONFIG['layout'],
        xaxis_title="Date",
        yaxis_title="Predicted Amount (R)",
        showlegend=False
    )
    
    return fig

def create_monthly_summary_chart(df):
    """Create monthly spending summary chart."""
    if 'month_name' not in df.columns or 'price' not in df.columns:
        return go.Figure()
    
    monthly_data = df.groupby(['month_num', 'month_name'])['price'].sum().reset_index()
    monthly_data = monthly_data.sort_values('month_num')
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=monthly_data['month_name'],
        y=monthly_data['price'],
        marker=dict(
            color=monthly_data['price'],
            colorscale='Plasma',
            showscale=False
        ),
        hovertemplate='<b>%{x}</b><br>Total: R%{y:,.2f}<extra></extra>'
    ))
    
    fig.update_layout(
        title=dict(text="📊 Monthly Spending Overview", font=dict(size=20, color=COLORS['text'])),
        **CHART_CONFIG['layout'],
        xaxis_title="Month",
        yaxis_title="Total Spending (R)",
        showlegend=False
    )
    
    return fig
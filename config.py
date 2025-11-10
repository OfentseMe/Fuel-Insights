# Configuration and styling for the Petrol Analytics Dashboard

COLORS = {
    'primary': '#2E86AB',
    'secondary': '#A23B72', 
    'accent': '#F18F01',
    'success': '#C73E1D',
    'background': '#F8F9FA',
    'text': '#2C3E50'
}

CSS_STYLES = """
<style>
.main-header {
    background: linear-gradient(135deg, #2E86AB 0%, #A23B72 100%);
    padding: 3rem 2rem;
    border-radius: 15px;
    text-align: center;
    color: white;
    margin-bottom: 2rem;
    box-shadow: 0 8px 32px rgba(0,0,0,0.1);
}

.metric-card {
    background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
    padding: 2rem;
    border-radius: 15px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    border-left: 5px solid #2E86AB;
    margin-bottom: 1rem;
    text-align: center;
    transition: transform 0.3s ease;
}

.metric-card:hover {
    transform: translateY(-5px);
}

.metric-title {
    color: #6C757D;
    font-size: 14px;
    font-weight: 600;
    margin-bottom: 10px;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.metric-value {
    color: #2E86AB;
    font-size: 32px;
    font-weight: 700;
    margin: 0;
}

.insight-card {
    background: linear-gradient(135deg, #2E86AB 0%, #A23B72 100%);
    padding: 1.5rem;
    border-radius: 12px;
    margin: 1rem 0;
    color: white;
    box-shadow: 0 4px 15px rgba(46, 134, 171, 0.3);
}

.page-nav {
    background: white;
    padding: 1rem;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    margin-bottom: 2rem;
}

.filter-section {
    background: white;
    padding: 1.5rem;
    border-radius: 12px;
    box-shadow: 0 2px 15px rgba(0,0,0,0.05);
    margin-bottom: 1rem;
}

.chart-container {
    background: white;
    padding: 1.5rem;
    border-radius: 12px;
    box-shadow: 0 2px 15px rgba(0,0,0,0.05);
    margin-bottom: 1rem;
}

.stSelectbox > div > div {
    background-color: white;
    border: 2px solid #E9ECEF;
    border-radius: 8px;
}

.stSelectbox > div > div:focus-within {
    border-color: #2E86AB;
    box-shadow: 0 0 0 3px rgba(46, 134, 171, 0.1);
}
</style>
"""

CHART_CONFIG = {
    'layout': {
        'plot_bgcolor': 'rgba(0,0,0,0)',
        'paper_bgcolor': 'rgba(0,0,0,0)',
        'font': {'family': 'Arial, sans-serif', 'color': '#2C3E50'},
        'margin': {'l': 40, 'r': 40, 't': 60, 'b': 40}
    },
    'line_style': {
        'width': 4,
        'shape': 'spline',
        'smoothing': 1.3
    }
}
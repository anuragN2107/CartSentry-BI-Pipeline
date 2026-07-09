import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
from src.transform import calculate_metrics

# Set up the webpage configuration
st.set_page_config(page_title="CartSentry BI Dashboard", layout="wide")

st.title("🛒 CartSentry E-Commerce Performance Dashboard")
st.markdown("This dashboard reflects live metrics processed by your automated data pipeline.")

# 1. Load the cleaned data
CLEAN_DATA_PATH = "data/clean_transactions.csv"

if not os.path.exists(CLEAN_DATA_PATH):
    st.error(f"❌ Cleaned data file not found at {CLEAN_DATA_PATH}. Please run your pipeline files first!")
else:
    df = pd.read_csv(CLEAN_DATA_PATH)
    
    # 2. Calculate the metrics using our existing engine
    metrics = calculate_metrics(df)
    
    # 3. Create Top Row Metric Cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="Hourly Revenue", 
            value=f"${metrics['total_revenue']:,.2f}",
            delta="Live Feed"
        )
        
    with col2:
        st.metric(
            label="Conversion Rate", 
            value=f"{metrics['conversion_rate']:.2f}%",
            delta="Target: > 50%"
        )
        
    with col3:
        st.metric(
            label="Cart Abandonment Rate", 
            value=f"{metrics['abandonment_rate']:.2f}%",
            delta="Keep Low",
            delta_color="inverse"
        )
        
    st.markdown("---")
    
    # 4. Create Visual Charts
    st.subheader("📊 Transaction Breakdown Over Time")
    
    # Prepare data for a quick line chart of revenue accumulation
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df_sorted = df.sort_values('timestamp')
    df_sorted['Cumulative Revenue'] = df_sorted['revenue'].cumsum()
    
    # Create two columns for charts
    chart_col1, chart_col2 = st.columns(2)
    
    with chart_col1:
        st.write("### Cumulative Revenue Growth")
        st.line_chart(df_sorted.set_index('timestamp')['Cumulative Revenue'])
        
    with chart_col2:
        st.write("### Transaction Status Counts")
        status_counts = df['status'].value_counts()
        st.bar_chart(status_counts)

    # 5. Show Raw Data Table at the bottom
    st.subheader("📋 Cleaned Transaction Logs")
    st.dataframe(df, width="stretch")
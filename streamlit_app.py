import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

def load_cyber_data():
    # Simulated data - replace with your actual data loading
    data = {
        'id': range(1, 11),
        'text': ['Suspicious login attempt detected', 'Malware signature identified', 
                'DDoS attack pattern observed', 'Phishing email detected',
                'Unauthorized access attempt', 'SQL injection attempt',
                'Ransomware activity detected', 'Data exfiltration attempt',
                'Brute force attack detected', 'Zero-day exploit attempt'],
        'label': ['Attack Pattern', 'Malware', 'DDoS', 'Phishing',
                 'Unauthorized Access', 'SQL Injection', 'Ransomware',
                 'Data Theft', 'Brute Force', 'Zero-day'],
        'severity': ['High', 'Critical', 'Medium', 'High',
                    'Critical', 'High', 'Critical', 'High',
                    'Medium', 'Critical'],
        'timestamp': [datetime.now() - timedelta(hours=x) for x in range(10)]
    }
    return pd.DataFrame(data)

def generate_threat_metrics():
    return {
        'total_threats': np.random.randint(100, 1000),
        'critical_threats': np.random.randint(10, 50),
        'resolved_threats': np.random.randint(50, 200),
        'active_threats': np.random.randint(20, 100)
    }

def main():
    st.set_page_config(layout="wide", page_title="Cyber Threat Analysis Dashboard")
    
    # Header
    st.title("🛡️ Cyber Threat Analysis Dashboard")
    
    # Load data
    df = load_cyber_data()
    metrics = generate_threat_metrics()
    
    # Metrics Row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Threats", metrics['total_threats'])
    with col2:
        st.metric("Critical Threats", metrics['critical_threats'], delta="↑")
    with col3:
        st.metric("Resolved", metrics['resolved_threats'])
    with col4:
        st.metric("Active Threats", metrics['active_threats'], delta="↓")
    
    # Main content
    st.markdown("---")
    
    # Two columns layout
    left_col, right_col = st.columns([2, 1])
    
    with left_col:
        st.subheader("Recent Threats")
        # Create a styled dataframe
        styled_df = df[['timestamp', 'label', 'severity', 'text']].copy()
        styled_df['timestamp'] = styled_df['timestamp'].dt.strftime('%Y-%m-%d %H:%M')
        st.dataframe(styled_df, use_container_width=True)
        
        # Threat Distribution
        st.subheader("Threat Distribution by Type")
        fig = px.pie(df, names='label', title='Distribution of Threat Types')
        st.plotly_chart(fig, use_container_width=True)
    
    with right_col:
        st.subheader("Severity Distribution")
        severity_counts = df['severity'].value_counts()
        fig = px.bar(x=severity_counts.index, y=severity_counts.values,
                    color=severity_counts.index,
                    title="Threats by Severity Level")
        st.plotly_chart(fig, use_container_width=True)
        
        # Time-based analysis
        st.subheader("Threat Timeline")
        timeline_data = df.groupby('timestamp').size().reset_index(name='count')
        fig = px.line(timeline_data, x='timestamp', y='count',
                     title="Threats Over Time")
        st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()

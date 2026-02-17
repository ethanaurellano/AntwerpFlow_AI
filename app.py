import streamlit as st
import pandas as pd
import time

# IMPORT YOUR OWN MODULES (This is the "Pro" move)
import data_loader as dl
import logistics_engine as engine

# --- PAGE CONFIG ---
st.set_page_config(page_title="AntwerpFlow Enterprise", layout="wide")
st.title("🚢 AntwerpFlow Enterprise Edition")
st.markdown("### Port of Antwerp-Bruges | Automated Congestion Manager")

# --- SIDEBAR CONTROLS ---
st.sidebar.header("Control Tower")
if st.sidebar.button("🔄 Refresh Live Data"):
    st.cache_data.clear() # Simulate clearing cache for new data

# --- 1. GET DATA (Using your backend file) ---
with st.spinner('Connecting to NxtPort Gateway...'):
    time.sleep(0.8) # Fake network delay for realism
    raw_data = dl.fetch_port_data()
    clean_data = dl.clean_data(raw_data)

# --- 2. ANALYZE DATA (Using your brain file) ---
# Let user pick a terminal
selected_terminal = st.selectbox("Select Terminal Zone:", clean_data['terminal'].unique())

# Filter data for that terminal
terminal_data = clean_data[clean_data['terminal'] == selected_terminal]
total_cargo = terminal_data['containers'].sum()

# Ask the 'Brain' for the status
status, color = engine.calculate_congestion_level(total_cargo)
action = engine.get_action_recommendation(status, selected_terminal)

# --- 3. SHOW DASHBOARD ---
# KPI Row
col1, col2, col3 = st.columns(3)
col1.metric("Active Vessels", len(terminal_data))
col2.metric("Total Containers", f"{total_cargo:,}")
col3.metric("Congestion Status", status, delta_color="inverse")

# Action Banner
if status == "CRITICAL":
    st.error(f"**AI RECOMMENDATION:** {action}")
elif status == "WARNING":
    st.warning(f"**AI RECOMMENDATION:** {action}")
else:
    st.success(f"**AI RECOMMENDATION:** {action}")

# Detailed Table
st.dataframe(terminal_data, use_container_width=True)
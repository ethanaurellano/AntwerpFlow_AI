import streamlit as st
import pandas as pd
import time
import altair as alt  # For beautiful charts

# IMPORT YOUR MODULES
import data_loader as dl
import logistics_engine as engine

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="AntwerpFlow AI", layout="wide")
st.title("🚢 AntwerpFlow: AI Terminal Planner")
st.markdown("### Port of Antwerp-Bruges | Intelligent Congestion Manager")

# --- 2. SIDEBAR (CONTROLS) ---
st.sidebar.header("🎛️ Control Tower")

# A. Reload Button
if st.sidebar.button("🔄 Refresh Live Data"):
    st.cache_data.clear()

# B. THE NEW SCENARIO SLIDER (Your "What-If" Feature)
st.sidebar.markdown("---")
st.sidebar.subheader("🛠 Scenario Planner")
extra_containers = st.sidebar.slider(
    "Simulate Sudden Surge (TEU)",
    min_value=0,
    max_value=5000,
    step=100,
    help="Drag to simulate a massive ship arriving unexpectedly."
)

if extra_containers > 0:
    st.sidebar.warning(f"⚠️ SIMULATION ACTIVE: +{extra_containers} TEU added")

# --- 3. LOAD DATA (BACKEND) ---
# We fetch the data using your data_loader.py file
raw_data = dl.fetch_port_data()
clean_data = dl.clean_data(raw_data)

# --- 4. MAIN DASHBOARD LOGIC ---

# Step A: Filter by Terminal
selected_terminal = st.selectbox("Select Terminal Zone:", clean_data['terminal'].unique())
terminal_data = clean_data[clean_data['terminal'] == selected_terminal]

# Step B: Calculate Real + Simulated Load
real_cargo = terminal_data['containers'].sum()
total_cargo = real_cargo + extra_containers  # The math happens here!

# Step C: Get AI Decision (Using the updated engine logic)
# Note: Ensure your logistics_engine.py has the updated function!
status, color, load_pct = engine.calculate_congestion_level(total_cargo)
action = engine.get_action_recommendation(status, selected_terminal)

# --- 5. VISUALIZATION (THE "UI") ---

# Row 1: KPI Cards
col1, col2, col3, col4 = st.columns(4)
col1.metric("Active Vessels", len(terminal_data))
col2.metric("Real Cargo Load", f"{real_cargo:,} TEU")
col3.metric("Simulated Surge", f"+{extra_containers} TEU", delta_color="inverse")
col4.metric("Risk Status", status)

# Row 2: The Action Banner
if "CRITICAL" in status or "GRIDLOCK" in status:
    st.error(f"🚨 **AI ACTION:** {action}")
elif "WARNING" in status or "HIGH" in status:
    st.warning(f"⚠️ **AI ADVICE:** {action}")
else:
    st.success(f"✅ **AI STATUS:** {action}")

# Row 3: The Progress Bar (Visualizing the Pressure)
st.write(f"**Terminal Capacity Usage: {int(load_pct)}%**")
bar_color = "red" if load_pct > 80 else "orange" if load_pct > 60 else "green"
st.progress(min(int(load_pct), 100), text=status)

# Row 4: Detailed Ship List
st.subheader(f"📋 Incoming Vessels at {selected_terminal}")
st.dataframe(terminal_data.style.highlight_max(axis=0), use_container_width=True)
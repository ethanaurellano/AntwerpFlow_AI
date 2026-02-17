# 🚢 AntwerpFlow AI: Intelligent Logistics Planner

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)]([YOUR_APP_LINK_HERE])
![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Status](https://img.shields.io/badge/Status-Live_Prototype-green)

> **"Predicting gate congestion before the trucks arrive."**

### 🎯 The Problem
The Port of Antwerp-Bruges faces a critical bottleneck: **Gate Surges**. When mega-vessels (like those docking at Deurganckdok) unload thousands of containers simultaneously, truck arrival patterns spike, causing massive traffic jams, delayed haulage, and increased emissions.

### 💡 The Solution
**AntwerpFlow** is a Decision Support System (DSS) designed for Logistics Managers. Unlike static dashboards, it offers **Scenario Planning** to predict bottlenecks before they happen.

### 📸 Interface Preview
![Dashboard Screenshot](dashboard.png)
*The Scenario Planner in action: Simulating a 5,000 TEU surge at Deurganckdok.*

### ⭐ Key Features
* **Real-Time Congestion Monitoring:** Tracks status across 4 major terminal zones (MPET, Deurganckdok, Kallo, Noordzee).
* **Scenario Simulation Engine:** A "What-If" slider that allows operators to stress-test terminal capacity against sudden cargo surges (0-5000 TEU).
* **Actionable AI Alerts:** Instead of just showing data, the system recommends specific actions (e.g., *"Reroute to Buffer Zone B"*).

### 🛠️ Tech Stack
This project uses a modular **3-Tier Architecture** to separate concerns:
* **Frontend:** `Streamlit` (Interactive Dashboard & Visualization)
* **Logic Layer:** `Python` (Custom Logistics Engine & Risk Algorithms)
* **Data Layer:** `Pandas` (ETL Pipeline for Port Data)

### 📂 Architecture
The codebase is structured for scalability:
```bash
├── app.py              # The Interface (UI)
├── logistics_engine.py # The Brain (Business Logic & Simulation)
└── data_loader.py      # The Connection (Data Cleaning & API Mock)

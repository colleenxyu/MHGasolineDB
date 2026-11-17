import pandas as pd
import streamlit as st
import os
import io

st.set_page_config(page_title="Dashboard Analysis Page", page_icon="🍽", layout="wide")


def logout():
    st.session_state.authenticated = False
    # Optional: force a rerun so it immediately jumps to the login screen


st.title("Dashboard Analysis Page 🍽")

st.sidebar.image("MH_Logo1.png")

st.sidebar.header("Dashboard Menu")

# Sidebar Details
st.sidebar.page_link("Home_Page.py", label="Home Page")
st.sidebar.page_link("pages/Current_Year_DB.py", label="Current Year Dashboard")
st.sidebar.page_link("pages/YearOnYear_DB.py", label="Year on Year Dashboard")
st.sidebar.page_link ("pages/DB_Analysis.py", label="Dashboard Analysis Page")

st.sidebar.header("Filter By Month:")

#DataFrameReads
gastable_df = pd.read_csv("2526GasFactTable.csv", index_col=False)
gaspervehicle_df = pd.read_csv ("2526GasPerVehicle.csv", index_col=False)


#SelectMonth
selected_month = st.sidebar.selectbox("Select Month", gastable_df["Month"].unique())
gastable_df = gastable_df[gastable_df["Month"] == selected_month].iloc[0]



#Logout Option
st.sidebar.button("Logout", on_click=logout)


with st.container(border=True):
    st.markdown("""
    ### 📊 Section 1: Current Year Gasoline Dashboard Analysis (Jan–Jun 2026)

    * **Coverage Period:** January to June 2026.
    * **Gas Spend Trends:** Total gas spend showed a marked increase in January, February, March, and May.
    * **Delivery Fares:** Includes cash spent for food and catering delivery via Lalamove. Marked increases in delivery costs occurred only in **May and June**.
    * **Consumption Volume:** Average gasoline spend ranges from **16–19 liters per month**, with a notable peak in March 2026 at **26.36 liters on average**.
    * **Global Oil Price Impact:** Cost per liter started around **53–55 pesos** (carrying over from 2025 averages), before spiking dramatically:
      * **March:** 81 pesos/liter
      * **April:** 119 pesos/liter
      * **May:** 86 pesos/liter
      * **June:** 80 pesos/liter

    ---

    ### 📈 Section 2: Year-on-Year Gasoline Dashboard Analysis (2025 vs. 2026)

    * **Comparative Scope:** Evaluates metrics for January–June 2025 against January–June 2026.
    * **Spend Increase:** Total gasoline spend increased from 2025 to 2026 in **January, February, March, May, and June**.
    * **Revenue Correlation:** This increase in fuel spend is likely explained by a comparative increase in business revenue over the same months.
    * **Delivery Cost Shifts:** Delivery costs only showed marked increases in **May** (8,529 to 13,134) and **June** (6,945 to 8,239) of 2026.
    * **Volume Stability:** Despite higher gasoline spend, total volume consumed did not increase drastically, further pointing to revenue growth as the main driver of higher costs.

    ---

    ### 🚙 Section 3: Vehicle-Specific Gasoline Dashboard Analysis

    * **Top Spenders:** The **Innova** ranks first in total gasoline spend, followed closely by the **L300 (UQJ 761)**.
    * **Transaction Cost Consistency:** Despite drastic differences in overall spend per vehicle, average cost per transaction remains relatively uniform, ranging from **1,300.00 to 1,500.00**.
    * **Volume Consistency:** Average gasoline amount ordered per transaction is also consistent across vehicles, ranging from **18 to 20 liters**.
    """)
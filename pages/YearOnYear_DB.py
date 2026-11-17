import pandas as pd
import plotly.express as px
import streamlit as st
import os
import io

st.set_page_config(page_title="Year On Year Dashboard", page_icon="🍽", layout="wide")


def logout():
    st.session_state.authenticated = False
    # Optional: force a rerun so it immediately jumps to the login screen


st.title("Year on Year Dashboard 🍽")

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
    col1, col2 = st.columns(2)

    Total_Revenue2026 = gastable_df["Revenue26"]
    Total_Revenue2025 = gastable_df ["Revenue25"]
    col1.metric(label="**Total Revenue:**", value=f"₱{Total_Revenue2026} vs ₱ {Total_Revenue2025}")

    Total_Gas_Spend26 = gastable_df["TotalGasSpend26"]
    Total_Gas_Spend25 = gastable_df ["TotalGasSpend25"]
    col2.metric(label="**Total Gasoline Spend**", value=f"₱{Total_Gas_Spend26} vs ₱ {Total_Gas_Spend25}")

    col1,col2 = st.columns (2)
    Total_Delivery_Spend26 = gastable_df["DelCost26"]
    Total_Delivery_Spend25 = gastable_df ["DelCost25"]
    col1.metric(label="**Total Delivery Fare Spend**", value=f"₱{Total_Delivery_Spend26} vs ₱ {Total_Delivery_Spend25} ")

    Total_Orders26 = gastable_df["TotalOrders26"]
    Total_Orders25 = gastable_df ["TotalOrders25"]
    col2.metric(label="**Total Orders**", value=f"{Total_Orders26} orders in 2026 vs {Total_Orders25} in 2025")

with st.container(border=True):

    Total_Volume2026 = gastable_df["TotalVolume26"]
    Total_Volume2025 = gastable_df ["TotalVolume25"]
    st.metric(label="**Total Volume Consumption**", value=f"{Total_Volume2026} liters in 2026 vs {Total_Volume2025} in 2025")

    Avg_Consumption2026 = gastable_df["AvgLiter26"]
    Avg_Consumption2025 = gastable_df ["AvgLiter25"]
    st.metric(label="**Average Gas Consumed Monthly**", value=f"{Avg_Consumption2026} liters in 2026 vs {Avg_Consumption2025} liters in 2025")

    Avg_Cost_Per_Liter26 = gastable_df["AvgCost26"]
    Avg_Cost_Per_Liter25 = gastable_df ["AvgCost25"]
    st.metric(label="**Average Cost Per Liter**", value=f"₱{Avg_Cost_Per_Liter26} in 2026 vs ₱{Avg_Cost_Per_Liter25} in 2025")

st.subheader("Vehicle Specific Dashboard")
st.markdown(
    "Please use the selectbox to choose which vehicle's costs to examine. The figures cover the period of January-June 2026 only.")

with st.container(border=True):
    # SelectVehicle
    selected_vehicle = st.selectbox("Select Vehicle", gaspervehicle_df["PlateNum"].unique())
    gaspervehicle_df = gaspervehicle_df[gaspervehicle_df["PlateNum"] == selected_vehicle].iloc[0]


    Total_Vehicle_Gas_Spend26 = gaspervehicle_df["TotalSpend26"]
    Total_Vehicle_Gas_Spend25 = gaspervehicle_df ["TotalSpend25"]
    st.metric(label="**Total Gasoline Spend**", value=f"₱{Total_Vehicle_Gas_Spend26} vs ₱{Total_Vehicle_Gas_Spend25} ")

    Total_Vehicle_Gas26 = gaspervehicle_df["TotalVol26"]
    Total_Vehicle_Gas25 = gaspervehicle_df ["TotalVol25"]
    st.metric(label="**Total Gasoline Consumption**", value=f"{Total_Vehicle_Gas26} liters vs {Total_Vehicle_Gas25} liters")

    AverageConsumption26 = gaspervehicle_df["AvgVol26"]
    AverageConsumption25 = gaspervehicle_df ["AvgVol25"]
    st.metric(label="**Average Gas Consumption**", value=f"{AverageConsumption26} liters vs {AverageConsumption25} liters")

    Average_Cost_Per_Liter26 = gaspervehicle_df["AvgCost26"]
    Average_Cost_Per_Liter25 = gaspervehicle_df ["AvgCost25"]
    st.metric(label="**Average Cost Per Transaction**", value=f"₱{Average_Cost_Per_Liter26} vs ₱ {Average_Cost_Per_Liter25}")



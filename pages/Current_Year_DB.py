import pandas as pd
import streamlit as st
import os


st.set_page_config (page_title = "Current Year Dashboard", page_icon ="🍽", layout="wide")

def logout():
    st.session_state.authenticated = False
    # Optional: force a rerun so it immediately jumps to the login screen





st.title("2026 Dashboard 🍽")

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

st.subheader("**General Dashboard**")
st.markdown("Covers the months of January-June 2026 only")

with st.container(border=True):
        col1, col2, col3, col4 = st.columns(4)

        Total_Revenue = gastable_df["Revenue26"]
        col1.metric(label="**Total Revenue:**", value=f"₱{Total_Revenue}")

        Total_Gas_Spend = gastable_df["TotalGasSpend26"]
        col2.metric(label="**Total Gasoline Spend**", value=f"₱{Total_Gas_Spend}")

        Total_Delivery_Spend = gastable_df ["DelCost26"]
        col3.metric(label="**Total Delivery Fare Spend**", value=f"₱{Total_Delivery_Spend}")

        Total_Orders = gastable_df["TotalOrders26"]
        col4.metric(label="**Total Orders**", value=f"{Total_Orders} orders")

with st.container(border=True):


        col1,col2,col3 = st.columns(3)
        Total_Volume= gastable_df ["TotalVolume26"]
        col1.metric(label="**Total Volume Consumption**", value = f"{Total_Volume} liters")

        Avg_Consumption = gastable_df ["AvgLiter26"]
        col2.metric(label = "**Average Gas Consumed Monthly**", value =f"{Avg_Consumption} liters")

        Avg_Cost_Per_Liter = gastable_df ["AvgCost26"]
        col3.metric(label = "**Average Cost Per Liter**", value = f"₱{Avg_Cost_Per_Liter}")


st.subheader("Vehicle Specific Dashboard")
st.markdown("Please use the selectbox to choose which vehicle's costs to examine. The figures cover the period of January-June 2026 only.")

with st.container(border=True):
    # SelectVehicle
    selected_vehicle = st.selectbox("Select Vehicle", gaspervehicle_df["PlateNum"].unique())
    gaspervehicle_df = gaspervehicle_df[gaspervehicle_df["PlateNum"] == selected_vehicle].iloc[0]

    col1,col2,col3,col4 = st.columns(4)
    Total_Vehicle_Gas_Spend = gaspervehicle_df ["TotalSpend26"]
    col1.metric(label ="**Total Gasoline Spend**", value = f"₱{Total_Vehicle_Gas_Spend}")

    Total_Vehicle_Gas = gaspervehicle_df ["TotalVol26"]
    col2.metric (label = "**Total Gasoline Consumption**", value = f"{Total_Vehicle_Gas} liters")

    AverageConsumption = gaspervehicle_df ["AvgVol26"]
    col3.metric (label = "**Average Gas Consumption**", value = f"{AverageConsumption} liters")

    Average_Cost_Per_Liter =gaspervehicle_df ["AvgCost26"]
    col4.metric(label = "**Average Cost Per Transaction**", value = f"₱{Average_Cost_Per_Liter}")


st.subheader("Vehicle Repair & Maintenance Expense Table")
st.markdown("Includes maintenance expenses from January-June 2025")
with st.container(border=True):

    df =pd.read_csv("VehicleExpenseTable.csv")
    st.dataframe(df)







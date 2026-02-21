import streamlit as st
import pandas as pd
import pickle
st.title("Predict Car Prices")
# data = pd.read_csv("cars24-car-price.csv")
# st.dataframe(data)

km_driven = st.number_input("Enter the kilometers driven:")
year = st.selectbox("Enter the year of manufacture:", [2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025])
fuel_type = st.selectbox("Select the fuel type:", ["Petrol", "Diesel", "CNG", "LPG", "Electric"])
seller_type = st.selectbox("Select the seller type:", ["Individual", "Dealer"])
transmission = st.selectbox("Select the transmission type:", ["Manual", "Automatic"])   
milage = st.slider("Enter the mileage:", 0, 70, step=1)
engine = st.slider("Enter the engine capacity:", 0, 5000, step=100)
max_power = st.slider("Enter the maximum power:", 0, 200, step=1)
seats = st.selectbox("Enter the number of seats:", [2, 4, 5, 6, 7, 8])


encode_dist={
    "fuel_type": {"Petrol": 0, "Diesel": 1, "CNG": 2, "LPG": 3, "Electric": 4},
    "seller_type": {"Individual": 0, "Dealer": 1},
    "transmission": {"Manual": 0, "Automatic": 1}
}

encoded_fuel_type = encode_dist["fuel_type"][fuel_type]
encoded_seller_type = encode_dist["seller_type"][seller_type]
encoded_transmission = encode_dist["transmission"][transmission]

with open("car_pred", "rb") as f:
    model = pickle.load(f)

    input_data = [[km_driven, year, encoded_fuel_type, encoded_seller_type, encoded_transmission, milage, engine, max_power, seats]]
   
if(st.button("Predict Price")):
    predicted_price = model.predict(input_data)
    st.write(f"Predicted Price: ${predicted_price[0]:,.2f}")


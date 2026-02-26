import streamlit as st
import joblib
import pandas as pd

model = joblib.load("crop_yield.pkl")

st.title("Crop Yield Predictor")
st.write("Enter the details below")

df = pd.read_csv("crop_yield.csv")  

Crop = st.selectbox("Crop", sorted(df["Crop"].unique()))
Season = st.selectbox("Season", sorted(df["Season"].unique()))
State = st.selectbox("State", sorted(df["State"].unique()))

Area = st.number_input("Area (hectares)", min_value=0.0)
Annual_Rainfall = st.number_input("Annual Rainfall (mm)", min_value=0.0)
Fertilizer = st.number_input("Fertilizer (kg)", min_value=0.0)
Pesticide = st.number_input("Pesticide (kg)", min_value=0.0)
Crop_Year = st.number_input("Crop Year", min_value=1900.0)

if st.button("Predict Production"):

    input_df = pd.DataFrame([{
        "Crop": Crop,
        "Season": Season,
        "State": State,
        "Area": Area,
        "Annual_Rainfall": Annual_Rainfall,
        "Fertilizer": Fertilizer,
        "Pesticide": Pesticide,
        "Crop_Year": Crop_Year
    }])

    prediction = model.predict(input_df)

  

    col1, col2 = st.columns(2)
    col1.metric("Predicted Production (tons)", round(prediction, 2))
    col2.metric("Yield (tons/hectare)", round(yield_efficiency, 2))

    if yield_efficiency > 5:
        st.success("High efficiency farming detected ")
    elif yield_efficiency > 2:
        st.warning("Moderate efficiency farming")
    else:
        st.error("Low yield efficiency — consider improving inputs")

   










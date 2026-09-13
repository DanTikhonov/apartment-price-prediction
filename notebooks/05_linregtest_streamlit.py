import streamlit as st
import joblib
import pandas as pd
import numpy as np
from pathlib import Path

MODEL_DIR = Path.home() / "apartment-price-prediction" / "models"
LINEAR_RIDGE = MODEL_DIR / "linear_ridge_numeric.joblib"
LINEAR_LASSO = MODEL_DIR / "linear_lasso_numeric.joblib"
LINEAR_CLASSIC = MODEL_DIR / "linear_linearregression_numeric.joblib"
LINEAR_ELASTIC_NET = MODEL_DIR / "linear_elastic net_numeric.joblib"
DATA_DIR = Path.home() / "apartment-price-prediction" / "data" / "modeling"
FILEPATH = DATA_DIR / "moscow_modeling_full.csv"

path_dict = {"Ridge": LINEAR_RIDGE, "Lasso": LINEAR_LASSO,
             "Elastic Net": LINEAR_ELASTIC_NET, "Classic LinReg": LINEAR_CLASSIC}

st.title("Тестирование модели предсказания стоимости квартир")


st.set_page_config(layout="centered")


@st.cache_resource
def load_model(path):

    return joblib.load(path)


with st.columns([1, 2, 1])[1]:
    st.header("Выбор модели")
    model = st.radio("Модель", ["Ridge", "Lasso",
                     "Elastic Net", "Classic LinReg"])
    path = path_dict[model]
    pipeline = load_model(path)


# Apartment type,Metro station,Minutes to metro,Number of rooms,Area,Living area,Kitchen area,Floor,Number of floors,Renovation,Price,source_file,Price_log

df = pd.read_csv(FILEPATH)
metro_stations = [metro_station.strip() for metro_station in set(df['Metro station'].astype(
    str)) if type(metro_station) == str and metro_station.strip() not in ['nan']]
metro_stations = list(set(metro_stations))

with st.sidebar:
    st.header("Параметры квартиры")
    apartment_type = st.radio("Тип здания", ["New building", "Secondary"])
    metro_station = st.selectbox("Станция метро", metro_stations)
    minutes_to_metro = st.slider(
        "Время до метро (мин.)", min_value=0.0, max_value=60.0)
    number_of_rooms = st.slider("Количество комнат", min_value=0, max_value=10)
    area = st.number_input("Площадь (м²)", min_value=9.0, max_value=1117.0, step=0.1)
    living_area = st.number_input("Жилая площадь (м²)",
                            min_value=2.0, max_value=min(area * 0.9, 567.0), step=0.1)
    kitchen_area = st.number_input("Площадь кухни (м²)", min_value=1.0, max_value=min(
        (area - living_area) * 0.8, 120.0), value=1.0, step=0.1)
    floor = st.slider("Этаж", min_value=1, max_value=100)
    number_of_floors = st.slider(
        "Всего этажей", min_value=floor, max_value=100) if floor != 100 else 100
    renovation = st.radio("Ремонт", [
                          "Designer", "Without renovation", "Cosmetic", "European-style renovation"])
    
new_data = pd.DataFrame([{
    "Apartment type": apartment_type,
    "Metro station": metro_station,
    "Minutes to metro": minutes_to_metro,
    "Number of rooms": number_of_rooms,
    "Area": area,
    "Living area": living_area,
    "Kitchen area": kitchen_area,
    "Floor": floor,
    "Number of floors": number_of_floors,
    "Renovation": renovation,
    "Price": 0.0,
    "source_file": "",
    "Price_log": 0.0
}])

if st.button("Предсказать цену"):
    prediction_log = pipeline.predict(new_data)[0]
    prediction_price = np.exp(prediction_log)
    st.success(
        f"Предсказанная стоимость квартиры: **{prediction_price:,.2f} руб**")

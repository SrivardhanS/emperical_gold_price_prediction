import streamlit as st
import importlib.util

spec = importlib.util.spec_from_file_location("model","gold_price_model.ipynb")
model = importlib.util.module_from_spec(spec)
spec.loader.exec_module(model)

price = model.predict_gold_price(123,213,213,124) #spx, uso, slv, eur_usd

st.title('Gold Price Prediction')

spx = st.number_input('Enter SPX Value', min_value=0)  
uso = st.number_input('Enter USO Value', min_value=0)
slv = st.number_input('Enter SLV Value', min_value=0)
eur_usd = st.number_input('Enter EUR/USD Value', min_value=0.0, max_value=5.0, step=0.01)

if st.button('Predict'):
    price = model.predict_gold_price(spx, uso, slv, eur_usd)
    st.write(f'The predicted gold price is: {price:.2f}')
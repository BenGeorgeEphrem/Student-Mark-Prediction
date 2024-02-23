import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.title("Student Final Exam Mark Prediction")
quiz1 = st.number_input("Enter Quiz 1 Mark", 0.0,10.0,step=0.01)
quiz2 = st.number_input("Enter Quiz 2 Mark", 0.0,10.0,step=0.01)
mid = st.number_input("Enter Mid Exam Mark", 0.0,20.0,step=0.01)
warn = st.radio("Attendance Warning", ("No","Yes"))

filename = 'lrmodel.sav'

@st.cache_data
def load_data():
    loaded_model = pickle.load(open(filename, 'rb'))
    return loaded_model
loaded_model= load_data()
w = 1 if warn == 'Yes' else 0
dic = {'Test 1':quiz1, 'Test 2':quiz2, 'Mid':mid,"Warning":w}
df = pd.DataFrame([dic])
res = loaded_model.predict(df)

if st.button("Predict Final Exam Mark"):
    st.write(f"Your Mark is : {res[0]:.2f}")

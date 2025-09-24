import joblib
import streamlit as st
TitanicModel = joblib.load("TitanicModel.pkl")


st.write("# Titanic Survival Prediction")
st.write("#### Enter the following details to predict survival")
Pclass = st.number_input("Pclass", 1, 3)
Sex = st.selectbox("Sex", ["male", "female"])
Age = st.number_input("Age", 0.0, 80.0)
SibSp = st.number_input("SibSp", 0, 8)
Parch = st.number_input("Parch", 0, 6)
Fare = st.number_input("Fare", 0.0, 512.0)

if Sex == "male":
    Sex = 1
else:
    Sex = 0

if st.button("Predict"):
    result = TitanicModel.predict([[Pclass, Sex, Age, SibSp, Parch, Fare]])
    if result == 1:
        st.write("Survived")
    else:
        st.write("Not Survived")


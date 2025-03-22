import streamlit as st

st.title("BMI Calculator")

height = st.slider("Enter your height in centimeters: ", 100, 250, 175)
weight = st.slider("Enter your weight in kilograms: ", 40, 200, 70)


if st.button("Calculate BMI", use_container_width=True):
    bmi = round(float(weight) / (float(height) / 100) ** 2, 2)
    st.success(f"Your BMI is {bmi}")


st.write("## BMI Categories:")
st.write("- Underweight: BMI less than 18.5")
st.write("- Normal: BMI between 18.5 and 24.9")
st.write("- Overweight: BMI between 25 and 29.9")
st.write("- Obese: BMI of 30 or more")
import streamlit as st
from datetime import datetime

current_year = datetime.now().year
yob = st.date_input("Select your Y.O.B").year

age = current_year - yob
st.write(f"Your age is: {age}")
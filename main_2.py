import streamlit as st

st.title("Chai Make App")

if st.button("Make Chai"):
    st.success("Your Chai is being brewed")

add_sugar = st.checkbox("Add Sugar")

if add_sugar:
    st.success("Sugar added to your Chai")

chai_type = st.radio("Pick your chai base: ", ["Milk", "Chai", "Water"])

st.write(f"Selected base {chai_type}")

flavour = st.selectbox("Choose flavour:", ["Adrak", "Tulsi", "Kesar"])
st.write(f"Selected Flavour: {flavour}")

sugar_level = st.slider("Sugar level", 0, 5, 4)
st.write(f"Selected Level: {sugar_level}")

cups = st.number_input("How many cups", min_value=1, max_value=10, step=1)
st.write(f"Cups: {cups}")

name = st.text_input("Enter your Name:")

if name:
    st.write(f"Welcome, {name}!, Your chai is on the way.")

dob = st.date_input("Select your D.O.B")
st.write(f"Your date of birth is {dob}")
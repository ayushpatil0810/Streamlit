import streamlit as st

st.title("Favourite Programming Language")
st.subheader("Made with Streamlit")
st.text("Select your Favourite Programming Language:")

language = st.selectbox("Your Favourite Programming Language", [
    "Python", "Java", "C", "C++", "JavaScript",
    "Ruby", "Swift", "Go", "Kotlin", "R",
    "PHP", "Rust", "TypeScript", "Perl", "Scala",
    "Dart", "Lua", "Haskell", "MATLAB", "Objective-C"
])

st.success(f"Your Favourite Programming Language is {language}.")
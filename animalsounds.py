import streamlit as st

st.title("🐾 Animal Sound App")

animal = st.text_input("Enter an animal (dog, cat, cow)")

if st.button("Show Sound"):
    if animal.lower() == "dog":
        st.write("🐶 mia meow")
    elif animal.lower() == "cat":
        st.write("🐱 amma meow")
    elif animal.lower() == "cow":
        st.write("🐮 ote mote")
    else:
        st.write("❌ Invalid animal")

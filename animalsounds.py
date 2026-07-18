import streamlit as st

st.title("🐾 Animal Sound App")

animal = st.text_input("Enter an animal (dog, cat, cow)")

if st.button("Show Sound"):
    if animal.lower() == "dog":
        st.write("🐶 Bow Bow")
    elif animal.lower() == "cat":
        st.write("🐱 Meow Meow")
    elif animal.lower() == "cow":
        st.write("🐮 Moo Moo")
    else:
        st.write("❌ Invalid animal")

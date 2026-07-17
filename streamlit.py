import streamlit as st
import random

choices = ["Rock", "Paper", "Scissors"]

st.title("Rock Paper Scissors Game")

user = st.selectbox("Choose your move:", choices)

if st.button("Play"):
    computer = random.choice(choices)

    st.write("**You chose:**", user)
    st.write("**Computer chose:**", computer)

    if user == computer:
        st.info("Draw!!")
    elif (
        (user == "Rock" and computer == "Scissors") or
        (user == "Paper" and computer == "Rock") or
        (user == "Scissors" and computer == "Paper")
    ):
        st.success("You Won!")
    else:
        st.error("Computer Won!")

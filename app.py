import streamlit as st
import pandas as pd
import numpy as np  

st.title("My First Streamlit App")
st.write("Hello, bhumi!")
st.write("lets start")   

name= st.text_input("Enter your name")
if st.button("Greet me"):
    st.write(f"Hello, {name}!")

df = pd.DataFrame(np.random.randn(10, 2), columns=['A', 'B'])
st.line_chart(df)   
st.bar_chart(df)

st.sidebar.title("Navigation")
st.image("https://www.pexels.com/search/dog/", width=200)
st.video("https://www.youtube.com/watch?v=Y6ICvSafK4g")
st.header("This is a header")
st.subheader("This is a subheader")

st.markdown("*Bold,*Italic,'Code',[Link](https://streamlit.io)")
st.code("for i in range(5): print(i)", language="python")
st.text_input("Naam kya hai bhai")
st.text_area(" Write something yaar")
st.number_input("Enter a number", min_value=0, max_value=100)
st.slider("Choose a range", 0, 100, )
st.selectbox("Select a fruit", ["Kiwi", "Peach", "Litchi"])
st.multiselect("Choose Toppings", ["Cheese", "Tomato", "Olves"])
st.radio("Pick a color", ["Red", "Green", "Blue"])

if st.checkbox("Show Details"):
    st.info("Here are more details...")

option=st.radio("Choose view", ["Show Chart", "Show Table"])
if option == "Show Chart":
    st.write("Chart would appear here")
else:    st.write("Table would appear here")
with st.form("login_form"):
    username= st.text_input("username")
    password = st.text_input("password",type="password")
    submitted = st.form_submit_button("login")

    if submitted:
        st.success(f"welcome,{username}!")

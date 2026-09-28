import streamlit as st
from datetime import date
Name=st.text_input("enter name")
Age=st.number_input("enter age")
Email=st.text_input("enter email")
Date=st.date_input("DOB",min_value=date(1998,1,1),max_value=date.today(),value=date(2000,1,1))
Gender=st.radio("Gender",['Female','Male'])
Course=st.selectbox("select course",['Python','Java','C','C++'])
btn=st.button("Register")

if btn:
    st.title("User Info")
    st.write("Name:", Name)
    st.write("Age:", Age)
    st.write("Email:",Email)
    st.write("DOB:", Date)
    st.write("Gender:", Gender)
    st.write("Course:", Course)
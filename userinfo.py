import streamlit as st
Name=st.text_input("enter name")
# st.write(name)
Age=st.number_input("enter age")
# st.write(age)
Place=st.text_input("enter place")
# st.write(place)
Gender=st.radio("select gender",['Female','Male','Other'])
# st.write(gender)
Qualification=st.selectbox("select qualification",['BCA','BBA','Btech','BCOM'])
# st.write(Qualification)
btn=st.button("submit")
if btn:
    st.title("User Info")
    st.write("Name:", Name)
    st.write("Age:", Age)
    st.write("Place:", Place)
    st.write("Gender:", Gender)
    st.write("Qualification:", Qualification)






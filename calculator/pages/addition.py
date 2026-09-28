import streamlit as st
st.title("Addition")

num1=st.number_input("enter number1",min_value=0)
print(num1)
num2=st.number_input("enter number2",min_value=0)
print(num2)
btn=st.button("Add")

if btn:  #when button click it will execute if block
    result=num1+num2
    print(result)

    st.write(result) #shows in interface


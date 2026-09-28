import streamlit as st
st.title("BMI")
weight=st.number_input("Weight in kg")
print(weight)
height=st.number_input("Height in cm")
print(height)
btn=st.button("bmi")
if btn:  #when button click it will execute if block
    bmi=weight/((height/100)**2)
    print(bmi)

    st.write(bmi) #shows in interface

    if bmi<18.5:
        st.info("underweight")
    elif 18.5<=bmi<25:
        st.success("normal")
    elif 25<=bmi<30:
        st.warning("overweight")
    else:
        st.error("obesity")
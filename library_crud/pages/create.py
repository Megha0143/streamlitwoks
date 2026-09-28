import streamlit as st
from classbookdb import BookListCreateRetrieveUpdateDelete

st.title("Add new book records")
t=st.text_input("Title")
a=st.text_input("Author")
p=st.number_input("Price")
pg=st.number_input("Pages")
l=st.text_input("Language")
btn=st.button("Add")
if btn:
    b=BookListCreateRetrieveUpdateDelete()
    b.create(t,a,p,pg,l)
    st.success("Record create Successfully")


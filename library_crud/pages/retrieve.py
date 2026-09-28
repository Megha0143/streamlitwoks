import streamlit as st
from classbookdb import BookListCreateRetrieveUpdateDelete
st.title("Read a book record")

i=st.number_input("Enter id",min_value=0)
btn=st.button("Retrieve")
if btn:
    b=BookListCreateRetrieveUpdateDelete()
    record=b.retrieve(i)
    print(record)

    if record:
        st.write("Title:",record[1])
        st.write("Author:",record[2])
        st.write("Price:",record[3])
        st.write("Pages:",record[4])
        st.write("Language:",record[5])
    else:
        st.error("Oops...Book record not found")
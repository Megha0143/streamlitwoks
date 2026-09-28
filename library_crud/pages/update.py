import  streamlit as st
from classbookdb import BookListCreateRetrieveUpdateDelete
st.title("Update book record")
i=st.number_input("Enter id",min_value=0)
st.title("Add new book records")
t=st.text_input("Title")
a=st.text_input("Author")
p=st.number_input("Price")
pg=st.number_input("Pages")
l=st.text_input("Language")
btn=st.button("Update")
if btn:
    b=BookListCreateRetrieveUpdateDelete()
    record=b.update(i,t,a,p,pg,l)
    print(record)
    if record:
        st.success("Updated Successfully")
    else:
        st.error("Oops...Book record not found")
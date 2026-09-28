import  streamlit as st
from classbookdb import BookListCreateRetrieveUpdateDelete
st.title("Delete a book record")
i=st.number_input("Enter id",min_value=0)
btn=st.button("Delete")
if btn:
    b=BookListCreateRetrieveUpdateDelete()
    record=b.delete(i)
    if record:
        st.success("Book record deleted")
    else:
        st.error("Oops...Book record not found")



import streamlit as st
from classbookdb import  BookListCreateRetrieveUpdateDelete
st.title("welcome to my app")
tab1,tab2,tab3,tab4,tab5=st.tabs(['ADD','READ','RETRIEVE','DELETE','UPDATE'])


b=BookListCreateRetrieveUpdateDelete()

with tab1:
    st.title('ADD')
with tab2:
    st.title('READ')
with tab3:
    st.title('RETRIEVE')
with tab4:
    st.title('DELETE')
with tab5:
    st.title('UPDATE')
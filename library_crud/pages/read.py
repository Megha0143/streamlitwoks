import streamlit as st
st.title("Read all book records")

from classbookdb import BookListCreateRetrieveUpdateDelete
b=BookListCreateRetrieveUpdateDelete()
records=b.list()

# print("hello")
# print(records)
# st.table(records)
if records:
    data = []

    for row in records:
        data.append({
            "ID": row[0],
            "Title": row[1],
            "Author": row[2],
            "Price": row[3],
            "Pages": row[4],
            "Language": row[5]
        })

    st.table(data)
else:
    st.write("No records found")
import streamlit as st

tasks = []

st.set_page_config(layout="wide")
st.title("!TaskIt")

new_task = st.text_input('Enter your Task')
if st.button('Add'):
    pass

st.sidebar.header('Analyze your tasks!')
st.sidebar.caption('*Early Stage App, Sidebar to be created at a later stage to add more functionalities')
selected_model = st.sidebar.selectbox('To be created', ['Plot your Progress', 'Focus Mode'])

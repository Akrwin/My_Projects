import streamlit as st 
from constant import *

st.set_page_config(page_title='Akkarawin portfolio' ,layout="wide",page_icon='👨‍🔬')

st.header('Akkarawin Saiprapakorn👏')

st.write('This is my portfolio')
st.write(info['brief'])

st.subheader('Skills & Tools')

col1, col2, col3 = st.columns(3)

with col1:
    st.button(info['skills'][1])
    st.button(info['skills'][2])
    
with col2:
    st.button(info['skills'][3])
    st.button(info['skills'][4])

with col3:
    st.button(info['skills'][5])
    st.button(info['skills'][0])

st.subheader('Education📖')

st.subheader('Experience📖')

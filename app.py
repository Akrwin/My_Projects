import streamlit as st 
from constant import *

st.set_page_config(page_title='Akkarawin portfolio' ,layout="wide",page_icon='👨‍🔬')

st.header('Akkarawin Saiprapakorn👏')

st.write('This is my portfolio')
st.write(info['brief'])

st.subheader('Skills & Tools')

def skill_tab():
    rows,cols = len(info['skills'])//skill_col_size,skill_col_size
    skills = iter(info['skills'])
    if len(info['skills'])%skill_col_size!=0:
        rows+=1
    for x in range(rows):
        columns = st.columns(skill_col_size)
        for index_ in range(skill_col_size):
            try:
                columns[index_].button(next(skills))
            except:
                break
with st.spinner(text="Loading section..."):
    skill_tab()

st.subheader('Education📖')

st.subheader('Experience📖')

import streamlit as st
import streamlit.components.v1 as components 
from constant import *

st.set_page_config(page_title='Akkarawin portfolio' ,layout="wide",page_icon='🌲')

st.title('Akkarawin Saiprapakorn 👏')

st.write('This is my portfolio')
st.write(info['brief'])

# Sidebar
with st.sidebar:
    st.title("Akkarawin Saiprapakorn 👦")
    components.html(info['linkedin'],height=310)

# Skill 
st.title('Technical Skills 🖥️')

col1, col2, col3 = st.columns(3)

with col1:
    st.button(info['skills'][0])
    st.button(info['skills'][1])
    
with col2:
    st.button(info['skills'][2])
    st.button(info['skills'][3])

with col3:
    st.button(info['skills'][4])
    st.button(info['skills'][5])

# Education
st.title('Education 📖')
st.markdown('<h3>'+educations['Institute']+'</h3>',unsafe_allow_html=True)
st.caption(educations['Qualification']+educations['Major'])
st.caption(educations['Year'])

# Experience
st.title('Experience 🗂️')


import streamlit as st
import streamlit.components.v1 as components 
from constant import *

st.set_page_config(page_title='Akkarawin portfolio' ,layout="wide",page_icon='🌲')

st.title('Akkarawin Saiprapakorn 👦')

st.header('Summary')
st.write(info['brief'])

# Sidebar
with st.sidebar:
    st.title("Akkarawin Saiprapakorn")
    components.html(info['linkedin'],height=310)

# Skill 
st.header('Technical Skills 🖥️')

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
st.header('Education 📖')
st.markdown('<h5>'+educations['Institute']+'</h5>',unsafe_allow_html=True)
st.caption(educations['Year'])
st.write(educations['Qualification']+educations['Major'])

# Experience
st.header('Work Experience 🗂️')

def work(i):
    st.markdown('<h5>'+work_exp['corp'][i]+'</h5>',unsafe_allow_html=True)
    st.caption(work_exp['year'][i])
    achievement_list = ''.join(['<li>'+item+'</li>' for item in work_exp['des'][i]])
    st.markdown('<ul>'+achievement_list+'</ul>',unsafe_allow_html=True)

work(0)
work(1)

# Certificates
st.header('Certificates 🔥')

st.markdown('<h5>'+certi[1]['name']+'</h5>',unsafe_allow_html=True)
st.markdown('*offer by *: ***'+certi[1]['offer_by']+'***.',unsafe_allow_html=True)

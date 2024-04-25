import streamlit as st
import streamlit.components.v1 as components 
from constant import *
import webbrowser
from PIL import Image
from streamlit_timeline import timeline
import pandas as pd
from bokeh.models.widgets import Div

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

def certii(i):
    st.markdown('<h5>'+certi[i]['name']+'</h5>',unsafe_allow_html=True)
    st.markdown('Offered by ***'+certi[i]['offer_by']+'***.',unsafe_allow_html=True)
    with st.expander('detailed description'):
        if st.button('Link Originals Certificates('+certi[i]['caption']+')'):
            js = "window.open('https://github.com/Akrwin/My_Projects/blob/main/app.py')"
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)
        

certii(0)
certii(1)

import streamlit as st 
from constant import *

st.set_page_config(page_title='Akkarawin portfolio' ,layout="wide",page_icon='👨‍🔬')

st.header('Akkarawin Saiprapakorn👏')

st.write('This is my portfolio')
st.write(info['brief'])

# Sidebar
with st.sidebar:
    st.title("Akkarawin Saiprapakorn")
    components.html('<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script><div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="dark" data-type="VERTICAL" data-vanity="harshitwadhwani" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://www.linkedin.com/in/ak4rawin/?trk=opento_sprofile_topcard"></a></div>', height = 310 )

# Skill 
st.subheader('Technical Skills')

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

# Education
st.subheader('Education📖')
st.markdown('<h5>'+educations['Institute']+'</h5>',unsafe_allow_html=True)
st.caption('    '+educations['Qualification']+educations['Major'])
st.caption('    '+educations['Year'])

# Experience
st.subheader('Experience')

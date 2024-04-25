import streamlit as st
import streamlit.components.v1 as components 
from constant import *
from bokeh.models.widgets import Div


st.set_page_config(page_title='Akkarawin portfolio' ,layout="wide",page_icon='🌲')

# st.header('**Akkarawin Saiprapakorn**    👦')

# st.header(':blue[Summary]')
st.markdown('<p style="color:#314E52"><font size="+6"><strong>Summary 🍀<strong></font></p>', unsafe_allow_html=True)
st.write(info['brief'])

# Sidebar
# Change colored
st.markdown("""
                <style>
                    [data-testid=stSidebar] {
                        background-color: #27374D;
                    }
                </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown('<p style="color:white"><font size="+7"><strong>Akkarawin Saiprapakorn<strong></font></p>', unsafe_allow_html=True)

    components.html(info['linkedin'],height=280)
    
    st.caption('github and download 👾')
    col_1,col_2,col_3 = st.columns(3)
    with col_1:
        st.button('Github')
    with col_2:
        st.button('Resume')
    with col_3:
        st.button('CV')

    st.markdown('#')
    st.caption('github(python code for this app) 💬')
    st.button('Python code for this app')

# Skill 
# st.header(':blue[Technical Skills 🖥️]')
st.markdown('<p style="color:#314E52"><font size="+6"><strong>Technical Skills 🖥️<strong></font></p>', unsafe_allow_html=True)

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
# st.header(':blue[Education 📖]')
st.header('#')
st.markdown('<p style="color:#314E52"><font size="+6"><strong>Education 📖<strong></font></p>', unsafe_allow_html=True)
st.markdown('<h5>'+educations['Institute']+'</h5>',unsafe_allow_html=True)
st.caption(educations['Year'])
st.write(educations['Qualification']+educations['Major'])

# Experience
# st.header(':blue[Work Experience 🗂️]')
st.header('#')
st.markdown('<p style="color:#314E52"><font size="+6"><strong>Work Experience 🗂️<strong></font></p>', unsafe_allow_html=True)

def work(i):
    st.markdown('<h5>'+work_exp['corp'][i]+'</h5>',unsafe_allow_html=True)
    st.caption(work_exp['year'][i])
    achievement_list = ''.join(['<li>'+item+'</li>' for item in work_exp['des'][i]])
    st.markdown('<ul>'+achievement_list+'</ul>',unsafe_allow_html=True)

work(0)
work(1)

# Certificates
# st.header(':blue[Certificates 🔥]')
st.header('#')
st.markdown('<p style="color:#314E52"><font size="+6"><strong>Certificates🔥<strong></font></p>', unsafe_allow_html=True)

def certii(i):
    st.markdown('<h5>'+certi[i]['name']+'</h5>',unsafe_allow_html=True)
    st.markdown('Offered by ***'+certi[i]['offer_by']+'***.',unsafe_allow_html=True)
    with st.expander('Show credential'):
        if st.button('Link Originals Certificates('+certi[i]['caption']+')'):
            js = f"window.open('{certi[i]['credential']}')"
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)
        
for i in certi :
    certii(i)

# Projects
# st.header(':blue[Projects🐤]')
st.header('#')
st.markdown('<p style="color:#314E52"><font size="+6"><strong>Projects🐤<strong></font></p>', unsafe_allow_html=True)
def Projects(i):
    st.markdown('<h5>'+proj_h[i]['name']+'</h5>',unsafe_allow_html=True)
    st.markdown('description : ***'+proj_h[i]['descript']+'***.',unsafe_allow_html=True)
    with st.expander('Show description'):
        st.button('download '+proj_h[i]['name']+'projects')

for i in proj_h:
    Projects(i)

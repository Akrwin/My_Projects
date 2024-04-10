import streamlit as st 
from constant import *

st.set_page_config(page_title='Akkarawin portfolio' ,layout="wide",page_icon='👨‍🔬')

st.header('Akkarawin Saiprapakorn👏')

st.write('This is my portfolio')
st.write(info['brief'])

# Skill 
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

# Education
st.subheader('Education📖')
df = pd.DataFrame(data, columns=['Institute','Qualification ','Major','Year'])
hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)
st.table(df)

# Experience
st.subheader('Experience')



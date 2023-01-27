import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

#Find emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
     r = requests.get(url)
     if r.status_code !=200:
          return None
     return r.json()

# Use Local CSS
def local_css(file_name):
     with open(file_name) as f:
          st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")


# ---- Load Assets ----
lottie_code = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_DbCYKfCXBZ.json")
img_KPI3_form = Image.open('images\KP13.png')
img_ciclo_form = Image.open('images\ciclodevida.png')

# ---- Header Section ----
st.subheader("Hi, We are Team 15: ")
st.title("This is our final Project of Data Science from Henry")
st.write("Este es un texto de ejemplo osea Lorem Ipsum")

# --- What I Do ----

with st.container():
     st.write("---")
     left_column, right_column = st.columns(2)
     with left_column:
          st.header('What I Do')
          st.write('##')
          st.write(
               '''
               esto 
               es
               documentación.
               
               =)
               =D
               
               '''
          )
     
     st.write('[Prueba PowerBi] (https://app.powerbi.com/reportEmbed?reportId=218673b7-267a-4606-977a-fef7cc1ec0d2&autoAuth=true&ctid=d8394b2a-09cf-4936-ae34-8b0e929034d5) ')

with right_column:
     st_lottie(lottie_code, height=300, key= "coding")

# --- Projects ----

with st.container():
     st.write("---")
     st.header("My Projects")
     st.write('##')
     image_column, text_column = st.columns((1,2))
     
     with image_column:
          st.image(img_KPI3_form)

     with text_column:
          st.subheader('Integra Animaciones Lottie dentro de Streamlite App')
          st.write(
               '''
               Aprende como usar Archivos Lottie en Streamlit!
               Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do 
               In this tutorial, i'll show you exactly how to do it 
               '''
          )
          st.markdown('[watch Video....](https://www.youtube.com/watch?v=VqgUkExPvLY)')

with st.container():
     image_column, text_column = st.columns((1,2))
     
     with image_column:
          st.image(img_ciclo_form)

     with text_column:
          st.subheader('Integra Animaciones Lottie dentro de Streamlite App')
          st.write(
               '''
               Aprende como usar Archivos Lottie en Streamlit!
               Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do 
               In this tutorial, i'll show you exactly how to do it 
               '''
          )
          st.markdown('[watch Video....](https://www.youtube.com/watch?v=VqgUkExPvLY)')

with st.container():
     st.write('---')
     st.header('Get in touch with Me!')
     st.write('##')

     #Documentación: https://formsubmit.co/
     contact_form = '''
          <form action="https://formsubmit.co/zavaletacode@gmail.com" method="POST">
          <input type="hidden" name ="_captcha" value= "false">
          <input type="text" placeholder="Your name" required>
          <input type="email" placeholder="Your email" required>
          <textarea name= "message" placeholder="Your message here" required ></textarea>
          <button type="submit">Send</button>
     </form>
     '''

     left_column, right_column = st.columns(2)
     with left_column: 
          st.markdown(contact_form, unsafe_allow_html=True)
     with right_column:
          st.empty()

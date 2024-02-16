import folium
import mysql.connector
import streamlit as st
from streamlit_folium import st_folium
# https://streamlit.io/
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="streamlit_db"
)

mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")
for tables in mycursor:
    if 'users' not in tables:
        mycursor.execute("""
                CREATE TABLE users(
                         id INT AUTO_INCREMENT PRIMARY KEY,
                         f_name VARCHAR(255), 
                         l_name VARCHAR(255))
                """)


st.header("Python streamlit")
st.write("Tp Streamlit")   
images = st.camera_input("Take A Photos")   
if images:
    st.image(images) 

with st.form('Regester'):
    f_name = st.text_input('First Name')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    l_name = st.text_input('Last Name')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    submit = st.form_submit_button("seve")
    if submit:
        req = "INSERT INTO users(f_name,l_name) VALUES (%s, %s)"
        val = (f_name,l_name)
        mycursor.execute(req,val)
        mydb.commit()
        st.write("The user was regesterd successfuly")




# center on Liberty Bell, add marker
m = folium.Map(location=[33.528496, -5.105826], zoom_start=1)
folium.Marker(
    [33.528496, -5.105826], popup="Marocco - Ifrane", tooltip="Lion Ifrane"
).add_to(m)

# call to render Folium map in Streamlit
st_data = st_folium(m, width=725)
import mysql.connector
import streamlit as st

# Uses st.experimental_singleton to only run once.
@st.experimental_singleton(show_spinner=False)
def init_connection(): # start a websocket to the database server
   return mysql.connector.connect(user = "recipeApp", password = "cS348!project", host = "165.232.138.171", database = "main")
   #return mysql.connector.connect(**st.secrets["db_credentials"])
cnx = init_connection()

@st.experimental_memo(ttl=600, show_spinner=False)
def query(q: str, params=None, insert: bool = False): # query the database server
    try:
        cursor = cnx.cursor()
    except:
        init_connection.clear()
        cnx = init_connection()
        cursor = cnx.cursor()

    try:
        if params:
            cursor.execute(q, params)
        else:
            cursor.execute(q)
    except Exception as e:
        print(e)
        return []
    
    if insert:
        try:
            cnx.commit()
            print('commited')
        except Exception as e:
            print(e)
            return []

    response = cursor.fetchall()
    cursor.close()
    return response

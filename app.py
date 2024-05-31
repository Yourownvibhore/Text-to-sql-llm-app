from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
import sqlite3

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# load gemini model
def get_gemini_response(question,prompt):
    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content([prompt[0],question])
    return response.text

def read_sql_query(sql,db):
    connection=sqlite3.connect('student.db')
    cursor=connection.cursor()
    cursor.execute(sql)
    rows=cursor.fetchall()
    connection.commit()
    connection.close()
    for row in rows:
        print(row)
    return rows

prompt=[
"""
You are an expert in converting English questions to SQL query!
    The SQL database has the name student and has the following columns - name, roll, 
    section,marks \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM student ;
    \nExample 2 - Tell me all the students studying in A section?, 
    the SQL command will be something like this SELECT * FROM student 
    where section="A"; 
    also the sql code should not have ``` in beginning or end and sql word in output
"""
]


st.set_page_config(page_title="SQL Query Generator",page_icon="📊")
st.title("SQL Query Generator")
st.write("This app generates SQL queries based on the questions asked by the user.")
question=st.text_input("Enter your question here:",key="input")
submit=st.button("Generate SQL Query")

if submit:
    response=get_gemini_response(question,prompt)
    st.write(response)
    rows=read_sql_query(response,"student.db")
    for row in rows:
        st.write(row)
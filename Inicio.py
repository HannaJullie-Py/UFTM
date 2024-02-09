
import mysql
import mysql.connector
import streamlit as st
import numpy as np
import pandas as pd


##### Conexão ao Banco MySQL #####
def conn_mysql():
        config = {
            "user" : "root",
            "password" : "ctti",
            "host" : "127.0.0.1",
            "port" : "3306",
            "database" : "facul",
            "raise_on_warnings":True
        }
    
        try:
            conexao = mysql.connector.connect(**config)
            return conexao
        except mysql.connector.Error as err:
            st.error(f"Erro ao conectar ao banco MySQL: {err}")
            return None

st.image('https://i.imgur.com/TBvRRfw.jpg', width=720)
st.divider()
st.title('Bem-Vindo(a) à Universidade Federal de Tangamandápio (UFTM)')
    
    

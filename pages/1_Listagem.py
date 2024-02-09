import mysql.connector
import streamlit as st
import pandas as pd
import numpy as np
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



def pagina_exibicao():
    st.title('Listagem de alunos matriculados')
    conexao = conn_mysql()
    if conexao:        
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM Alunos')
        resultados = cursor.fetchall()
        st.write("Resultados da consulta ao banco de dados MySQL: ")
        for resultado in resultados:
            st.write(f'CPF: {resultado[0]}, Nome: {resultado[1]}, Curso: {resultado[2]}, Telefone de contato: {resultado[3]}, Email: {resultado[4]}')
st.header('Listagem dos Alunos', divider='rainbow')
st.title('Nesta Página')
st.markdown('''Você poderá ver quais alunos estão matriculados na **Universidade Federal de Tangamandápio**
\nClique no botão :red["Mostrar alunos matriculados"] para ver nossa lista de alunos matriculados''')
if st.button('Mostrar alunos matriculado'):
        pagina_exibicao()

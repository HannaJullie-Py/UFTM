#Caso não tenha instalado, deve instalar
#pip install mysql-connector-python
#pip install streamlit-authenticator
#pip install streamlit

import mysql.connector
import streamlit as st
import numpy as np
import pandas as pd
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

with open('../config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

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
    
##### LOGIN #####

hashed_passwords = stauth.Hasher(['aluno2024', 'professor2024']).generate()

##### FUNÇÕES #####

##### PAGINAS #####
 
#### Pagina 1 ####
def pagina_inicio():
    st.image('https://i.imgur.com/TBvRRfw.jpg', width=720)
    st.divider()
    st.title('Bem-Vindo(a) à Universidade Federal de Tangamandápio (UFTM)')


#### Pagina 2 ####

def pagina_cadastro():
    st.header('Cadastro', divider='rainbow')
    st.title('Nesta Página')
    st.markdown('''Você vai cadastrar o aluno na Universidade Estadual de Tangamandápio (UFTM)''')
    st.divider()
    conexao = conn_mysql()
    cpf = st.text_input('Digite seu CPF')
    nome = st.text_input('Digite seu Nome')
    curso = st.text_input('Digite o curso em que está matriculado')
    ctt = st.text_input('Digite seu telefone de contato')
    email = st.text_input('Digite seu Email')
    if conexao:
        cursor = conexao.cursor()
        joja = st.button('Cadastrar')
        if joja:
            st.success("Aluno matriculado com sucesso")
            cursor.execute('INSERT INTO alunos (CPF, Nome, Curso, Telefone, Email) values (%s,%s,%s,%s,%s)', (cpf,nome,curso,ctt,email))
        conexao.commit()

#### Pagina 3 ####

def pagina_bonita():
    st.header('Listagem dos Alunos', divider='rainbow')
    st.title('Nesta Página')
    st.markdown('''Você poderá ver quais alunos estão matriculados na **Universidade Federal de Tangamandápio**
    \nClique no botão :red["Mostrar alunos matriculados"] para ver nossa lista de alunos matriculados''')

#### Pagina 3.2 ####

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

#### Chamar as paginas ####
pagina_atual = st.sidebar.radio('Selecione uma opção:',('Início','Cadastro','Listagem'))
if pagina_atual == 'Cadastro':
    pagina_cadastro()
elif pagina_atual == 'Início':
    pagina_inicio()
elif pagina_atual == 'Listagem':
    pagina_bonita()
    if st.button ('Mostrar alunos matriculados'):
        st.divider()
        pagina_exibicao()        

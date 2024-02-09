import streamlit as st
import mysql.connector
import pandas as pd
import numpy as np



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

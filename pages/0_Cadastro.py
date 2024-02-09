
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

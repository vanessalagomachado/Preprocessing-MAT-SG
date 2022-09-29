from Funcoes import Funcoes 

#Funcoes().leitor_de_entrada(input("informe o diretorio do arquivo: "))
while True:
    print("1 - Organizar colunas")
    print("2 - Excluir Coluna")
    print("3 - Juntar Colunas")
    print("4 - Exportar em CSV")
    print("0 - Sair")
    numero = int(input())
    if numero == 1:
        Funcoes().organizar(input("escreva o nome das colunas com aspas dentro de colchetes separado por virgula: "))
    if numero == 2:
        Funcoes.excluir_coluna(input("escreva o nome das colunas com aspas dentro de colchetes saparado por virgula: "))
    if numero == 3:
        coluna1 =input("escreva o nome das coluna 1: ")
        coluna2 = input("escreva o nome das colunas 2: ")
        newcoluna = input("nome da coluna com a juncao das 2 anteriores: ")
        separador = input("separador entre a junçao das colunas: ")
        eixo = input("eixo de juncao das colunas: ")
        Funcoes().juntar_colunas(newcoluna,coluna1,coluna2,separador,eixo)
    if numero == 4:
        Funcoes().exportar_csv(input("nome do arquivo: "))
    if numero == 0:
        break
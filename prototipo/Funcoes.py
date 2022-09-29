import pandas as pd
import os

class Funcoes:

    def __init__(self):
        self.tabela_modificada = pd.DataFrame()

    #ok
    def organizar(self, colunas:list):
        self.tabela_modificada = self.tabela_modificada[colunas]
        print("colunas reordenadas")

    def converter_formato_datetime(self, coluna:str):
        self.tabela_modificada[coluna]= pd.to_datetime(self.tabela_modificada[coluna])

    #ok
    def leitor_de_entrada(self, diretorio):
        tabela_antiga = pd.DataFrame()
        try:
            for arquivo in os.listdir(diretorio):
                tabela_df = pd.read_csv(os.path.join(diretorio, arquivo),"r",header=None)
                tabela_antiga= pd.concat([tabela_antiga, tabela_df])
            self.tabela_modificada = tabela_antiga
        except:
            self.tabela_modificada = pd.read_csv(diretorio)

    #ok
    def excluir_coluna(self, colunas:list):
        self.tabela_modificada = self.tabela_modificada.drop(columns=colunas)
        print("coluna/s excluidas")

    #ok
    def exportar_csv(self, nome:str):
        self.tabela_modificada.to_csv(nome +".csv", index= False)
        print("arquivo salvo")

    def modificar_tipo_de_dado(self, coluna:str, tipo:str):
        self.tabela_modificada[coluna] = self.tabela_modificada[[coluna]].astype(tipo)

    def juntar_tabelas(self, tabela1, tabela2, forma:str):
        self.tabela_modificada = pd.merge(tabela1,tabela2, how=forma)

    #ok
    def juntar_colunas(self, juncao:str, coluna1:str, coluna2:str, separador:str, eixo:int):
        self.tabela_modificada[[coluna1, coluna2]] = self.tabela_modificada[[coluna1, coluna2]].astype(str)
        self.tabela_modificada[juncao] = self.tabela_modificada[[coluna1,coluna2]].agg(separador.join, axis= eixo)
        print("colunas juntadas")
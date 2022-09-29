
import pandas as pd
import os as os

file =r"C:\Users\block\Desktop\codigos_leitor_de_CSV\Geolife_Trajectories_1.3\Data\052\Trajectory"
file_locomocao = r"C:\Users\block\Desktop\codigos_leitor_de_CSV\Geolife_Trajectories_1.3\Data\052\labels.txt"
cont = 0
tabela_antiga = pd.DataFrame()
for arquivo in os.listdir(file):
    tabela_df = pd.read_csv(os.path.join(file, arquivo),"r",header=None)
    tabela_df = tabela_df.drop(tabela_df.index[[0,1,2,3,4,5]])
    tabela_antiga= pd.concat([tabela_antiga, tabela_df])
    cont += 1
tabela_locomocao = pd.read_table(file_locomocao)
print(tabela_antiga)
tabela_antiga = tabela_antiga.drop(columns=[1,2])
tabela_antiga = tabela_antiga[0].str.split(",",-1,True)
tabela_antiga = tabela_antiga.drop(columns=[2,4])
tabela_editavel = tabela_antiga
tabela_antiga = tabela_antiga[[0,1,5,6]].astype(str)
tabela_editavel["lat_lon"] = tabela_antiga[[0,1]].agg(' '.join, axis= 1)
tabela_editavel["altitude"] = tabela_editavel[3]
tabela_editavel['Start Time'] = tabela_antiga[[5,6]].agg(' '.join, axis= 1)
tabela_editavel = tabela_editavel.drop(columns=[0,1,6,5,3])
tabela_editavel.loc[tabela_editavel["altitude"] == -777, "altitude"] = -1
tabela_locomocao['Start Time']= pd.to_datetime(tabela_locomocao['Start Time'])
tabela_locomocao['End Time']= pd.to_datetime(tabela_locomocao['End Time'])
tabela_editavel["Start Time"] = tabela_editavel[["Start Time"]].astype('datetime64')
mistura = pd.merge(tabela_editavel,tabela_locomocao, how="outer")
mistura.to_csv("teste52.csv", index = False)
print(tabela_editavel)
print(tabela_locomocao)
print(mistura)
print(cont)
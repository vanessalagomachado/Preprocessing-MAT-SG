from operator import index
from time import strftime
import pandas as pd

tabela_df = pd.read_csv(r"C:\Users\block\Downloads\Hurricanes_1944_to_1948.csv")
tabela_organizada = tabela_df[["class","tid","LatLon","WindSpeed","Pressure","Name",]]
tabela_hora = tabela_df[['Hour']].astype(str)
tabela_hora = tabela_hora.assign(min='00',sec='00')
tabela_hora = tabela_hora[['Hour','min','sec']].agg(':'.join, axis=1)
tabela_organizada['Hour'] = pd.to_datetime(tabela_hora,format= '%H:%M:%S')\
                        .apply(lambda x: x.strftime('%H:%M:%S'))
tabela_data = tabela_df[['Year','Month','Day']]
tabela_organizada['time'] = pd.to_datetime(tabela_data,format= '%Y-%m-%d')\
                        .apply(lambda x: x.strftime('%Y-%m-%d'))
tabela_organizada['date_time_copy'] = tabela_organizada[['time','Hour']].agg(' '.join, axis= 1)
tabela_organizada.insert(3,"date_time",tabela_organizada['date_time_copy'])
tabela_organizada = tabela_organizada.drop(columns=["Hour","time","date_time_copy"])
tabela_organizada.to_csv("arquivo2.csv", index = False)
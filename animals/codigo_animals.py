import pandas as pd

tabela_df = pd.read_csv(r"C:\Users\block\Downloads\projeto PET\Animals_specific_test.csv")
tabela_organizada = tabela_df[["label","tid"]]
tabela_lat_lon = tabela_df[["lat","lon",]].astype(str)
tabela_lat = tabela_lat_lon[['lat','lon']].agg(' '.join, axis= 1)
tabela_organizada.insert(2,"lat_lon",tabela_lat)
tabela_date = pd.to_datetime(tabela_df["time"],unit="m",)
tabela_date = tabela_date.dt.round(freq='s',)
tabela_organizada.insert(3,"date_time",tabela_date)

tabela_organizada.to_csv("animals_formated.csv", index=False)
import pandas as pd

tabela_df = pd.read_csv(r"C:\Users\block\Downloads\projeto PET\Vania-Foursquare\Vania-Foursquare.csv")
tabela_organizada = tabela_df[["label","tid","lat_lon","date_time","day","poi","type","root_type","price","rating","weather"]]
tabela_organizada.to_csv("arquivonovo.csv", index=False)
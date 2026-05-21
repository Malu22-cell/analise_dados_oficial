import requests
import pandas as pd
base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc3MTE5MzIwLCJpYXQiOjE3NzQ1MjczMjAsImp0aSI6ImY1OWE1YTM1MzgwNjQxMzc4MDA1NDBhZDU1ZTNkZTY2IiwidXNlcl9pZCI6IjEyNSJ9.SpCIAGyeyHW_EqevLvBfkJANPFhqO0JuIZqEVph-cXE"
#Ibov
params = {"ticker": "Ibov", "data_ini": "2000-01-01", "data_fim": "2025-12-31"}
resp = requests.get(
    f"{base_url}/preco/diversos",
    headers={"Authorization": f"Bearer {token}"},
    params=params,
)
dados = resp.json()
Ibov = pd.DataFrame(dados)

#Dolar 
params = {"ticker": "usd_brl", "data_ini": "2000-01-01", "data_fim": "2025-12-31"}
resp = requests.get(
    f"{base_url}/preco/diversos",
    headers={"Authorization": f"Bearer {token}"},
    params=params,
)
dados = resp.json()
Dolar = pd.DataFrame(dados)

#Garantir que os campos sejam do tip Datatime
Ibov["data"]= pd.to_datetime(Ibov["data"])
Dolar["data"]= pd.to_datetime(Dolar["data"])

#Selecionar apenas o preço de fechamento 
Ibov = Ibov[["data", "fechamento"]]
Dolar = Dolar[["data", "fechamento"]]

#Renomeia as colunas 
Ibov = Ibov.rename(columns={"fechamento":"Ibov"})
Dolar = Dolar.rename(columns={"fechamento":"Dolar"})

#Merge entre os dois df através do campo data
df = pd.merge(Ibov, Dolar, on="data", how="inner")

#Correlação 
df[["Ibov", "Dolar"]].corr()

#Criação do df de datas 
datas = pd.date_range("2000-01-01", "2025-12-31", freq="B")
df_base = pd.DataFrame({"data":datas})
df_base = pd.merge(df_base, Ibov, on="data", how="left")
df_base = pd.merge(df_base, Dolar,on="data", how="left")

#Tratamento dos dados faltantes 
df_base.isna().sum()
df_base.dropna()
df_base.ffill() #forward fill 
df_base.bfill() #backard fill
#
df.head()
df.info()
df.columns
df["Ibov"] = pd.to_numeric(df["Ibov"], errors="coerce")
df["Dolar"] = pd.to_numeric(df["Dolar"], errors="coerce")
df["ret_Ibov"] = df["Ibov"].pct_change()
df["ret_Dolar"] = df["Dolar"].pct_change()

#Correção
import seaborn as sn 
corr = df[["ret_Ibov", "ret_Dolar"]].corr()
sn.heatmap(corr, annot=True)

#Histograma 
sn.histplot(df["ret_Ibov"], kde=True)

#Boxplot 




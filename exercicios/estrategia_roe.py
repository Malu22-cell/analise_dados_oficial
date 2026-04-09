import requests
import pandas as pd 
base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc3MTE5MzIwLCJpYXQiOjE3NzQ1MjczMjAsImp0aSI6ImY1OWE1YTM1MzgwNjQxMzc4MDA1NDBhZDU1ZTNkZTY2IiwidXNlcl9pZCI6IjEyNSJ9.SpCIAGyeyHW_EqevLvBfkJANPFhqO0JuIZqEVph-cXE"
resp = requests.get(
    f"{base_url}/bolsa/planilhao",
    headers={"Authorization": f"Bearer {token}"},
    params={"data_base": "2026-03-23"},
)
dados = resp.json()
df = pd.DataFrame(dados)
maximo = df["roe"].max()
filtro = df["roe"]==maximo
df[filtro]



import requests
import pandas as pd
base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc3MTE5MzIwLCJpYXQiOjE3NzQ1MjczMjAsImp0aSI6ImY1OWE1YTM1MzgwNjQxMzc4MDA1NDBhZDU1ZTNkZTY2IiwidXNlcl9pZCI6IjEyNSJ9.SpCIAGyeyHW_EqevLvBfkJANPFhqO0JuIZqEVph-cXE"
resp = requests.get(
    f"{base_url}/bolsa/planilhao",
    headers={"Authorization": f"Bearer {token}"},
    params={"data_base": "2021-04-01"},
)
dados = resp.json()
df = pd.DataFrame(dados)
df2 = df[["ticker", "roic", "earning_yield"]]
df2['rank_roic'] = df2 ['roic'].rank(ascending=False)
df2['rank_p_ey'] = df2['earning_yield'].rank(ascending=False)
df2["rank_final"] = (df2['rank_roic'] + df2['rank_p_ey']) / 2
carteira = df2.sort_values("rank_final", ascending=False)['ticker'][:20]  

#API para pegar os precos das acoes
base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc3MTE5MzIwLCJpYXQiOjE3NzQ1MjczMjAsImp0aSI6ImY1OWE1YTM1MzgwNjQxMzc4MDA1NDBhZDU1ZTNkZTY2IiwidXNlcl9pZCI6IjEyNSJ9.SpCIAGyeyHW_EqevLvBfkJANPFhqO0JuIZqEVph-cXE"
params = {"ticker" : "BBSE3", "data_ini" : "2001-01-01", "data_fim": "2026-03-31"}
resp = requests.get(
    f"{base_url}/preco/corrigido",
    headers={"Authorization": f"Bearer {token}"},
    params = params,
)
dados = resp.json()
df_preco = pd.DataFrame(dados)
#Preco final``
filtro1 = df_preco["data"] == "2026-03-31"
preco_final = df_preco.loc[filtro1, 'fechamento'].iloc[0]
preco_final = float(preco_final)
#Filtro inicial
filtro2 = df_preco["data"] == "2021-04-01"
precos_inicial = df_preco.loc[filtro2, 'fechamento'].iloc[0]
precos_inicial = float(precos_inicial)
preco_final/precos_inicial - 1


# 5 anos 
# preco final
filtro1 = df_preco["data"]=="2026-03-23"
preco_final = df_preco.loc[filtro1, 'fechamento'].iloc[0]
preco_final = float(preco_final)
#Filtro Inicial
filtro2 = df_preco["data"]=="2021-03-22"
precos_inicial = df_preco.loc[filtro2, 'fechamento'].iloc[0]
precos_inicial = float(precos_inicial)
preco_final/precos_inicial - 1

#API para pegar o Ibov
import yfinance as yf
#Get ticker data
ibov = yf.download("^BVSP", start="2001-01-01", end= "2026-04-01")
filtro1 = ibov.index == "2021-04-01"
ibov_ini = ibov[filtro1]["Close"].iloc[0]
filtro2 = ibov.index == "2026-03-31"
ibov_fim = ibov [filtro2]["Close"].iloc[0]
ibov_fim/ibov_ini - 1
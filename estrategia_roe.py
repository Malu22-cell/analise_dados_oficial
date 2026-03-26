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



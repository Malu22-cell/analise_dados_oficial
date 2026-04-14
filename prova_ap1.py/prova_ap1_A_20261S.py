# O dataset NCR Ride Bookings contém registros de corridas urbanas realizadas em regiões da National Capital Region (NCR), que abrange Delhi, Gurgaon, Noida, Ghaziabad, Faridabad e áreas próximas.
# Utilize os arquivos : ncr_ride_bookings.csv para resolver as questoes.
# Principais informaçoes no dataset:
# Date → Data da corrida
# Time → Horário da corrida
# Booking ID → Identificador da corrida
# Booking Status → Status da corrida
# Customer ID → Identificador do cliente
# Vehicle Type → Tipo de veículo
# Pickup Location → Local de embarque
# Drop Location → Local de desembarque
# Booking Value → Valor da corrida
# Ride Distance → Distância percorrida
# Driver Ratings → Avaliação do motorista
# Customer Rating → Avaliação do cliente
# Payment Method → Método de pagamento
# Questões:
# (0,5) 1 - Quantas corridas estão com Status da Corrida como Completada ("Completed") no dataset? 

import pandas as pd

df = pd.read_csv('ncr_ride_bookings.csv')

corridas_completadas = (df['Booking Status'] == 'Completed').sum()

print(f"Quantidade de corridas completadas: {corridas_completadas}")

# (0,5) 2 - Qual a proporção em relação ao total de corridas?

total_corridas = len(df)

proporcao = corridas_completadas/total_corridas

print(f"Proporção: {proporcao}")
print(f"Porcentagem: {proporcao * 100:.2f}%")

# (0,5) 3 - Calcule a média da Distância ("Ride Distance") percorrida por cada Tipo de veículo.

media_distancia = df.groupby('Vehicle Type')['Ride Distance'].mean()

print(media_distancia)

# (0,5) 4 - Qual o Metodo de Pagamento ("Payment Method") mais utilizado pelas bicicletas ("Bike") ?

metodo_bike = df[df['Vehicle Type'] == 'Bike']['Payment Method'].mode()[0]

print(f"Método mais utilizado pelas bicicletas: {metodo_bike}")

# (0,5) 5 - Qual o valor total arrecadado ("Booking Value") apenas das corridas Completed?

corridas_completed = df[df['Booking Status'] == 'Completed']

valor_total = corridas_completed['Booking Value'].sum()

print(f"Valor total arrecadado: {valor_total}")

# (0,5) 6 - E qual o ticket médio ("Booking Value")dessas corridas Completed?

ticket_medio = corridas_completed['Booking Value'].mean()

print(f"ticket_medio:{ticket_medio}")

# (1,5) 7 - O IPEA disponibiliza uma API pública com diversas séries econômicas. 
# Para encontrar a série de interesse, é necessário primeiro acessar o endpoint de metadados.
# Acesse o endpoint de metadados: "http://www.ipeadata.gov.br/api/odata4/Metadados";
# Transforme em um DataFrame;
# Filtre para encontrar as séries da Fipe relacionadas a venda de imoveis (“vendas - Brasil”).
# Dica: 
# Utilize a coluna FNTSIGLA para encontrar a serie da Fipe;
# Utilize a coluna SERNOME para encontrar as vendas de imoveis no Brasil;

import requests
import pandas as pd

url = "http://www.ipeadata.gov.br/api/odata4/Metadados"
resposta = requests.get(url)
dados = resposta.json()

df = pd.DataFrame(dados["value"])
df["FNTSIGLA"] = df["FNTSIGLA"].astype(str)
df["SERNOME"] = df["SERNOME"].astype(str)
df["SERCODIGO"] = df["SERCODIGO"].astype(str)

fipe = df[df["FNTSIGLA"].str.contains("Fipe", case=False, na=False)]

print(fipe[["SERCODIGO", "FNTSIGLA", "SERNOME"]])

resultado = fipe[fipe["SERCODIGO"].str.contains("VENBR", case=False, na=False)]

print(resultado[["SERCODIGO", "FNTSIGLA", "SERNOME"]])

# (1,5) 8 -  Descubra qual é o código da série correspondente (coluna: SERCODIGO).
# CODIGO_ENCONTRADO=''
# Usando o código encontrado, acesse a API de valores: f"http://ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{CODIGO_ENCONTRADO}')"
# Construa um DataFrame através da chave 'value' do retorno da api
# Selecione apenas as colunas datas (VALDATA) e os valores (VALVALOR).
# Exiba a Data e o Valor que teve o valor maximo de vendas.

import requests
import pandas as pd

CODIGO_ENCONTRADO = "FIPE12_VENBR12"

url = f"http://ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{CODIGO_ENCONTRADO}')"

resposta = requests.get(url)
dados = resposta.json()

df_valores = pd.DataFrame(dados["value"])
df_valores = df_valores[["VALDATA", "VALVALOR"]]
df_valores["VALDATA"] = pd.to_datetime(df_valores["VALDATA"])

linha_max = df_valores.loc[df_valores["VALVALOR"].idxmax()]

print("Data do valor máximo:", linha_max["VALDATA"])
print("Valor máximo:", linha_max["VALVALOR"])


# (1,5) 9 - Descubra quanto rendeu a VALE no ano de 2025
# base_url = "https://laboratoriodefinancas.com/api/v2"
# token = "SEU_JWT"
# params = {"ticker": "VALE3", "data_ini": "2001-01-01", "data_fim": "2026-12-31"}
# response = requests.get(
#     f"{base_url}/preco/corrigido",
#     headers={"Authorization": f"Bearer {token}"},
#     params=params,
# )

import requests
import pandas as pd

base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIj"
params = {
    "ticker": "VALE3",
    "data_ini": "2025-01-01",
    "data_fim": "2025-12-31"
}

response = requests.get(
    f"{base_url}/preco/corrigido",
    headers={"Authorization": f"Bearer {token}"},
    params=params
)

print(response.status_code)
print(response.json())

# (1,5) 10 - Você tem acesso à API do Laboratório de Finanças, que fornece dados do Planilhão em formato JSON. 
# Selecione a empresa do setor de "tecnologia" que apresenta o maior ROE (Return on Equity) na data base 2024-04-01.
# Exiba APENAS AS COLUNAS "ticker", "setor" e o "roe"
# base_url = "https://laboratoriodefinancas.com/api/v2"
# token = "SEU_JWT"
# response = requests.get(
#     f"{base_url}/bolsa/planilhao",
#     headers={"Authorization": f"Bearer {token}"},
#     params={"data_base": "2026-04-01"},
# )

import requests
import pandas as pd

base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIj"
response = requests.get(
    f"{base_url}/bolsa/planilhao",
    headers={"Authorization": f"Bearer {token}"},
    params={"data_base": "2024-04-01"}
)

df = pd.DataFrame(response.json())
tec = df[df["setor"].str.contains("tecnologia", case=False, na=False)]
resultado = tec.loc[[tec["roe"].idxmax()], ["ticker", "setor", "roe"]]

print(resultado)

# (1,5) 11 - Faça a Magic Formula através dos indicadores Return on Capital (roc) e Earning Yield (ey) no dia 2024-04-01.
# Monte uma carteira de investimento com 10 ações baseado na estratégia Magic Formula.
# base_url = "https://laboratoriodefinancas.com/api/v2"
# token = "SEU_JWT"
# response = requests.get(
#     f"{base_url}/bolsa/planilhao",
#     headers={"Authorization": f"Bearer {token}"},
#     params={"data_base": "2026-04-01"},
# )

import requests
import pandas as pd

base_url = "https://laboratoriodefinancas.com/api/v2/bolsa/planilhao"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIj"
response = requests.get(
    f"{base_url}/bolsa/planilhao",
    headers={"Authorization": f"Bearer {token}"},
    params={"data_base": "2024-04-01"}
)

dados = response.json()
df = pd.DataFrame(dados)
mf = df[["ticker", "setor", "roc", "ey"]].copy()
mf["rank_roc"] = mf["roc"].rank(ascending=False, method="min")
mf["rank_ey"] = mf["ey"].rank(ascending=False, method="min")
mf["magic_formula"] = mf["rank_roc"] + mf["rank_ey"]

carteira = mf.sort_values("magic_formula").head(0)

print(carteira[["ticker", "roc", "ey", "rank_roc", "rank_ey", "magic_formula"]])

print(df.columns)

# (1,5) 12 - Quantos setores ("setor") tem essa carteira formada por 10 ações?

carteira = mf.sort_values("magic_formula").head(10)
quantidade_setores = carteira["setor"].nunique()

print(f"A carteira possui {quantidade_setores} setores.")
quantidade_setores = carteira["setor"].nunique()

print(quantidade_setores)
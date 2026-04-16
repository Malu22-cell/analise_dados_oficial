"""
=============================================================
  GABARITO COMPLETO - PREPARAÇÃO PARA PROVA AP1
  Análise de Dados com Python & Pandas
=============================================================
  Tópicos cobertos:
  1. Pandas - Criação, inspeção e seleção
  2. Pandas - Filtros e condições
  3. Pandas - Novas colunas e métricas
  4. Pandas - Groupby e agregações
  5. Pandas - Ordenação e ranking
  6. Listas, dicionários e conversões
  7. API pública (IPEA)
  8. API com autenticação JWT (Lab. de Finanças)
  9. Retorno de ações
  10. ROE / Magic Formula
=============================================================
"""

import pandas as pd
import requests

# =============================================================
# BLOCO 1 — CRIAÇÃO E INSPEÇÃO DE DATAFRAME
# =============================================================
print("\n" + "="*60)
print("BLOCO 1 — CRIAÇÃO E INSPEÇÃO DE DATAFRAME")
print("="*60)

"""
EXERCÍCIO 1
Dataset: vendas de uma loja com colunas produto, categoria, preco, quantidade, regiao.

a) Crie o DataFrame df_loja
b) Mostre as primeiras 5 linhas
c) Mostre o shape (linhas, colunas)
d) Mostre os tipos de dados de cada coluna
e) Mostre estatísticas descritivas (describe)
"""

dados_loja = {
    "produto":    ["Notebook", "Celular", "Tablet", "Monitor", "Teclado", "Mouse", "Headset"],
    "categoria":  ["Computador", "Celular", "Tablet", "Computador", "Acessório", "Acessório", "Acessório"],
    "preco":      [3500, 2200, 1400, 1800, 350, 120, 280],
    "quantidade": [10, 25, 15, 8, 50, 80, 30],
    "regiao":     ["Sul", "Norte", "Sul", "Nordeste", "Norte", "Sul", "Nordeste"],
}

# GABARITO:
df_loja = pd.DataFrame(dados_loja)

print("\na) DataFrame criado:")
print(df_loja)

print("\nb) Primeiras 5 linhas:")
print(df_loja.head())

print("\nc) Shape:")
print(df_loja.shape)

print("\nd) Tipos de dados:")
print(df_loja.dtypes)

print("\ne) Describe:")
print(df_loja.describe())


# =============================================================
# BLOCO 2 — SELEÇÃO DE COLUNAS E LINHAS
# =============================================================
print("\n" + "="*60)
print("BLOCO 2 — SELEÇÃO DE COLUNAS E LINHAS")
print("="*60)

"""
EXERCÍCIO 2
Usando df_loja:

a) Mostre apenas as colunas "produto" e "preco"
b) Mostre a terceira linha (índice 2) com iloc
c) Mostre as linhas de índice 1 até 3
d) Mostre o valor da coluna "preco" na linha 0 com .iloc e .loc
"""

# GABARITO:
print("\na) Colunas produto e preco:")
print(df_loja[["produto", "preco"]])

print("\nb) Terceira linha (índice 2):")
print(df_loja.iloc[2])

print("\nc) Linhas índice 1 até 3:")
print(df_loja.iloc[1:4])

print("\nd) Preço da linha 0 com iloc e loc:")
print("iloc:", df_loja.iloc[0]["preco"])
print("loc: ", df_loja.loc[0, "preco"])


# =============================================================
# BLOCO 3 — FILTROS COM CONDIÇÕES
# =============================================================
print("\n" + "="*60)
print("BLOCO 3 — FILTROS COM CONDIÇÕES")
print("="*60)

"""
EXERCÍCIO 3
Usando df_loja:

a) Filtre produtos com preço acima de 1000
b) Filtre apenas a categoria "Acessório"
c) Filtre produtos com preço > 200 e quantidade > 20
d) Filtre produtos da região "Sul" OU "Norte"
e) Filtre a linha do produto "Notebook"
"""

# GABARITO:
print("\na) Preço acima de 1000:")
print(df_loja[df_loja["preco"] > 1000])

print("\nb) Categoria Acessório:")
print(df_loja[df_loja["categoria"] == "Acessório"])

print("\nc) Preço > 200 e quantidade > 20:")
print(df_loja[(df_loja["preco"] > 200) & (df_loja["quantidade"] > 20)])

print("\nd) Região Sul ou Norte:")
print(df_loja[df_loja["regiao"].isin(["Sul", "Norte"])])

print("\ne) Produto Notebook:")
print(df_loja[df_loja["produto"] == "Notebook"])


# =============================================================
# BLOCO 4 — NOVAS COLUNAS E MÉTRICAS
# =============================================================
print("\n" + "="*60)
print("BLOCO 4 — NOVAS COLUNAS E MÉTRICAS")
print("="*60)

"""
EXERCÍCIO 4
Usando df_loja:

a) Crie a coluna "receita_total" = preco * quantidade
b) Crie a coluna "caro" com True se preco >= 1500
c) Crie a coluna "desconto_10pct" = preco * 0.9
d) Mostre apenas produto, preco, receita_total, caro
"""

# GABARITO:
df_loja["receita_total"]  = df_loja["preco"] * df_loja["quantidade"]
df_loja["caro"]           = df_loja["preco"] >= 1500
df_loja["desconto_10pct"] = df_loja["preco"] * 0.9

print("\na/b/c) DataFrame com novas colunas:")
print(df_loja[["produto", "preco", "receita_total", "caro", "desconto_10pct"]])


# =============================================================
# BLOCO 5 — GROUPBY E AGREGAÇÕES
# =============================================================
print("\n" + "="*60)
print("BLOCO 5 — GROUPBY E AGREGAÇÕES")
print("="*60)

"""
EXERCÍCIO 5
Usando df_loja:

a) Total de receita por categoria
b) Preço médio por região
c) Quantidade total vendida por categoria
d) Resumo completo por região: total_receita, media_preco, qtd_produtos
e) Qual região teve maior receita total?
"""

# GABARITO:
print("\na) Total receita por categoria:")
print(df_loja.groupby("categoria")["receita_total"].sum())

print("\nb) Preço médio por região:")
print(df_loja.groupby("regiao")["preco"].mean())

print("\nc) Quantidade total por categoria:")
print(df_loja.groupby("categoria")["quantidade"].sum())

print("\nd) Resumo completo por região:")
resumo_regiao = df_loja.groupby("regiao").agg(
    total_receita=("receita_total", "sum"),
    media_preco=("preco", "mean"),
    qtd_produtos=("quantidade", "sum")
)
print(resumo_regiao)

print("\ne) Região com maior receita total:")
print(resumo_regiao["total_receita"].idxmax())


# =============================================================
# BLOCO 6 — ORDENAÇÃO E RANKING
# =============================================================
print("\n" + "="*60)
print("BLOCO 6 — ORDENAÇÃO E RANKING")
print("="*60)

"""
EXERCÍCIO 6
Usando df_loja:

a) Ordene por preco crescente
b) Ordene por receita_total decrescente
c) Mostre o top 3 produtos com maior receita_total
d) Mostre produto, preco e receita_total do ranking top 3
"""

# GABARITO:
print("\na) Ordenado por preço crescente:")
print(df_loja.sort_values("preco"))

print("\nb) Ordenado por receita_total decrescente:")
print(df_loja.sort_values("receita_total", ascending=False))

print("\nc/d) Top 3 por receita_total:")
top3 = df_loja.sort_values("receita_total", ascending=False).head(3)
print(top3[["produto", "preco", "receita_total"]])


# =============================================================
# BLOCO 7 — LISTAS, DICIONÁRIOS E CONVERSÕES
# =============================================================
print("\n" + "="*60)
print("BLOCO 7 — LISTAS, DICIONÁRIOS E CONVERSÕES")
print("="*60)

"""
EXERCÍCIO 7
Dado o seguinte dataset de exportações:

a) Qual o tipo da variável dados_export?
b) Quantos registros existem?
c) Quais são as chaves do primeiro dicionário?
d) Liste os países sem repetição
e) Converta para DataFrame chamado df_export
f) Filtre apenas exportações do Brasil
g) Calcule o total exportado por país
h) Converta df_export de volta para lista de dicionários
"""

dados_export = [
    {"pais": "Brasil",    "produto": "Soja",    "valor_usd": 5000, "ano": 2023},
    {"pais": "Brasil",    "produto": "Minério",  "valor_usd": 8000, "ano": 2023},
    {"pais": "Argentina", "produto": "Trigo",    "valor_usd": 3000, "ano": 2023},
    {"pais": "Argentina", "produto": "Soja",    "valor_usd": 4500, "ano": 2023},
    {"pais": "Chile",     "produto": "Cobre",   "valor_usd": 7000, "ano": 2023},
    {"pais": "Brasil",    "produto": "Café",    "valor_usd": 2500, "ano": 2023},
]

# GABARITO:
print("\na) Tipo da variável:")
print(type(dados_export))

print("\nb) Quantidade de registros:")
print(len(dados_export))

print("\nc) Chaves do primeiro dicionário:")
print(list(dados_export[0].keys()))

print("\nd) Países sem repetição:")
paises = list({item["pais"] for item in dados_export})
print(paises)

print("\ne) DataFrame df_export:")
df_export = pd.DataFrame(dados_export)
print(df_export)

print("\nf) Apenas Brasil:")
print(df_export[df_export["pais"] == "Brasil"])

print("\ng) Total exportado por país:")
print(df_export.groupby("pais")["valor_usd"].sum())

print("\nh) Convertido para lista de dicionários:")
print(df_export.to_dict(orient="records"))


# =============================================================
# BLOCO 8 — MANIPULAÇÃO DE LISTAS COM LOOPS
# =============================================================
print("\n" + "="*60)
print("BLOCO 8 — MANIPULAÇÃO DE LISTAS COM LOOPS")
print("="*60)

"""
EXERCÍCIO 8
a) Transforme a coluna "valor_usd" do df_export em uma lista
b) Multiplique cada elemento por 5 (taxa de câmbio fictícia)
c) Crie a coluna "valor_brl" no df_export com esses valores
d) Usando loop for, imprima país e valor_brl de cada linha
e) Crie uma lista apenas com valores acima de 30000 BRL
"""

# GABARITO:
lista_usd = df_export["valor_usd"].tolist()
lista_brl = [v * 5 for v in lista_usd]
df_export["valor_brl"] = lista_brl

print("\na/b/c) Coluna valor_brl adicionada:")
print(df_export[["pais", "produto", "valor_usd", "valor_brl"]])

print("\nd) Loop imprimindo país e valor_brl:")
for _, row in df_export.iterrows():
    print(f"  {row['pais']} - R$ {row['valor_brl']:,.0f}")

print("\ne) Valores acima de R$30.000:")
altos = [v for v in lista_brl if v > 30000]
print(altos)


# =============================================================
# BLOCO 9 — API PÚBLICA: IPEA
# =============================================================
print("\n" + "="*60)
print("BLOCO 9 — API PÚBLICA: IPEA")
print("="*60)

"""
EXERCÍCIO 9
Similar à questão 7 e 8 da prova AP1.

PARTE A — Buscar metadados e filtrar série:
  - Endpoint: "http://www.ipeadata.gov.br/api/odata4/Metadados"
  - Filtre pela coluna FNTSIGLA == "FGV" (ou "FIPE")
  - Filtre pela coluna SERNOME contendo "IGP" (ou outro termo)
  - Descubra o SERCODIGO da série

PARTE B — Buscar valores da série:
  - Use o SERCODIGO encontrado para acessar os valores
  - Endpoint: f"http://ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{codigo}')"
  - Construa DataFrame com a chave 'value' do retorno
  - Selecione colunas VALDATA e VALVALOR
  - Exiba a data e valor do pico máximo
"""

# GABARITO COMPLETO:

# PARTE A — Metadados
print("\nPARTE A — Buscando metadados do IPEA...")
try:
    resp_meta = requests.get(
        "http://www.ipeadata.gov.br/api/odata4/Metadados",
        timeout=20
    )
    df_meta = pd.DataFrame(resp_meta.json()["value"])

    print("Colunas disponíveis:", df_meta.columns.tolist())
    print("Shape:", df_meta.shape)

    # Filtrando série FIPE de vendas de imóveis (como na prova)
    df_fipe = df_meta[df_meta["FNTSIGLA"] == "FIPE"]
    df_vendas_imoveis = df_fipe[
        df_fipe["SERNOME"].str.contains("vendas", case=False, na=False)
    ]
    print("\nSéries FIPE de vendas encontradas:")
    print(df_vendas_imoveis[["SERCODIGO", "SERNOME"]].head(10))

    # Pegando o código
    if not df_vendas_imoveis.empty:
        codigo_encontrado = df_vendas_imoveis.iloc[0]["SERCODIGO"]
        print(f"\nCódigo encontrado: {codigo_encontrado}")

        # PARTE B — Valores da série
        print("\nPARTE B — Buscando valores da série...")
        resp_valores = requests.get(
            f"http://ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{codigo_encontrado}')",
            timeout=30
        )
        df_valores = pd.DataFrame(resp_valores.json()["value"])
        df_valores = df_valores[["VALDATA", "VALVALOR"]]

        print("Primeiras linhas:")
        print(df_valores.head())

        # Pico máximo
        idx_max = df_valores["VALVALOR"].idxmax()
        print("\nData e valor do pico máximo:")
        print(df_valores.loc[idx_max])
    else:
        print("Nenhuma série encontrada com esse filtro.")
except Exception as e:
    print(f"Erro na requisição IPEA: {e}")


# =============================================================
# BLOCO 10 — API COM JWT: LABORATÓRIO DE FINANÇAS
# =============================================================
print("\n" + "="*60)
print("BLOCO 10 — API COM JWT: LABORATÓRIO DE FINANÇAS")
print("="*60)

"""
EXERCÍCIO 10 — Retorno de ação no período
Similar à questão 9 da prova:
  - Buscar preço corrigido de uma ação (ex: PETR4)
  - Calcular o retorno percentual em um ano específico (ex: 2024)
"""

# GABARITO:
base_url = "https://laboratoriodefinancas.com/api/v2"
token = "SEU_JWT_AQUI"  # Substitua pelo seu token

print("\nEXERCÍCIO 10A — Retorno anual de uma ação:")
print("""
# Estrutura do código para calcular retorno de PETR4 em 2024:

import requests
import pandas as pd

base_url = "https://laboratoriodefinancas.com/api/v2"
token = "SEU_JWT"

resp = requests.get(
    f"{base_url}/preco/corrigido",
    headers={"Authorization": f"Bearer {token}"},
    params={"ticker": "PETR4", "data_ini": "2024-01-01", "data_fim": "2024-12-31"},
)

df = pd.DataFrame(resp.json()["data"])  # ajuste a chave conforme retorno real
df["data"] = pd.to_datetime(df["data"])
df = df.sort_values("data")

preco_inicial = df.iloc[0]["preco"]
preco_final   = df.iloc[-1]["preco"]
retorno       = (preco_final / preco_inicial - 1) * 100

print(f"Retorno de PETR4 em 2024: {retorno:.2f}%")
""")


# =============================================================
# BLOCO 11 — ROE: MAIOR RETURN ON EQUITY POR SETOR
# =============================================================
print("\n" + "="*60)
print("BLOCO 11 — ROE: MAIOR RETURN ON EQUITY POR SETOR")
print("="*60)

"""
EXERCÍCIO 11 — Similar à questão 10 da prova:
  - Acessar o Planilhão do Lab. de Finanças
  - Filtrar setor de "tecnologia"
  - Encontrar a empresa com maior ROE
  - Exibir apenas colunas ticker, setor, roe
"""

print("""
# Código completo para encontrar maior ROE no setor de tecnologia:

import requests
import pandas as pd

base_url = "https://laboratoriodefinancas.com/api/v2"
token = "SEU_JWT"

resp = requests.get(
    f"{base_url}/bolsa/planilhao",
    headers={"Authorization": f"Bearer {token}"},
    params={"data_base": "2026-04-01"},
)

df_planilhao = pd.DataFrame(resp.json()["data"])  # ajuste a chave conforme retorno

# Filtra tecnologia
df_tech = df_planilhao[df_planilhao["setor"].str.lower() == "tecnologia"]

# Remove nulos no ROE
df_tech = df_tech.dropna(subset=["roe"])

# Empresa com maior ROE
idx_max_roe = df_tech["roe"].idxmax()
empresa_maior_roe = df_tech.loc[idx_max_roe, ["ticker", "setor", "roe"]]

print(empresa_maior_roe)
""")


# =============================================================
# BLOCO 12 — MAGIC FORMULA (ROC + EY)
# =============================================================
print("\n" + "="*60)
print("BLOCO 12 — MAGIC FORMULA (ROC + EY)")
print("="*60)

"""
EXERCÍCIO 12 — Similar à questão 11 da prova:
  - Usar o Planilhão com ROC (Return on Capital) e EY (Earning Yield)
  - Ranquear as ações por ROC (melhor = maior) e EY (melhor = maior)
  - Somar os rankings e pegar as 10 melhores
  - Mostrar quantos setores distintos tem a carteira
"""

print("""
# Código completo da Magic Formula:

import requests
import pandas as pd

base_url = "https://laboratoriodefinancas.com/api/v2"
token = "SEU_JWT"

resp = requests.get(
    f"{base_url}/bolsa/planilhao",
    headers={"Authorization": f"Bearer {token}"},
    params={"data_base": "2026-04-01"},
)

df = pd.DataFrame(resp.json()["data"])  # ajuste a chave conforme retorno

# Remove linhas sem roc ou ey
df = df.dropna(subset=["roc", "ey"])

# Ranking: quanto MAIOR o roc e ey, MELHOR a posição (rank ascending=False → rank 1 = maior)
df["rank_roc"] = df["roc"].rank(ascending=False)
df["rank_ey"]  = df["ey"].rank(ascending=False)

# Score final = soma dos dois rankings (quanto menor, melhor)
df["score_magic"] = df["rank_roc"] + df["rank_ey"]

# Top 10 (menor score = melhor combinação)
carteira = df.sort_values("score_magic").head(10)

print("Carteira Magic Formula (Top 10):")
print(carteira[["ticker", "setor", "roc", "ey", "score_magic"]])

# Questão 12: Quantos setores distintos na carteira?
qtd_setores = carteira["setor"].nunique()
print(f"\\nQuantidade de setores na carteira: {qtd_setores}")
print(f"Setores: {carteira['setor'].unique().tolist()}")
""")


# =============================================================
# BLOCO 13 — SIMULADO COMPLETO NO ESTILO DA PROVA
# =============================================================
print("\n" + "="*60)
print("BLOCO 13 — SIMULADO NO ESTILO DA PROVA AP1")
print("="*60)

"""
DATASET FICTÍCIO: Corridas de Aplicativo (similar ao NCR Ride Bookings da prova)

Colunas:
  - booking_id       → ID da corrida
  - status           → Status: "Completed", "Cancelled", "Pending"
  - vehicle_type     → "Car", "Bike", "Auto"
  - payment_method   → "Cash", "Card", "Pix"
  - booking_value    → Valor da corrida (R$)
  - ride_distance    → Distância percorrida (km)
  - driver_rating    → Avaliação do motorista (1-5)
  - customer_rating  → Avaliação do cliente (1-5)
"""

dados_corridas = {
    "booking_id":      [f"BK{str(i).zfill(3)}" for i in range(1, 21)],
    "status":          ["Completed", "Completed", "Cancelled", "Completed", "Pending",
                        "Completed", "Cancelled", "Completed", "Completed", "Cancelled",
                        "Completed", "Completed", "Pending", "Completed", "Completed",
                        "Cancelled", "Completed", "Completed", "Pending", "Completed"],
    "vehicle_type":    ["Car", "Bike", "Car", "Auto", "Bike",
                        "Car", "Auto", "Bike", "Car", "Car",
                        "Bike", "Auto", "Car", "Car", "Bike",
                        "Auto", "Car", "Bike", "Car", "Auto"],
    "payment_method":  ["Card", "Pix", "Cash", "Card", "Pix",
                        "Pix", "Card", "Cash", "Card", "Pix",
                        "Pix", "Cash", "Card", "Card", "Pix",
                        "Cash", "Pix", "Card", "Cash", "Pix"],
    "booking_value":   [45.0, 18.0, 60.0, 30.0, 12.0,
                        80.0, 25.0, 22.0, 55.0, 40.0,
                        15.0, 35.0, 70.0, 90.0, 20.0,
                        28.0, 65.0, 17.0, 50.0, 38.0],
    "ride_distance":   [8.5, 3.2, 12.0, 5.0, 2.1,
                        15.3, 4.5, 4.0, 9.8, 7.2,
                        2.8, 6.1, 13.5, 18.0, 3.5,
                        5.3, 11.0, 3.0, 9.0, 6.8],
    "driver_rating":   [4.5, 4.0, 3.5, 5.0, 4.2,
                        4.8, 3.0, 4.1, 4.7, 3.8,
                        4.3, 4.6, 3.9, 5.0, 4.4,
                        3.2, 4.9, 4.0, 3.7, 4.5],
    "customer_rating": [4.0, 3.5, 4.5, 4.8, 3.0,
                        5.0, 3.8, 4.2, 4.6, 3.5,
                        3.9, 4.7, 4.1, 5.0, 3.6,
                        3.3, 4.8, 3.7, 4.0, 4.4],
}

df_corridas = pd.DataFrame(dados_corridas)

# --- Questão S1 (0,5 pt) ---
# Quantas corridas estão com status "Completed"?
print("\nQ1 — Corridas com status Completed:")
q1 = df_corridas[df_corridas["status"] == "Completed"]["booking_id"].count()
print(q1)

# --- Questão S2 (0,5 pt) ---
# Qual a proporção de corridas Completed em relação ao total?
print("\nQ2 — Proporção de Completed:")
q2 = q1 / len(df_corridas)
print(f"{q2:.2%}")

# --- Questão S3 (0,5 pt) ---
# Calcule a média da distância percorrida por tipo de veículo
print("\nQ3 — Média da distância por tipo de veículo:")
q3 = df_corridas.groupby("vehicle_type")["ride_distance"].mean()
print(q3)

# --- Questão S4 (0,5 pt) ---
# Qual o método de pagamento mais usado pelas Bikes?
print("\nQ4 — Método mais usado pelas Bikes:")
df_bikes = df_corridas[df_corridas["vehicle_type"] == "Bike"]
q4 = df_bikes["payment_method"].value_counts().idxmax()
print(q4)

# --- Questão S5 (0,5 pt) ---
# Qual o valor total arrecadado nas corridas Completed?
print("\nQ5 — Total arrecadado nas corridas Completed:")
df_completed = df_corridas[df_corridas["status"] == "Completed"]
q5 = df_completed["booking_value"].sum()
print(f"R$ {q5:.2f}")

# --- Questão S6 (0,5 pt) ---
# Qual o ticket médio das corridas Completed?
print("\nQ6 — Ticket médio das corridas Completed:")
q6 = df_completed["booking_value"].mean()
print(f"R$ {q6:.2f}")

# --- BÔNUS: Questões extras de análise ---
print("\nBÔNUS — Análise extra:")

# Qual veículo tem maior avaliação média de motorista?
print("\nAvaliação média do motorista por veículo:")
print(df_corridas.groupby("vehicle_type")["driver_rating"].mean().sort_values(ascending=False))

# Qual forma de pagamento tem o maior ticket médio?
print("\nTicket médio por método de pagamento:")
print(df_corridas.groupby("payment_method")["booking_value"].mean().sort_values(ascending=False))

# Top 3 corridas mais caras com status Completed
print("\nTop 3 corridas mais caras (Completed):")
top3_corridas = df_completed.sort_values("booking_value", ascending=False).head(3)
print(top3_corridas[["booking_id", "vehicle_type", "booking_value"]])


# =============================================================
# BLOCO 14 — RESUMO DOS PADRÕES DE CÓDIGO MAIS COBRADOS
# =============================================================
print("\n" + "="*60)
print("BLOCO 14 — COLA RÁPIDA: PADRÕES MAIS COBRADOS NA PROVA")
print("="*60)

print("""
# ── CRIAR DATAFRAME ──────────────────────────────────────────
df = pd.DataFrame(dicionario)
df = pd.DataFrame(lista_de_dicts)

# ── INSPECIONAR ──────────────────────────────────────────────
df.head()           # primeiras linhas
df.shape            # (linhas, colunas)
df.dtypes           # tipos de cada coluna
df.describe()       # estatísticas descritivas
df.columns          # nomes das colunas

# ── SELECIONAR ───────────────────────────────────────────────
df["coluna"]                    # uma coluna
df[["col1", "col2"]]            # múltiplas colunas
df.iloc[0]                      # linha por índice numérico
df.iloc[2:5]                    # linhas 2 até 4
df.loc[0, "coluna"]             # linha e coluna por nome

# ── FILTROS ──────────────────────────────────────────────────
df[df["col"] > 1000]
df[df["col"] == "valor"]
df[(df["col1"] > 100) & (df["col2"] == "X")]    # E
df[(df["col1"] > 100) | (df["col2"] == "X")]    # OU
df[df["col"].isin(["A", "B"])]
df[df["col"].str.contains("texto", case=False, na=False)]

# ── NOVAS COLUNAS ────────────────────────────────────────────
df["nova"] = df["a"] * df["b"]
df["flag"] = df["preco"] >= 1000           # coluna booleana

# ── AGREGAÇÕES ───────────────────────────────────────────────
df["col"].sum()
df["col"].mean()
df["col"].count()
df["col"].value_counts()                   # frequência de cada valor
df["col"].value_counts().idxmax()          # valor mais frequente
df["col"].idxmax()                         # índice do máximo
df["col"].nunique()                        # qtd de valores únicos

# ── GROUPBY ──────────────────────────────────────────────────
df.groupby("cat")["val"].sum()
df.groupby("cat")["val"].mean()
df.groupby("cat").agg(
    total=("val", "sum"),
    media=("val", "mean"),
    contagem=("val", "count")
)

# ── ORDENAÇÃO ────────────────────────────────────────────────
df.sort_values("col")                        # crescente
df.sort_values("col", ascending=False)       # decrescente
df.sort_values("col", ascending=False).head(10)  # top 10

# ── RANKING (MAGIC FORMULA) ──────────────────────────────────
df["rank_col"] = df["col"].rank(ascending=False)  # rank 1 = maior valor

# ── CONVERSÕES ───────────────────────────────────────────────
df.to_dict(orient="records")    # DataFrame → lista de dicts
df.to_dict(orient="list")       # DataFrame → dict de listas
df["col"].tolist()              # coluna → lista Python

# ── API REST ─────────────────────────────────────────────────
import requests

# Sem autenticação (IPEA):
resp = requests.get("https://url.com/endpoint", params={"chave": "valor"})
df = pd.DataFrame(resp.json()["value"])

# Com JWT (Lab. Finanças):
resp = requests.get(
    f"{base_url}/rota",
    headers={"Authorization": f"Bearer {token}"},
    params={"param": "valor"},
)
df = pd.DataFrame(resp.json()["data"])  # ajuste a chave conforme API

# ── MÁXIMO / MÍNIMO COM LOCALIZAÇÃO ──────────────────────────
idx_max = df["col"].idxmax()
print(df.loc[idx_max])          # linha completa do máximo
""")

print("\n" + "="*60)
print("FIM DO GABARITO — BOA PROVA! 🎯")
print("="*60)
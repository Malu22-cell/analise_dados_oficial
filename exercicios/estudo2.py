"""
╔══════════════════════════════════════════════════════════════╗
║           SIMULADO AP1 — ANÁLISE DE DADOS COM PYTHON         ║
║                    >>> SEM GABARITO <<<                      ║
╠══════════════════════════════════════════════════════════════╣
║  Total: 10 pontos                                            ║
║  Dataset: Brazil E-Commerce Orders (inspirado em Olist)      ║
║  Instruções: resolva cada questão e valide com print()       ║
╚══════════════════════════════════════════════════════════════╝

CONTEXTO DO DATASET:
  O dataset contém pedidos de um e-commerce brasileiro com as colunas:
  - order_id          → ID único do pedido
  - order_status      → Status: "delivered", "canceled", "shipped", "processing"
  - payment_type      → Tipo de pagamento: "credit_card", "boleto", "pix", "voucher"
  - product_category  → Categoria do produto
  - order_value       → Valor do pedido (R$)
  - freight_value     → Valor do frete (R$)
  - review_score      → Nota do cliente (1 a 5)
  - seller_state      → Estado do vendedor (UF)
  - delivery_days     → Dias para entrega
"""

import pandas as pd
import requests

# ──────────────────────────────────────────────
# DATASET — não altere este bloco
# ──────────────────────────────────────────────
import random
random.seed(42)

dados_ecommerce = {
    "order_id": [f"ORD{str(i).zfill(4)}" for i in range(1, 31)],
    "order_status": [
        "delivered","delivered","canceled","delivered","shipped",
        "delivered","canceled","delivered","delivered","processing",
        "delivered","delivered","canceled","delivered","delivered",
        "shipped","delivered","delivered","processing","delivered",
        "canceled","delivered","delivered","shipped","delivered",
        "delivered","canceled","delivered","delivered","delivered",
    ],
    "payment_type": [
        "credit_card","boleto","credit_card","pix","boleto",
        "pix","credit_card","boleto","credit_card","pix",
        "pix","voucher","credit_card","credit_card","boleto",
        "credit_card","pix","boleto","credit_card","pix",
        "boleto","credit_card","pix","credit_card","boleto",
        "pix","credit_card","boleto","credit_card","pix",
    ],
    "product_category": [
        "eletronicos","moda","eletronicos","beleza","casa",
        "eletronicos","moda","casa","eletronicos","beleza",
        "moda","casa","eletronicos","beleza","moda",
        "eletronicos","casa","moda","beleza","eletronicos",
        "casa","moda","eletronicos","beleza","casa",
        "eletronicos","moda","beleza","casa","eletronicos",
    ],
    "order_value": [
        350.0, 89.9, 520.0, 45.0, 210.0,
        780.0, 130.0, 310.0, 430.0, 67.0,
        95.0, 180.0, 640.0, 55.0, 112.0,
        890.0, 260.0, 75.0, 490.0, 340.0,
        200.0, 145.0, 710.0, 38.0, 295.0,
        560.0, 170.0, 83.0, 415.0, 920.0,
    ],
    "freight_value": [
        18.0, 12.5, 25.0, 8.0, 15.0,
        30.0, 10.0, 20.0, 22.0, 9.0,
        11.0, 17.0, 28.0, 7.0, 13.0,
        35.0, 19.0, 10.5, 24.0, 16.0,
        14.0, 11.5, 32.0, 6.0, 18.5,
        27.0, 12.0, 9.5, 21.0, 38.0,
    ],
    "review_score": [
        5, 4, 1, 5, 3,
        5, 2, 4, 5, 3,
        4, 4, 1, 5, 3,
        5, 4, 3, 2, 5,
        1, 4, 5, 3, 4,
        5, 2, 4, 4, 5,
    ],
    "seller_state": [
        "SP","RJ","SP","MG","SP",
        "RS","SP","RJ","SP","MG",
        "SP","RS","SP","RJ","MG",
        "SP","SP","RJ","MG","SP",
        "RS","SP","SP","MG","RJ",
        "SP","SP","RS","MG","SP",
    ],
    "delivery_days": [
        7, 12, 0, 5, 0,
        9, 0, 14, 8, 0,
        11, 6, 0, 4, 10,
        0, 13, 7, 0, 6,
        0, 9, 5, 0, 11,
        8, 0, 12, 7, 4,
    ],
}

df = pd.DataFrame(dados_ecommerce)


# ══════════════════════════════════════════════════════════════
# PARTE 1 — ANÁLISE DO DATASET (6 x 0,5 pt = 3,0 pts)
# ══════════════════════════════════════════════════════════════

# (0,5) QUESTÃO 1
# Quantos pedidos têm status "delivered" no dataset?


# (0,5) QUESTÃO 2
# Qual a proporção de pedidos "delivered" em relação ao total?
# Exiba o resultado em formato percentual (ex: 66.67%)


# (0,5) QUESTÃO 3
# Calcule a média do valor do pedido ("order_value") por categoria de produto ("product_category").
# Ordene do maior para o menor.


# (0,5) QUESTÃO 4
# Qual o tipo de pagamento ("payment_type") mais utilizado nos pedidos com status "delivered"?


# (0,5) QUESTÃO 5
# Qual o valor total arrecadado ("order_value") apenas nos pedidos com status "delivered"?


# (0,5) QUESTÃO 6
# Qual o ticket médio ("order_value") dos pedidos "delivered"?
# E qual a nota média de avaliação ("review_score") desses pedidos?


# ══════════════════════════════════════════════════════════════
# PARTE 2 — API PÚBLICA: IPEA (1,5 pt)
# ══════════════════════════════════════════════════════════════

# (1,5) QUESTÃO 7
# O IPEA disponibiliza uma API pública com séries econômicas.
#
# PASSO A:
#   - Acesse o endpoint de metadados: "http://www.ipeadata.gov.br/api/odata4/Metadados"
#   - Transforme o retorno (chave "value") em um DataFrame chamado df_meta
#   - Filtre as séries do Banco Central do Brasil: coluna FNTSIGLA == "BCB"
#   - Dentro dessas, encontre séries relacionadas à "Taxa Selic" usando a coluna SERNOME
#   - Exiba as colunas SERCODIGO e SERNOME das séries encontradas
#
# PASSO B:
#   - Pegue o SERCODIGO da primeira série encontrada
#   - Acesse os valores: f"http://ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{codigo}')"
#   - Construa um DataFrame com a chave "value" do retorno
#   - Selecione apenas as colunas VALDATA e VALVALOR
#   - Exiba a data e o valor do ponto MÁXIMO da série


# ══════════════════════════════════════════════════════════════
# PARTE 3 — API COM JWT: LABORATÓRIO DE FINANÇAS (4,0 pts)
# ══════════════════════════════════════════════════════════════

base_url = "https://laboratoriodefinancas.com/api/v2"
token = "SEU_JWT_AQUI"  # substitua pelo seu token

# (1,0) QUESTÃO 8
# Descubra quanto rendeu a ação ITUB4 no ano de 2024.
# Use o endpoint /preco/corrigido com os parâmetros:
#   ticker    = "ITUB4"
#   data_ini  = "2024-01-01"
#   data_fim  = "2024-12-31"
#
# Calcule o retorno percentual:
#   retorno = (preco_final / preco_inicial - 1) * 100
# Exiba o resultado formatado: "Retorno de ITUB4 em 2024: XX.XX%"


# (1,0) QUESTÃO 9
# Acesse o Planilhão via endpoint /bolsa/planilhao com data_base = "2026-04-01"
# Filtre as empresas do setor "financeiro"
# Encontre a empresa com o MAIOR P/L (coluna "pl")
# Exiba apenas as colunas: ticker, setor, pl


# (1,0) QUESTÃO 10
# Usando o mesmo Planilhão (data_base = "2026-04-01"):
# Monte uma carteira com a estratégia Greenblatt Magic Formula:
#   - Use os indicadores ROC (roc) e Earning Yield (ey)
#   - Remova linhas com valores nulos em roc ou ey
#   - Crie um ranking para cada indicador (rank 1 = maior valor)
#   - Some os rankings para obter o score_magic
#   - Selecione as 10 ações com MENOR score_magic (melhor combinação)
#   - Exiba: ticker, setor, roc, ey, score_magic


# (1,0) QUESTÃO 11 — EXTRA/DESAFIO
# Usando a carteira da Magic Formula formada na questão 10:
#   a) Quantos setores distintos ela possui?
#   b) Qual o setor com mais ações na carteira?
#   c) Qual a média do ROC das 10 ações selecionadas?
"""
FIM DO SIMULADO
"""


"""
╔══════════════════════════════════════════════════════════════╗
║           SIMULADO AP1 — ANÁLISE DE DADOS COM PYTHON         ║
║                  >>> GABARITO COMPLETO <<<                   ║
╠══════════════════════════════════════════════════════════════╣
║  Total: 10 pontos                                            ║
║  Dataset: Brazil E-Commerce Orders (inspirado em Olist)      ║
╚══════════════════════════════════════════════════════════════╝
"""

import pandas as pd
import requests

# ──────────────────────────────────────────────
# DATASET — não altere este bloco
# ──────────────────────────────────────────────
dados_ecommerce = {
    "order_id": [f"ORD{str(i).zfill(4)}" for i in range(1, 31)],
    "order_status": [
        "delivered","delivered","canceled","delivered","shipped",
        "delivered","canceled","delivered","delivered","processing",
        "delivered","delivered","canceled","delivered","delivered",
        "shipped","delivered","delivered","processing","delivered",
        "canceled","delivered","delivered","shipped","delivered",
        "delivered","canceled","delivered","delivered","delivered",
    ],
    "payment_type": [
        "credit_card","boleto","credit_card","pix","boleto",
        "pix","credit_card","boleto","credit_card","pix",
        "pix","voucher","credit_card","credit_card","boleto",
        "credit_card","pix","boleto","credit_card","pix",
        "boleto","credit_card","pix","credit_card","boleto",
        "pix","credit_card","boleto","credit_card","pix",
    ],
    "product_category": [
        "eletronicos","moda","eletronicos","beleza","casa",
        "eletronicos","moda","casa","eletronicos","beleza",
        "moda","casa","eletronicos","beleza","moda",
        "eletronicos","casa","moda","beleza","eletronicos",
        "casa","moda","eletronicos","beleza","casa",
        "eletronicos","moda","beleza","casa","eletronicos",
    ],
    "order_value": [
        350.0, 89.9, 520.0, 45.0, 210.0,
        780.0, 130.0, 310.0, 430.0, 67.0,
        95.0, 180.0, 640.0, 55.0, 112.0,
        890.0, 260.0, 75.0, 490.0, 340.0,
        200.0, 145.0, 710.0, 38.0, 295.0,
        560.0, 170.0, 83.0, 415.0, 920.0,
    ],
    "freight_value": [
        18.0, 12.5, 25.0, 8.0, 15.0,
        30.0, 10.0, 20.0, 22.0, 9.0,
        11.0, 17.0, 28.0, 7.0, 13.0,
        35.0, 19.0, 10.5, 24.0, 16.0,
        14.0, 11.5, 32.0, 6.0, 18.5,
        27.0, 12.0, 9.5, 21.0, 38.0,
    ],
    "review_score": [
        5, 4, 1, 5, 3,
        5, 2, 4, 5, 3,
        4, 4, 1, 5, 3,
        5, 4, 3, 2, 5,
        1, 4, 5, 3, 4,
        5, 2, 4, 4, 5,
    ],
    "seller_state": [
        "SP","RJ","SP","MG","SP",
        "RS","SP","RJ","SP","MG",
        "SP","RS","SP","RJ","MG",
        "SP","SP","RJ","MG","SP",
        "RS","SP","SP","MG","RJ",
        "SP","SP","RS","MG","SP",
    ],
    "delivery_days": [
        7, 12, 0, 5, 0,
        9, 0, 14, 8, 0,
        11, 6, 0, 4, 10,
        0, 13, 7, 0, 6,
        0, 9, 5, 0, 11,
        8, 0, 12, 7, 4,
    ],
}

df = pd.DataFrame(dados_ecommerce)
print("Dataset carregado com sucesso!")
print(f"Shape: {df.shape}")
print(df.head())


# ══════════════════════════════════════════════════════════════
# PARTE 1 — ANÁLISE DO DATASET (6 x 0,5 pt = 3,0 pts)
# ══════════════════════════════════════════════════════════════

print("\n" + "="*60)
print("PARTE 1 — ANÁLISE DO DATASET")
print("="*60)


# ──────────────────────────────────────────────────────────────
# QUESTÃO 1 (0,5 pt)
# Quantos pedidos têm status "delivered" no dataset?
# ──────────────────────────────────────────────────────────────
print("\n--- QUESTÃO 1 ---")

# RESPOSTA:
q1 = df[df["order_status"] == "delivered"]["order_id"].count()
# Alternativa igualmente válida:
# q1 = len(df[df["order_status"] == "delivered"])
# q1 = df["order_status"].value_counts()["delivered"]

print(f"Pedidos com status 'delivered': {q1}")
# Resultado esperado: 21


# ──────────────────────────────────────────────────────────────
# QUESTÃO 2 (0,5 pt)
# Qual a proporção de pedidos "delivered" em relação ao total?
# ──────────────────────────────────────────────────────────────
print("\n--- QUESTÃO 2 ---")

# RESPOSTA:
total = len(df)
proporcao = q1 / total
print(f"Proporção de 'delivered': {proporcao:.2%}")
# Resultado esperado: 70.00%

# Alternativa com uma linha só:
print(df["order_status"].value_counts(normalize=True).map("{:.2%}".format))


# ──────────────────────────────────────────────────────────────
# QUESTÃO 3 (0,5 pt)
# Calcule a média do order_value por product_category,
# ordenada do maior para o menor.
# ──────────────────────────────────────────────────────────────
print("\n--- QUESTÃO 3 ---")

# RESPOSTA:
media_por_categoria = (
    df.groupby("product_category")["order_value"]
    .mean()
    .sort_values(ascending=False)
)
print("Média de order_value por categoria (maior → menor):")
print(media_por_categoria)


# ──────────────────────────────────────────────────────────────
# QUESTÃO 4 (0,5 pt)
# Qual o payment_type mais usado nos pedidos "delivered"?
# ──────────────────────────────────────────────────────────────
print("\n--- QUESTÃO 4 ---")

# RESPOSTA:
df_delivered = df[df["order_status"] == "delivered"]   # filtra delivered
pagamento_mais_usado = df_delivered["payment_type"].value_counts().idxmax()

print(f"Pagamento mais usado nos pedidos delivered: {pagamento_mais_usado}")
print("\nContagem completa:")
print(df_delivered["payment_type"].value_counts())


# ──────────────────────────────────────────────────────────────
# QUESTÃO 5 (0,5 pt)
# Qual o valor total arrecadado nos pedidos "delivered"?
# ──────────────────────────────────────────────────────────────
print("\n--- QUESTÃO 5 ---")

# RESPOSTA:
total_arrecadado = df_delivered["order_value"].sum()
print(f"Total arrecadado (delivered): R$ {total_arrecadado:,.2f}")


# ──────────────────────────────────────────────────────────────
# QUESTÃO 6 (0,5 pt)
# Ticket médio e nota média dos pedidos "delivered"
# ──────────────────────────────────────────────────────────────
print("\n--- QUESTÃO 6 ---")

# RESPOSTA:
ticket_medio = df_delivered["order_value"].mean()
nota_media   = df_delivered["review_score"].mean()

print(f"Ticket médio (delivered): R$ {ticket_medio:.2f}")
print(f"Nota média (delivered):   {nota_media:.2f}")


# ══════════════════════════════════════════════════════════════
# PARTE 2 — API PÚBLICA: IPEA (1,5 pt)
# ══════════════════════════════════════════════════════════════

print("\n" + "="*60)
print("PARTE 2 — API PÚBLICA: IPEA")
print("="*60)


# ──────────────────────────────────────────────────────────────
# QUESTÃO 7 (1,5 pt)
# PASSO A: metadados → filtrar série do BCB sobre Selic
# PASSO B: buscar valores → exibir data e valor do pico máximo
# ──────────────────────────────────────────────────────────────
print("\n--- QUESTÃO 7 ---")

# RESPOSTA — PASSO A:
print("Buscando metadados do IPEA...")
try:
    resp_meta = requests.get(
        "http://www.ipeadata.gov.br/api/odata4/Metadados",
        timeout=30,
    )
    df_meta = pd.DataFrame(resp_meta.json()["value"])

    print(f"Metadados carregados. Shape: {df_meta.shape}")

    # Filtra BCB
    df_bcb = df_meta[df_meta["FNTSIGLA"] == "BCB"]

    # Filtra séries com "Selic" no nome
    df_selic = df_bcb[
        df_bcb["SERNOME"].str.contains("Selic", case=False, na=False)
    ]

    print("\nSéries do BCB relacionadas à Selic:")
    print(df_selic[["SERCODIGO", "SERNOME"]].head(10))

    # PASSO B: pega o primeiro código e busca valores
    if not df_selic.empty:
        codigo = df_selic.iloc[0]["SERCODIGO"]
        print(f"\nCódigo selecionado: {codigo}")

        resp_valores = requests.get(
            f"http://ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{codigo}')",
            timeout=30,
        )
        df_valores = pd.DataFrame(resp_valores.json()["value"])
        df_valores = df_valores[["VALDATA", "VALVALOR"]]
        df_valores = df_valores.dropna(subset=["VALVALOR"])

        print("\nPrimeiras linhas dos valores:")
        print(df_valores.head())

        # Linha do pico máximo
        idx_max = df_valores["VALVALOR"].idxmax()
        print("\nData e valor do pico máximo:")
        print(df_valores.loc[idx_max])

except Exception as e:
    print(f"Erro na requisição IPEA: {e}")
    print("(Verifique sua conexão com a internet)")


# ══════════════════════════════════════════════════════════════
# PARTE 3 — API COM JWT: LABORATÓRIO DE FINANÇAS (4,0 pts)
# ══════════════════════════════════════════════════════════════

print("\n" + "="*60)
print("PARTE 3 — API LABORATÓRIO DE FINANÇAS (JWT)")
print("="*60)

base_url = "https://laboratoriodefinancas.com/api/v2"
token    = "SEU_JWT_AQUI"   # <-- substitua pelo seu token real

HEADERS  = {"Authorization": f"Bearer {token}"}


# ──────────────────────────────────────────────────────────────
# QUESTÃO 8 (1,0 pt)
# Retorno de ITUB4 no ano de 2024
# ──────────────────────────────────────────────────────────────
print("\n--- QUESTÃO 8 ---")

# RESPOSTA:
try:
    resp = requests.get(
        f"{base_url}/preco/corrigido",
        headers=HEADERS,
        params={
            "ticker":   "ITUB4",
            "data_ini": "2024-01-01",
            "data_fim": "2024-12-31",
        },
        timeout=20,
    )

    # O retorno da API costuma vir em uma chave como "data" ou "prices"
    # Ajuste conforme o retorno real da sua API:
    dados_preco = resp.json()

    # Se vier numa lista direta:
    df_itub4 = pd.DataFrame(dados_preco)

    # Se vier numa chave "data":
    # df_itub4 = pd.DataFrame(dados_preco["data"])

    # Ordena por data para garantir a ordem cronológica
    df_itub4["data"] = pd.to_datetime(df_itub4["data"])
    df_itub4 = df_itub4.sort_values("data").reset_index(drop=True)

    # Pega o primeiro e último preço do ano
    preco_inicial = df_itub4.iloc[0]["preco"]
    preco_final   = df_itub4.iloc[-1]["preco"]

    retorno = (preco_final / preco_inicial - 1) * 100
    print(f"Retorno de ITUB4 em 2024: {retorno:.2f}%")

except Exception as e:
    print(f"Erro na requisição: {e}")
    print("Verifique seu token e a estrutura de retorno da API.")

    # ── ESTRUTURA DO CÓDIGO (para colar na prova sem internet) ──
    print("""
    # Estrutura padrão para calcular retorno de uma ação:

    resp = requests.get(
        f"{base_url}/preco/corrigido",
        headers={"Authorization": f"Bearer {token}"},
        params={"ticker": "ITUB4", "data_ini": "2024-01-01", "data_fim": "2024-12-31"},
    )
    df_itub4 = pd.DataFrame(resp.json())          # ajuste a chave conforme retorno
    df_itub4["data"] = pd.to_datetime(df_itub4["data"])
    df_itub4 = df_itub4.sort_values("data")

    preco_inicial = df_itub4.iloc[0]["preco"]
    preco_final   = df_itub4.iloc[-1]["preco"]
    retorno = (preco_final / preco_inicial - 1) * 100
    print(f"Retorno de ITUB4 em 2024: {retorno:.2f}%")
    """)


# ──────────────────────────────────────────────────────────────
# QUESTÃO 9 (1,0 pt)
# Maior P/L no setor "financeiro" via Planilhão
# ──────────────────────────────────────────────────────────────
print("\n--- QUESTÃO 9 ---")

# RESPOSTA:
try:
    resp_pl = requests.get(
        f"{base_url}/bolsa/planilhao",
        headers=HEADERS,
        params={"data_base": "2026-04-01"},
        timeout=20,
    )

    df_planilhao = pd.DataFrame(resp_pl.json()["data"])  # ajuste a chave conforme retorno

    # Filtra setor financeiro (case-insensitive)
    df_financeiro = df_planilhao[
        df_planilhao["setor"].str.lower() == "financeiro"
    ]

    # Remove nulos no P/L
    df_financeiro = df_financeiro.dropna(subset=["pl"])

    # Empresa com maior P/L
    idx_max_pl = df_financeiro["pl"].idxmax()
    resultado  = df_financeiro.loc[idx_max_pl, ["ticker", "setor", "pl"]]

    print("Empresa do setor financeiro com maior P/L:")
    print(resultado)

except Exception as e:
    print(f"Erro na requisição: {e}")
    print("""
    # Estrutura padrão para filtrar por setor e pegar maior indicador:

    resp = requests.get(
        f"{base_url}/bolsa/planilhao",
        headers={"Authorization": f"Bearer {token}"},
        params={"data_base": "2026-04-01"},
    )
    df_planilhao = pd.DataFrame(resp.json()["data"])

    df_setor = df_planilhao[df_planilhao["setor"].str.lower() == "financeiro"]
    df_setor = df_setor.dropna(subset=["pl"])

    idx_max = df_setor["pl"].idxmax()
    print(df_setor.loc[idx_max, ["ticker", "setor", "pl"]])
    """)


# ──────────────────────────────────────────────────────────────
# QUESTÃO 10 (1,0 pt)
# Magic Formula: ranking ROC + EY → top 10
# ──────────────────────────────────────────────────────────────
print("\n--- QUESTÃO 10 ---")

# RESPOSTA:
try:
    # Reusa o df_planilhao da questão 9 (se já carregado)
    # Caso contrário, busca novamente:
    # resp = requests.get(f"{base_url}/bolsa/planilhao", headers=HEADERS, params={"data_base": "2026-04-01"})
    # df_planilhao = pd.DataFrame(resp.json()["data"])

    df_magic = df_planilhao.copy()

    # Remove linhas sem roc ou ey
    df_magic = df_magic.dropna(subset=["roc", "ey"])

    # Cria rankings: rank 1 = maior valor de cada indicador
    df_magic["rank_roc"] = df_magic["roc"].rank(ascending=False)
    df_magic["rank_ey"]  = df_magic["ey"].rank(ascending=False)

    # Score final: soma dos dois rankings (menor = melhor)
    df_magic["score_magic"] = df_magic["rank_roc"] + df_magic["rank_ey"]

    # Seleciona top 10
    carteira = df_magic.sort_values("score_magic").head(10).reset_index(drop=True)

    print("Carteira Magic Formula — Top 10:")
    print(carteira[["ticker", "setor", "roc", "ey", "score_magic"]])

except Exception as e:
    print(f"Erro na requisição: {e}")
    print("""
    # Estrutura padrão da Magic Formula:

    df_magic = df_planilhao.dropna(subset=["roc", "ey"]).copy()

    df_magic["rank_roc"]    = df_magic["roc"].rank(ascending=False)
    df_magic["rank_ey"]     = df_magic["ey"].rank(ascending=False)
    df_magic["score_magic"] = df_magic["rank_roc"] + df_magic["rank_ey"]

    carteira = df_magic.sort_values("score_magic").head(10)
    print(carteira[["ticker", "setor", "roc", "ey", "score_magic"]])
    """)


# ──────────────────────────────────────────────────────────────
# QUESTÃO 11 (1,0 pt) — DESAFIO
# Análise da carteira Magic Formula
# ──────────────────────────────────────────────────────────────
print("\n--- QUESTÃO 11 ---")

# RESPOSTA:
try:
    # a) Quantos setores distintos?
    qtd_setores = carteira["setor"].nunique()
    print(f"a) Setores distintos na carteira: {qtd_setores}")
    print(f"   Setores: {carteira['setor'].unique().tolist()}")

    # b) Setor com mais ações na carteira
    setor_dominante = carteira["setor"].value_counts().idxmax()
    print(f"\nb) Setor com mais ações: {setor_dominante}")
    print(carteira["setor"].value_counts())

    # c) Média do ROC das 10 ações
    media_roc = carteira["roc"].mean()
    print(f"\nc) Média do ROC da carteira: {media_roc:.4f}")

except Exception as e:
    print(f"Erro: {e}")
    print("""
    # Estrutura padrão para analisar a carteira:

    # a) Setores distintos
    qtd_setores = carteira["setor"].nunique()
    print(f"Setores distintos: {qtd_setores}")

    # b) Setor mais frequente
    setor_dominante = carteira["setor"].value_counts().idxmax()
    print(f"Setor dominante: {setor_dominante}")

    # c) Média do ROC
    media_roc = carteira["roc"].mean()
    print(f"Média ROC: {media_roc:.4f}")
    """)


# ══════════════════════════════════════════════════════════════
# RESUMO DOS PONTOS
# ══════════════════════════════════════════════════════════════
print("\n" + "="*60)
print("RESUMO — DISTRIBUIÇÃO DE PONTOS")
print("="*60)
print("""
  Parte 1 — Dataset E-Commerce:
    Q1  (0,5 pt) → count de delivered
    Q2  (0,5 pt) → proporção percentual
    Q3  (0,5 pt) → groupby + mean + sort
    Q4  (0,5 pt) → value_counts().idxmax() nos delivered
    Q5  (0,5 pt) → sum do order_value nos delivered
    Q6  (0,5 pt) → mean do order_value + mean do review_score

  Parte 2 — API IPEA:
    Q7  (1,5 pt) → metadados → filtro FNTSIGLA+SERNOME → SERCODIGO
                             → valores → pico máximo com idxmax()

  Parte 3 — API Lab. Finanças (JWT):
    Q8  (1,0 pt) → preco/corrigido → sort → retorno %
    Q9  (1,0 pt) → planilhao → filtro setor → dropna → idxmax()
    Q10 (1,0 pt) → planilhao → rank(roc) + rank(ey) → score → top 10
    Q11 (1,0 pt) → nunique() + value_counts() + mean()

  TOTAL: 10,0 pontos
""")
print("="*60)
print("BOA PROVA! 🎯")
print("="*60)
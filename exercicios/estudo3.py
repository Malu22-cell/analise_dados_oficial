"""
╔══════════════════════════════════════════════════════════════╗
║     QUESTÃO ESTILO AP1 — ESTRATÉGIA BAZIN (DIVIDENDOS)      ║
║              Enunciado + Gabarito Completo                   ║
╚══════════════════════════════════════════════════════════════╝

CONTEXTO:
  A Estratégia Bazin é uma abordagem de investimento em valor que
  seleciona ações com base no Dividend Yield (dy) — quanto a empresa
  paga de dividendos em relação ao preço da ação — e no P/L (Price
  to Earnings), que mede o quanto o mercado paga por cada real de lucro.

  A lógica:
    - Quanto MAIOR o DY  → melhor (empresa paga mais dividendos)
    - Quanto MENOR o P/L → melhor (ação mais barata em relação ao lucro)

  Para combinar os dois critérios:
    1. Ranqueie pelo DY  (rank 1 = maior DY)
    2. Ranqueie pelo P/L (rank 1 = menor P/L → use ascending=True)
    3. Some os rankings: score_bazin = rank_dy + rank_pl
    4. As 10 ações com MENOR score_bazin formam a carteira

ENUNCIADO (1,5 pt):
  Você tem acesso à API do Laboratório de Finanças.
  Use o endpoint /bolsa/planilhao com data_base = "2026-04-01".

  a) Monte uma carteira de 10 ações usando a Estratégia Bazin
     com os indicadores Dividend Yield (dy) e P/L (pl).
  b) Exiba: ticker, setor, dy, pl, rank_dy, rank_pl, score_bazin
  c) Quantos setores distintos essa carteira possui?
  d) Qual o setor com mais ações na carteira?
"""

import requests
import pandas as pd

# ──────────────────────────────────────────────────────────────
# CONFIGURAÇÃO DA API
# ──────────────────────────────────────────────────────────────
base_url = "https://laboratoriodefinancas.com/api/v2"
token    = "SEU_JWT_AQUI"   # <-- substitua pelo seu token

# ──────────────────────────────────────────────────────────────
# PASSO 1 — Buscar o Planilhão
# ──────────────────────────────────────────────────────────────
response = requests.get(
    f"{base_url}/bolsa/planilhao",
    headers={"Authorization": f"Bearer {token}"},
    params={"data_base": "2026-04-01"},
)

dados = response.json()
df = pd.DataFrame(dados)

print("Planilhão carregado!")
print(f"Shape: {df.shape}")
print(f"Colunas: {df.columns.tolist()}")

# ──────────────────────────────────────────────────────────────
# PASSO 2 — Selecionar colunas e limpar nulos
# ──────────────────────────────────────────────────────────────
bazin = df[["ticker", "setor", "dy", "pl"]].copy()
bazin = bazin.dropna(subset=["dy", "pl"])

# Remove P/L negativo (empresa com prejuízo — não faz sentido na Bazin)
bazin = bazin[bazin["pl"] > 0]

print(f"\nLinhas após limpeza: {len(bazin)}")

# ──────────────────────────────────────────────────────────────
# PASSO 3 — Criar os rankings
# ──────────────────────────────────────────────────────────────
# DY:  rank 1 = MAIOR dividend yield   → ascending=False
# P/L: rank 1 = MENOR P/L              → ascending=True
bazin["rank_dy"] = bazin["dy"].rank(ascending=False, method="min")
bazin["rank_pl"] = bazin["pl"].rank(ascending=True,  method="min")

# ──────────────────────────────────────────────────────────────
# PASSO 4 — Score final e seleção das top 10
# ──────────────────────────────────────────────────────────────
bazin["score_bazin"] = bazin["rank_dy"] + bazin["rank_pl"]

carteira = bazin.sort_values("score_bazin").head(10).reset_index(drop=True)

# ──────────────────────────────────────────────────────────────
# PASSO 5 — Exibir resultados
# ──────────────────────────────────────────────────────────────
print("\n=== CARTEIRA BAZIN — TOP 10 ===")
print(carteira[["ticker", "setor", "dy", "pl", "rank_dy", "rank_pl", "score_bazin"]])

# ──────────────────────────────────────────────────────────────
# PARTE C — Quantos setores distintos?
# ──────────────────────────────────────────────────────────────
qtd_setores = carteira["setor"].nunique()
print(f"\nA carteira Bazin possui {qtd_setores} setor(es) distinto(s).")
print(f"Setores: {carteira['setor'].unique().tolist()}")

# ──────────────────────────────────────────────────────────────
# PARTE D — Setor com mais ações na carteira
# ──────────────────────────────────────────────────────────────
setor_dominante = carteira["setor"].value_counts().idxmax()
print(f"\nSetor com mais ações na carteira: {setor_dominante}")
print("\nContagem por setor:")
print(carteira["setor"].value_counts())
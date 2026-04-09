import pandas as pd
import matplotlib.pyplot as plt

# Carregar dataset
df = pd.read_csv("notas.csv")

# ============================================================
# EXPLORAÇÃO INICIAL (EDA BÁSICA)
# ============================================================

print("===== EXERCÍCIO 1 =====")

# 1. Quantas linhas e colunas existem
print("Shape:", df.shape)

# 2. Tipos de dados
print("\nTipos de dados:")
print(df.dtypes)

# 3. Colunas com valores ausentes
print("\nValores ausentes:")
print(df.isnull().sum())

# 4. Período de anos disponível
print("\nAnos disponíveis:")
print(df["year"].min(), "até", df["year"].max())

# 5. Quantos países diferentes existem
print("\nNúmero de países diferentes:")
print(df["country"].nunique())


# ============================================================
# EXERCÍCIO 2 – ESTATÍSTICAS GERAIS
# ============================================================

print("\n===== EXERCÍCIO 2 =====")

# 1. Média do score
print("Média do score:", df["score"].mean())

# 2. Maior score
print("Maior score:", df["score"].max())

# 3. Menor score
print("Menor score:", df["score"].min())

# 4. Média do score por ano
print("\nMédia do score por ano:")
print(df.groupby("year")["score"].mean())

# 5. Desvio padrão
print("\nDesvio padrão do score:")
print(df["score"].std())


# ============================================================
# FILTROS E SELEÇÕES
# ============================================================

print("\n===== EXERCÍCIO 3 =====")

# 1. 10 melhores universidades (menor world_rank)
top10 = df.sort_values("world_rank").head(10)
print("\nTop 10 universidades do mundo:")
print(top10[["institution", "country", "world_rank", "score"]])

# 2. 5 melhores do Brasil
brasil = df[df["country"] == "Brazil"].sort_values("world_rank").head(5)
print("\nTop universidades do Brasil:")
print(brasil[["institution", "world_rank", "score"]])

# 3. Universidades com score maior que 90
score90 = df[df["score"] > 90]
print("\nUniversidades com score > 90:")
print(score90[["institution", "country", "score"]])

# 4. EUA com score maior que 80
usa80 = df[(df["country"] == "United States") & (df["score"] > 80)]
print("\nUniversidades dos EUA com score > 80:")
print(usa80[["institution", "score"]])


# ============================================================
# EXERCÍCIO 4 – SELEÇÃO AVANÇADA
# ============================================================

print("\n===== EXERCÍCIO 4 =====")

# 1. Apenas algumas colunas
print(df[["institution", "country", "score"]])

# 2. Rank entre 50 e 100
rank_50_100 = df[(df["world_rank"] >= 50) & (df["world_rank"] <= 100)]
print("\nUniversidades entre rank 50 e 100:")
print(rank_50_100[["institution", "world_rank"]])

# 3. Universidades do Reino Unido
uk = df[df["country"] == "United Kingdom"]
print("\nUniversidades do Reino Unido:")
print(uk[["institution", "score"]])


# ============================================================
# PARTE 3 – MISSING VALUES
# ============================================================

print("\n===== EXERCÍCIO 5 =====")

# 1. Quantos nulos em broad_impact
print("Nulos em broad_impact:", df["broad_impact"].isnull().sum())

# 2. Percentual nulo
percentual = df["broad_impact"].isnull().mean() * 100
print("Percentual nulo:", percentual, "%")

# 3. Remover linhas com nulo
df_sem_nulo = df.dropna(subset=["broad_impact"])

# 4. Preencher com média
media_broad = df["broad_impact"].mean()
df_preenchido = df.copy()
df_preenchido["broad_impact"].fillna(media_broad, inplace=True)

# 5. Comparação de médias
print("Média antes:", df["broad_impact"].mean())
print("Média depois:", df_preenchido["broad_impact"].mean())


# ============================================================
# PARTE 4 – GROUPBY
# ============================================================

print("\n===== EXERCÍCIO 6 =====")

# 1. Média do score por país
media_pais = df.groupby("country")["score"].mean()
print(media_pais)

# 2. País com maior média
print("\nPaís com maior média:")
print(media_pais.idxmax(), media_pais.max())

# 3. Quantidade de universidades por país
quantidade = df["country"].value_counts()
print("\nUniversidades por país:")
print(quantidade)

# 4. Top 10 países com mais universidades
print("\nTop 10 países:")
print(quantidade.head(10))


# ============================================================
# EXERCÍCIO 7 – ANÁLISE POR ANO
# ============================================================

print("\n===== EXERCÍCIO 7 =====")

# 1. Média do score por ano
media_ano = df.groupby("year")["score"].mean()
print(media_ano)

# 2. Ano com maior média
print("\nAno com maior média:")
print(media_ano.idxmax(), media_ano.max())

# 3. Gráfico
media_ano.plot(marker='o')
plt.title("Evolução do Score Médio por Ano")
plt.xlabel("Ano")
plt.ylabel("Score Médio")
plt.show()
import pandas as pd

"""
Aula - Exercicios de Pandas DataFrame
Como usar:
1) Leia o enunciado de cada bloco.
2) Complete o codigo onde estiver RESOLUCAO.
3) Rode o arquivo e valide os resultados.

Requisito:
- Instalar pandas: pip install pandas

Regra da aula:
- Pense no DataFrame como uma planilha.
- Resolva um exercicio por vez.
"""

# -------------------------------------------------
# BLOCO 1: criar DataFrame e inspecionar estrutura
# -------------------------------------------------
dados_vendas = {
    "mes": ["Jan", "Jan", "Fev", "Fev", "Mar", "Mar"],
    "filial": ["Centro", "Norte", "Centro", "Norte", "Centro", "Norte"],
    "vendas": [12000, 9500, 13500, 10200, 14100, 11000],
    "clientes": [210, 180, 225, 190, 235, 205],
}

print("\n" + "="*60)
print("BLOCO 1: criar DataFrame e inspecionar estrutura")
print("="*60)

# Exercicio 1:
# a) Crie o DataFrame df_vendas usando dados_vendas
# b) Mostre as 5 primeiras linhas
# c) Mostre o formato (linhas, colunas)
# d) Mostre os tipos de dados das colunas

df_vendas = pd.DataFrame(dados_vendas)

print("\n5 primeiras linhas:")
print(df_vendas.head())

print("\nFormato (linhas, colunas):")
print(df_vendas.shape)

print("\nTipos de dados:")
print(df_vendas.dtypes)


# -------------------------------------------------
# BLOCO 2: selecionar colunas e linhas
# -------------------------------------------------
print("\n" + "="*60)
print("BLOCO 2: selecionar colunas e linhas")
print("="*60)

# Exercicio 2:
# a) Mostre apenas as colunas "mes" e "vendas"
# b) Mostre somente a primeira linha
# c) Mostre as linhas de indice 2 ate 4

print("\nColunas 'mes' e 'vendas':")
print(df_vendas[["mes", "vendas"]])

print("\nPrimeira linha:")
print(df_vendas.iloc[0])

print("\nLinhas de índice 2 até 4:")
print(df_vendas.iloc[2:5])


# -------------------------------------------------
# BLOCO 3: filtros com condicoes de negocio
# -------------------------------------------------
print("\n" + "="*60)
print("BLOCO 3: filtros com condições de negócio")
print("="*60)

# Exercicio 3:
# a) Filtre vendas acima de 12000
# b) Filtre apenas a filial "Centro"
# c) Filtre vendas acima de 11000 na filial "Norte"

print("\nVendas acima de 12000:")
print(df_vendas[df_vendas["vendas"] > 12000])

print("\nApenas filial Centro:")
print(df_vendas[df_vendas["filial"] == "Centro"])

print("\nVendas acima de 11000 na filial Norte:")
print(df_vendas[(df_vendas["vendas"] > 11000) & (df_vendas["filial"] == "Norte")])


# -------------------------------------------------
# BLOCO 4: novas colunas e metricas
# -------------------------------------------------
print("\n" + "="*60)
print("BLOCO 4: novas colunas e métricas")
print("="*60)

# Exercicio 4:
# a) Crie a coluna "ticket_medio" = vendas / clientes
# b) Crie a coluna "meta_batida" com True para vendas >= 13000
# c) Mostre apenas "filial", "mes", "ticket_medio", "meta_batida"

df_vendas["ticket_medio"] = df_vendas["vendas"] / df_vendas["clientes"]
df_vendas["meta_batida"] = df_vendas["vendas"] >= 13000

print("\nColunas selecionadas:")
print(df_vendas[["filial", "mes", "ticket_medio", "meta_batida"]])


# -------------------------------------------------
# BLOCO 5: agregacao com groupby
# -------------------------------------------------
print("\n" + "="*60)
print("BLOCO 5: agregação com groupby")
print("="*60)

# Exercicio 5:
# a) Calcule total de vendas por filial
# b) Calcule media de clientes por mes
# c) Descubra a filial com maior total de vendas

total_vendas_filial = df_vendas.groupby("filial")["vendas"].sum()
media_clientes_mes = df_vendas.groupby("mes")["clientes"].mean()
filial_maior_total = total_vendas_filial.idxmax()

print("\nTotal de vendas por filial:")
print(total_vendas_filial)

print("\nMédia de clientes por mês:")
print(media_clientes_mes)

print("\nFilial com maior total de vendas:")
print(filial_maior_total)


# -------------------------------------------------
# BLOCO 6: ordenacao e ranking
# -------------------------------------------------
print("\n" + "="*60)
print("BLOCO 6: ordenação e ranking")
print("="*60)

# Exercicio 6:
# a) Ordene df_vendas por "vendas" em ordem decrescente
# b) Pegue os 3 maiores resultados de vendas
# c) Mostre um ranking com "filial", "mes", "vendas"

df_ordenado = df_vendas.sort_values("vendas", ascending=False)
top_3_vendas = df_ordenado.head(3)
ranking = df_ordenado[["filial", "mes", "vendas"]]

print("\nDataFrame ordenado por vendas (decrescente):")
print(df_ordenado)

print("\nTop 3 maiores vendas:")
print(top_3_vendas)

print("\nRanking com filial, mês e vendas:")
print(ranking)


# -------------------------------------------------
# BLOCO 7: desafio final de analise
# -------------------------------------------------
print("\n" + "="*60)
print("BLOCO 7: desafio final de análise")
print("="*60)

# Exercicio 7 (desafio):
# 1) Gere um resumo por filial com:
#    - total_vendas
#    - media_ticket_medio
#    - total_clientes
# 2) Ordene o resumo por total_vendas (desc)
# 3) Exiba qual filial teve melhor desempenho geral

resumo_filial = df_vendas.groupby("filial").agg(
    total_vendas=("vendas", "sum"),
    media_ticket_medio=("ticket_medio", "mean"),
    total_clientes=("clientes", "sum")
)

resumo_filial = resumo_filial.sort_values("total_vendas", ascending=False)

print("\nResumo por filial:")
print(resumo_filial)

print("\nFilial com melhor desempenho geral:")
print(resumo_filial.index[0])



# ===========================================================
# PARTE 1 – Estrutura lista + dicionário
# ===========================================================
dados_list_dict = [{
    "Column A": [1, 2, 3],
    "Column B": [4, 5, 6],
    "Column C": [7, 8, 9]
}]

print("\n" + "="*60)
print("PARTE 1 – Estrutura lista + dicionário")
print("="*60)

# -----------------------------------------------------------
# EXERCÍCIO 1 – Explorando a estrutura
# -----------------------------------------------------------
# 1. Qual é o tipo de dados_list_dict?
# 2. Qual é o tipo do primeiro elemento?
# 3. Como acessar a lista da "Column A"?
# 4. Como acessar o segundo elemento da "Column C"?

print("\nTipo de dados_list_dict:")
print(type(dados_list_dict))

print("\nTipo do primeiro elemento:")
print(type(dados_list_dict[0]))

print("\nLista da 'Column A':")
print(dados_list_dict[0]["Column A"])

print("\nSegundo elemento da 'Column C':")
print(dados_list_dict[0]["Column C"][1])


# -----------------------------------------------------------
# EXERCÍCIO 2 – Convertendo para DataFrame
# -----------------------------------------------------------
# 1. Converta dados_list_dict[0] em um DataFrame chamado df1
# 2. Mostre:
#    - shape
#    - tipos das colunas
# 3. Calcule:
#    - soma de cada coluna
#    - média de cada coluna

print("\n" + "="*60)
print("EXERCÍCIO 2 – Convertendo para DataFrame")
print("="*60)

df1 = pd.DataFrame(dados_list_dict[0])

print("\nDataFrame df1:")
print(df1)

print("\nShape:")
print(df1.shape)

print("\nTipos das colunas:")
print(df1.dtypes)

print("\nSoma de cada coluna:")
print(df1.sum())

print("\nMédia de cada coluna:")
print(df1.mean())


# -----------------------------------------------------------
# EXERCÍCIO 3 – Criando novas colunas
# -----------------------------------------------------------
# No df1:
# 1. Crie coluna "Total" = soma das colunas
# 2. Crie coluna "Media" = média por linha
# 3. Filtre linhas onde Total > 10

print("\n" + "="*60)
print("EXERCÍCIO 3 – Criando novas colunas")
print("="*60)

df1["Total"] = df1.sum(axis=1)
df1["Media"] = df1[["Column A", "Column B", "Column C"]].mean(axis=1)

print("\nDataFrame com novas colunas:")
print(df1)

print("\nLinhas onde Total > 10:")
print(df1[df1["Total"] > 10])


# -----------------------------------------------------------
# EXERCÍCIO 4 – Conversões estruturais
# -----------------------------------------------------------
# 1. Converta df1 para:
#    - lista de dicionários [ {linha1}, {linha2}, {linha3} ]
#    - dicionário de listas { coluna1: [valores], coluna2: [valores] }

print("\n" + "="*60)
print("EXERCÍCIO 4 – Conversões estruturais")
print("="*60)

lista_de_dicts = df1.to_dict(orient="records")
dict_de_listas = df1.to_dict(orient="list")

print("\nLista de dicionários:")
print(lista_de_dicts)

print("\nDicionário de listas:")
print(dict_de_listas)


# -----------------------------------------------------------
# EXERCÍCIO 5 – Trabalhando com lista
# -----------------------------------------------------------
# 1. Transforme a coluna "Column A" em uma lista chamada lista_a.
# 2. Multiplique cada elemento da lista por 10.
# 3. Crie uma nova coluna chamada "Column A x10" com essa nova lista.

print("\n" + "="*60)
print("EXERCÍCIO 5 – Trabalhando com lista")
print("="*60)

lista_a = df1["Column A"].tolist()
lista_a_x10 = [x * 10 for x in lista_a]
df1["Column A x10"] = lista_a_x10

print("\nLista A:")
print(lista_a)

print("\nLista A multiplicada por 10:")
print(lista_a_x10)

print("\nDataFrame atualizado:")
print(df1)



# ===========================================================
# BASE DE DADOS
# ===========================================================
dados = [
    {"id_pais": 0, "nome_pais": "Brasil", "id_produto": 101, "descricao": "Produto A",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-01", "valor": 5000},

    {"id_pais": 0, "nome_pais": "Brasil", "id_produto": 102, "descricao": "Produto B",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-01", "valor": 3000},

    {"id_pais": 1, "nome_pais": "Argentina", "id_produto": 101, "descricao": "Produto A",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-02", "valor": 4000},

    {"id_pais": 1, "nome_pais": "Argentina", "id_produto": 102, "descricao": "Produto B",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-02", "valor": 6000},

    {"id_pais": 0, "nome_pais": "Brasil", "id_produto": 101, "descricao": "Produto A",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-03", "valor": 7000},
]

print("\n" + "="*60)
print("BASE DE DADOS DE EXPORTAÇÃO")
print("="*60)

# ===========================================================
# PARTE 1 – EXPLORAÇÃO INICIAL
# ===========================================================
# Exercício 1
# 1. Qual o tipo da variável dados?
# 2. Quantos registros existem?
# 3. Quais são as chaves do primeiro dicionário?
# 4. Liste todos os países existentes (sem repetição).

print("\nPARTE 1 – EXPLORAÇÃO INICIAL")

print("\nTipo da variável dados:")
print(type(dados))

print("\nQuantidade de registros:")
print(len(dados))

print("\nChaves do primeiro dicionário:")
print(dados[0].keys())

print("\nPaíses existentes (sem repetição):")
paises = list({item["nome_pais"] for item in dados})
print(paises)


# ===========================================================
# PARTE 2 – CONVERSÃO PARA DATAFRAME
# ===========================================================
# Exercício 2
# 1. Converta dados para DataFrame chamado df
# 2. Mostre shape, tipos e primeiras linhas
# 3. Converta a coluna periodo para datetime

print("\n" + "="*60)
print("PARTE 2 – CONVERSÃO PARA DATAFRAME")
print("="*60)

df = pd.DataFrame(dados)

print("\nShape:")
print(df.shape)

print("\nTipos das colunas antes da conversão:")
print(df.dtypes)

print("\nPrimeiras linhas:")
print(df.head())

df["periodo"] = pd.to_datetime(df["periodo"])

print("\nTipos das colunas depois da conversão de 'periodo':")
print(df.dtypes)


# ===========================================================
# PARTE 3 – FILTROS E ORDENAÇÃO
# ===========================================================
print("\n" + "="*60)
print("PARTE 3 – FILTROS E ORDENAÇÃO")
print("="*60)

# Exercício 3 – Filtros
# 1. Filtre apenas Brasil
# 2. Filtre apenas Produto A
# 3. Filtre valor > 4000
# 4. Combine Brasil + Produto A

print("\nApenas Brasil:")
print(df[df["nome_pais"] == "Brasil"])

print("\nApenas Produto A:")
print(df[df["descricao"] == "Produto A"])

print("\nValor > 4000:")
print(df[df["valor"] > 4000])

print("\nBrasil + Produto A:")
print(df[(df["nome_pais"] == "Brasil") & (df["descricao"] == "Produto A")])


# Exercício 4 – Ordenação
# 1. Ordene por valor crescente
# 2. Ordene por valor decrescente
# 3. Ordene por periodo e depois por valor

print("\nOrdenado por valor crescente:")
print(df.sort_values("valor"))

print("\nOrdenado por valor decrescente:")
print(df.sort_values("valor", ascending=False))

print("\nOrdenado por período e depois por valor:")
print(df.sort_values(["periodo", "valor"]))


# ===========================================================
# PARTE 4 – AGREGAÇÕES
# ===========================================================
print("\n" + "="*60)
print("PARTE 4 – AGREGAÇÕES")
print("="*60)

# Exercício 5 – GroupBy Simples
# 1. Total exportado por país
# 2. Total exportado por produto
# 3. Média por país
# 4. Quantidade de operações por país

print("\nTotal exportado por país:")
print(df.groupby("nome_pais")["valor"].sum())

print("\nTotal exportado por produto:")
print(df.groupby("descricao")["valor"].sum())

print("\nMédia por país:")
print(df.groupby("nome_pais")["valor"].mean())

print("\nQuantidade de operações por país:")
print(df.groupby("nome_pais")["valor"].count())


# Exercício 6 – GroupBy Múltiplo
# Agrupe por nome_pais e descricao
# Calcule soma, média e contagem
# Explique em comentário o que essa tabela representa

print("\nGroupBy múltiplo por país e produto:")
group_multiplo = df.groupby(["nome_pais", "descricao"])["valor"].agg(["sum", "mean", "count"])
print(group_multiplo)

# Essa tabela representa o desempenho de cada produto dentro de cada país,
# mostrando o total exportado (sum), a média dos valores (mean)
# e quantas operações/registros existem (count) para cada combinação.


# ===========================================================
# PARTE 5 – PIVOT TABLE
# ===========================================================
print("\n" + "="*60)
print("PARTE 5 – PIVOT TABLE")
print("="*60)

# Exercício 7 – Pivot por Produto
# Linhas: periodo
# Colunas: descricao
# Valores: soma de valor
# Responda:
# 1. Qual produto vendeu mais?
# 2. Qual mês teve maior valor total?
# 3. Existe mês sem venda?

pivot_produto = df.pivot_table(
    index="periodo",
    columns="descricao",
    values="valor",
    aggfunc="sum"
)

print("\nPivot por produto:")
print(pivot_produto)

produto_mais_vendido = pivot_produto.sum().idxmax()
mes_maior_valor = pivot_produto.sum(axis=1).idxmax()
mes_sem_venda = pivot_produto.isna().any(axis=1)

print("\nProduto que vendeu mais:")
print(produto_mais_vendido)

print("\nMês com maior valor total:")
print(mes_maior_valor)

print("\nExiste mês sem venda?")
print(mes_sem_venda)


# Exercício 8 – Pivot por País
# Linhas: periodo
# Colunas: nome_pais
# Valores: soma de valor
# Explique o que podemos interpretar dessa tabela

pivot_pais = df.pivot_table(
    index="periodo",
    columns="nome_pais",
    values="valor",
    aggfunc="sum"
)

print("\nPivot por país:")
print(pivot_pais)

# Essa tabela mostra quanto cada país exportou em cada período,
# permitindo comparar a evolução das exportações mês a mês entre os países.


# ===========================================================
# PARTE 6 – FEATURE ENGINEERING
# ===========================================================
print("\n" + "="*60)
print("PARTE 6 – FEATURE ENGINEERING")
print("="*60)

# Exercício 9
# 1. Extraia ano e mês da coluna periodo
# 2. Crie coluna valor_mil (valor / 1000)
# 3. Calcule crescimento percentual por produto mês a mês

df["ano"] = df["periodo"].dt.year
df["mes"] = df["periodo"].dt.month
df["valor_mil"] = df["valor"] / 1000

df = df.sort_values(["descricao", "periodo"])
df["crescimento_percentual"] = df.groupby("descricao")["valor"].pct_change() * 100

print("\nDataFrame com novas colunas:")
print(df[["descricao", "periodo", "ano", "mes", "valor", "valor_mil", "crescimento_percentual"]])


# ===========================================================
# PARTE 7 – QUALIDADE DE DADOS
# ===========================================================
print("\n" + "="*60)
print("PARTE 7 – QUALIDADE DE DADOS")
print("="*60)

# Exercício 10
# 1. Verifique valores nulos
# 2. Verifique valores negativos
# 3. Verifique duplicatas

print("\nValores nulos por coluna:")
print(df.isnull().sum())

print("\nRegistros com valores negativos:")
print(df[df["valor"] < 0])

print("\nQuantidade de linhas duplicadas:")
print(df.duplicated().sum())

print("\nLinhas duplicadas:")
print(df[df.duplicated()])
import pandas as pd

# Exemplo de dados (você pode trocar pelo seu arquivo depois)
dados = {
    "estado": ["MG", "MG", "SP", "SP", "RJ"],
    "renda": [1000, 2000, 3000, 4000, 2500]
}

df = pd.DataFrame(dados)

# Agrupar por estado e calcular tudo
resultado = df.groupby("estado")["renda"].agg([
    "min",
    "max",
    "mean",
    "median",
    "std"
])

print(resultado)

#######

import pandas as pd

df = pd.read_csv("nome.csv")

resultado = df.groupby("estado")["renda"].agg([
    "min",
    "max",
    "mean",
    "median",
    "std"
])

print(resultado)



#API
import requests
import pandas as pd

url = "https://viacep.com.br/ws/30140071/json/"

response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    
    df = pd.DataFrame([dados])
    
    print(df.head())
else:
    print("Erro na API")


#Criando DataFrame e filtrando

import pandas as pd

dados = {
    "nome": ["Ana", "Bruno", "Carlos", "Daniela", "Eduarda"],
    "idade": [17, 20, 17, 22, 19],
    "estado": ["MG", "SP", "MG", "RJ", "SP"],
    "renda": [1200, 2500, 1800, 3200, 2100]
}

df = pd.DataFrame(dados)

print(df)

#Filtro com uma condicao
filtro = df["idade"] == 17
df_filtrado = df[filtro]

print(df_filtrado)

#Filtro com multiplas condicoes
filtro = (df["idade"] == 17) & (df["estado"] == "MG")
df_filtrado = df[filtro]

print(df_filtrado)


#Adicionando nova coluna
df["pais"] = "Brasil"

print(df)

#Adicionando coluna com condicao
df["categoria"] = df["idade"].apply(lambda x: "maior" if x >= 18 else "menor")

print(df)

#Removendo coluna
df = df.drop(columns=["renda"])

print(df)


#Ranking
import pandas as pd

dados = {
    "nome": ["Ana", "Bruno", "Carlos", "Daniela", "Eduarda"],
    "estado": ["MG", "SP", "MG", "RJ", "SP"],
    "renda": [1200, 2500, 1800, 3200, 2100]
}

df = pd.DataFrame(dados)

print(df)

#Ranking geral (maior renda=1)
df["ranking"] = df["renda"].rank(ascending=False)

print(df)

#Ranking do menor para o maior 
df["ranking"] = df["renda"].rank(ascending=True)

print(df)

#Ranking por grupo
df["ranking_estado"] = df.groupby("estado")["renda"].rank(ascending=False)

print(df)

#Ranking por grupo + top por grupo
df["ranking_estado"] = df.groupby("estado")["renda"].rank(ascending=False)

top_estado = df[df["ranking_estado"] == 1]

print(top_estado)

# LISTAS

numeros = [10, 20, 30, 40, 50]

print("Lista original:")
print(numeros)

# acessar elementos
print("\nPrimeiro elemento:")
print(numeros[0])

print("\nTerceiro elemento:")
print(numeros[2])

# adicionar elemento
numeros.append(60)
print("\nLista depois de adicionar 60:")
print(numeros)

# remover elemento
numeros.remove(20)
print("\nLista depois de remover 20:")
print(numeros)

# ordenar
numeros.sort()
print("\nLista ordenada:")
print(numeros)

# soma
soma = sum(numeros)
print("\nSoma dos valores:")
print(soma)

# média
media = sum(numeros) / len(numeros)
print("\nMédia dos valores:")
print(media)

# percorrer lista
print("\nPercorrendo a lista:")
for numero in numeros:
    print(numero)

# filtrar valores maiores que 30
maiores_que_30 = [numero for numero in numeros if numero > 30]
print("\nValores maiores que 30:")
print(maiores_que_30)

# DICIONÁRIOS

pessoa = {
    "nome": "Ana",
    "idade": 20,
    "estado": "MG"
}

print("Dicionário original:")
print(pessoa)

# acessar valores
print("\nNome:")
print(pessoa["nome"])

print("\nIdade:")
print(pessoa["idade"])

# adicionar nova chave
pessoa["renda"] = 2500
print("\nDicionário depois de adicionar renda:")
print(pessoa)

# alterar valor
pessoa["idade"] = 21
print("\nDicionário depois de alterar idade:")
print(pessoa)

# remover chave
del pessoa["estado"]
print("\nDicionário depois de remover estado:")
print(pessoa)

# percorrer dicionário
print("\nPercorrendo o dicionário:")
for chave, valor in pessoa.items():
    print(chave, ":", valor)
# Exercício 1: Criando um Dicionário
# Crie um dicionário chamado 'aluno' com as seguintes chaves:
# - 'nome': contendo um nome fictício,
# - 'idade': contendo a idade do aluno,
# - 'curso': contendo o curso que ele está matriculado.
# Após criar o dicionário, exiba seus valores no seguinte formato:]
# Nome: <nome>
# Idade: <idade>
# Curso: <curso>

aluno = {
    'nome': 'Ana Souza',     
    'idade': 19,             
    'curso': 'Administração'  
}

print(f"Nome: {aluno['nome']}")
print(f"Idade: {aluno['idade']}")
print(f"Curso: {aluno['curso']}")


# Exercício 2: Manipulação de Dicionário
# Dado o dicionário abaixo:
# produto = {
# "nome": "Teclado Mecânico",
# "preco": 350.00,
# "estoque": 10}

# 1. Adicione uma nova chave chamada 'marca' com um valor de sua escolha.
# 2. Atualize o preço do produto para R$ 320,00.
# 3. Reduza o estoque em 2 unidades.
# 4. Remova a chave 'marca' do dicionário.
# 5. Exiba o dicionário atualizado.

produto = {
    "nome": "Teclado mecânico",
    "preco": 350.00,
    "estoque": 10
}
produto["marca"] = "Toshiba"
produto["preco"] = 320.00
produto

# Exercício 3: Iterando sobre um Dicionário
# Dado o dicionário:
# notas = {
   # "Alice": 8.5,
   # "Bruno": 7.0,
   # "Carla": 9.2,
   # "Daniel": 6.8}

  
notas = {
"Alice": 8.5,
"Bruno": 7.0,
"Carla": 9.2,
"Daniel":6.8
}

print("Notas dos alunos")
for key, value in notas.items():
    print(f"O aluno é {key} e a nota é {value}")


media = sum(notas.values()) / len(notas)
print(f"A média é: {media}")


# Exercício 4: Soma de Valores
# Dado um dicionário com valores numéricos, percorra o dicionário e some todos os valores.
# Exemplo:
# numeros = {"a": 10, "b": 20, "c": 30}
# Saída esperada: 60

numeros = {"a": 10, "b": 20, "c": 30}
soma = sum(numeros.values())
print(soma)


# Exercício 5: Contagem de Itens Repetidos
# Dado uma lista de elementos, conte a frequência de cada elemento utilizando um dicionário.
# Exemplo:
# lista = ["maçã", "banana", "laranja", "maçã", "banana", "maçã"]
# Saída esperada: {'maçã': 3, 'banana': 2, 'laranja': 1}

lista = ["maçã", "banana", "laranja", "maçã", "banana", "maçã"]
frequencia = {}
for item in lista:
    if item in frequencia:
        frequencia[item] +=1
    else:
        frequencia[item] = 1
    print(frequencia)

# Exercício 6: Filtrando Dicionário
# Dado um dicionário contendo produtos e seus preços, filtre os produtos que custam mais de R$ 50,00.
# Exemplo:
# produtos = {"caneta": 10, "mochila": 80, "caderno": 45, "notebook": 3000}
# Saída esperada: {"mochila": 80, "notebook": 3000}

produtos = {"caneta": 10, "mochila": 80, "caderno": 45, "notebook": 3000 }

filtro = {}
for produto, preco in produtos.items():
    if preco >= 50:
        filtro[produto] = preco
print(filtro)

# Exercício 7: Tradutor Simples
# Crie um dicionário chamado 'tradutor' que contém algumas palavras em inglês como chaves e suas traduções para português como valores.
# Peça ao usuário para digitar uma palavra em inglês e exiba sua tradução, caso exista no dicionário.
# Se a palavra não estiver cadastrada, exiba "Palavra não encontrada".

tradutor = {"door": "porta", "cat": "gato", "drink": "bebida"}
palavra = input("Digite a palavra em inglês:")
if palavra in tradutor:
    print(f"Traducão: {tradutor[palavra]}")
else:
    print("Palavra nao encontrada")

# Exercício 8: Lista de Compras
# Crie um dicionário onde as chaves são nomes de produtos e os valores são quantidades.
# Permita ao usuário adicionar produtos, atualizar quantidades e remover itens.
# No final, exiba a lista completa de compras.

compras = {"bolo": 2, "pão frances": 10, "suco": 1, "salgado": 15}
produtos_adicionais = input
quant_adicionais = input

estoque = {}


# Exercício 9: Dicionário Aninhado
# Crie um dicionário chamado 'turma' onde as chaves são nomes de alunos e os valores são dicionários contendo:
# - "idade" (inteiro),
# - "notas" (lista de três notas).
# Exemplo de estrutura:
# turma = {
# "Ana": {"idade": 17, "notas": [8, 9, 7]},
# "Pedro": {"idade": 18, "notas": [6, 7, 8]},
# "Mariana": {"idade": 17, "notas": [9, 10, 8]}}

turma = { "Ana": {"idade": 17, "notas": [8, 9, 7]},
"Pedro": {"idade": 18, "notas": [6, 7, 8]},
"Mariana": {"idade": 17, "notas": [9, 10, 8]}}

estoque = {}
remover = input("Remover item")
produtor = input("Digite o prduto")
quantidade = int(input("Digite a quantidade"))
if remover == "nao":
    if produto in estoque:
        estoque[produto] = estoque[produto] + quantidade
    else:
        estoque[produto] = quantidade
    print(estoque)
else:
    estoque.pop(produto)
    print(estoque)


# Exercício 10: Cadastro de Funcionários
# Crie um programa que permita cadastrar funcionários em uma empresa.
# O programa deve permitir adicionar funcionários com os seguintes dados:
# - Nome
# - Cargo
# - Salário
# Os funcionários devem ser armazenados em um dicionário onde a chave é o nome e o valor é outro dicionário com os dados do funcionário.
# O programa deve permitir consultar funcionários pelo nome e exibir suas informações.

funcionario = {}

while True:
    escolha = input("Digite o que voce deseja (1:inclusao, 2:consulta):")
    if escolha == '1':
        nome = input("Digite o nome")
        cargo = input("Digite o cargo")
        salario = float(input("Digite a salario"))
        funcionario["nome"] = nome
        funcionario["cargo"] = cargo
        funcionario["salario"] = salario
    elif escolha=='2':
        nome = input("Digite o nome a ser consultado")
        if nome in funcionario["nome"]:
            print(funcionario.values())
    else:
        print("programa encerrado")
        break
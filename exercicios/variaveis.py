"""
Aula - Variaveis e Tipos Basicos em Python
Objetivo:
- Entender o que e uma variavel
- Conhecer tipos basicos: str, int, float, bool
- Aplicar em cenarios simples de negocio
"""

# ------------------------------------------------
# BLOCO 1: o que e variavel na pratica
# ------------------------------------------------
#
# Variavel = "caixa com nome" para guardar um valor.
# Exemplo em negocio:
# - nome_empresa guarda texto
# - funcionarios guarda numero inteiro
# - taxa_juros guarda numero com casas decimais

nome_empresa = "Loja Centro"
funcionarios = 12
taxa_juros = 1.75
empresa_ativa = True

print("Bloco 1")
print(nome_empresa, funcionarios, taxa_juros, empresa_ativa)


# ------------------------------------------------
# BLOCO 2: tipos basicos e type()
# ------------------------------------------------

print("\nBloco 2")
print(type(nome_empresa))   # str
print(type(funcionarios))   # int
print(type(taxa_juros))     # float
print(type(empresa_ativa))  # bool

# Exercicio 1:
# Crie as variaveis abaixo com os tipos corretos:
# a) produto = "Notebook Pro"
# b) estoque = 45
# c) preco = 3499.90
# d) em_promocao = False

# RESOLUCAO: complete aqui


# ------------------------------------------------
# BLOCO 3: entrada, conversao e cuidado
# ------------------------------------------------

# Em Python, dados podem vir como texto (str).
# Para calcular, as vezes precisamos converter.

print("\nBloco 3")
quantidade_str = "10"
preco_str = "25.5"

quantidade = int(quantidade_str)
preco_unitario = float(preco_str)
total = quantidade * preco_unitario

print("Total calculado:", total)

# Exercicio 2:
# Converta os valores e calcule:
# faturamento_str = "15890.75"
# custo_str = "9230.10"
# lucro = faturamento - custo

# RESOLUCAO: complete aqui


# ------------------------------------------------
# BLOCO 4: operacoes com tipos basicos
# ------------------------------------------------

print("\nBloco 4")
vendas_jan = 12000
vendas_fev = 14500
meta_batida = vendas_fev > 13000

print("Soma bimestre:", vendas_jan + vendas_fev)
print("Media bimestre:", (vendas_jan + vendas_fev) / 2)
print("Meta batida em Fev?", meta_batida)

# Exercicio 3:
# Crie um mini painel com variaveis:
# - clientes_ativos (int)
# - ticket_medio (float)
# - nome_gerente (str)
# - equipe_completa (bool)
#
# Depois mostre uma frase com f-string:
# "Gerente X acompanha Y clientes com ticket medio de Z."

# RESOLUCAO: complete aqui


# ------------------------------------------------
# BLOCO 5: pratica focada em f-string
# ------------------------------------------------

# Exercicio 4:
# Monte um resumo executivo usando f-string.
# Use os dados abaixo e exiba:
# "A loja X faturou R$ Y no mes, com crescimento de Z% e status W."
#
# Regras:
# - faturamento com 2 casas decimais
# - crescimento com 1 casa decimal

loja = "Loja Centro"
faturamento_mes = 27890.5
crescimento_percentual = 6.37
status_meta = True

# RESOLUCAO: complete aqui


# ------------------------------------------------
# BLOCO 6: desafio final integrando tudo
# ------------------------------------------------

# Cenario:
# Uma loja quer calcular margem de lucro e status da meta.

receita = 25000.0
custos = 17800.0
meta_receita = 24000.0

# Exercicio 5 (desafio):
# 1) Crie variavel lucro = receita - custos
# 2) Crie variavel margem = (lucro / receita) * 100
# 3) Crie variavel bateu_meta (bool)
# 4) Mostre resultados com 2 casas decimais
#
# Dica:
# print(f"Margem: {margem:.2f}%")

# RESOLUCAO: complete aqui


# ---------------------
# CHECKLIST DE REVISAO
# ---------------------
#
# [ ] Entendo o que e variavel
# [ ] Sei identificar str, int, float, bool
# [ ] Sei usar type() para conferir tipos
# [ ] Sei converter texto para numero com int/float
# [ ] Sei montar calculos simples de negocio
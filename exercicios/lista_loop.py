# Exercício sobre Listas

# 1.	Crie uma lista frutas contendo as seguintes frutas: "maçã", "banana", "laranja", "uva".

frutas = ["maca", "banana", "laranja", "uva"] 

# 2.	Imprima o primeiro e o último elemento da lista.

frutas[0]
frutas[-1]

# 3.	Adicione a fruta "manga" ao final da lista.

frutas.append("manga")
frutas = frutas + ["manga"]

# 4.	Remova a fruta "banana" da lista.

frutas.remove("banana")

# 5.	Substitua "laranja" por "abacaxi".

indice = frutas.index("laranja")
frutas[indice] = "abacaxi"

# 6.	Crie uma lista numeros contendo os números de 1 a 10.

numeros = list(range(1,11))

# 7.	Calcule e imprima a soma de todos os números da lista.

soma = sum(numeros)
print(soma)

# 8.	Encontre e imprima o maior e o menor número da lista.

max(numeros)
min(numeros)

# 9.	Inverta a ordem dos elementos na lista e imprima a lista invertida.

list(reversed(numeros))

# 10.	Crie uma lista cidades contendo as seguintes cidades: "São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba".

cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba"]

# 11.	Ordene a lista cidades em ordem alfabética.

sorted(cidades)

# 12.	Adicione a cidade "Porto Alegre" ao final da lista.

cidades.append("Porto Alegre")
cidade = cidades + ["Porto Alegre"]

# 13.	Encontre o índice da cidade "Curitiba" na lista.

cidades.index("Curitiba")

# 14.	Remova a cidade "Rio de Janeiro" da lista.

cidades.remove("Rio de Janeiro")

# 15.	Crie duas listas lista1 e lista2, onde lista1 contém os números [1, 2, 3] e lista2 contém os números [4, 5, 6].

lista1 = [1,2,3]
lista2 = [4,5,6]

# 16.	Concatene lista1 e lista2 em uma nova lista lista3.

lista3 = [lista1, lista2]

# 17.	Imprima lista3.

print(lista3)

# 18.	Crie duas listas animais_domesticos e animais_selvagens, onde animais_domesticos contém ["cachorro", "gato", "coelho"] e animais_selvagens contém ["leão", "tigre", "urso"].

animais_domesticos = ["cachorro", "gato", "coelho"]
animais_selvagens = ["leão", "tigre", "urso"]

# 19.	Concatene as duas listas em uma nova lista todos_animais.

todos_animais = [animais_domesticos, animais_selvagens]

# 20.	Imprima todos_animais.

print(todos_animais)

# 21.	Crie uma lista nomes contendo os nomes: "Ana", "Pedro", "Maria", "João".

nomes=["Ana", "Pedro", "Maria", "João"]

# 22.	Utilize um loop for para imprimir cada nome da lista.

for nome in nomes:
    print(nomes)

# 23.	Crie uma nova lista nomes_maiusculos contendo os nomes da lista nomes em letras maiúsculas. Utilize um loop for para isso.

nomes_maiusculos = []
for nome in nomes:
    nomes_maiusculos.append(nome)
    print(nome)

# 24.	Crie uma lista numeros contendo os números de 1 a 20. Utilize um loop for para imprimir apenas os números pares.

numeros = list(range(1,21))
for i in numeros:
    if i % 2 == 0:
        print(i)

# 25.	Usando a lista numeros, utilize um loop for para criar uma nova lista quadrados contendo o quadrado de cada número.

numeros = list(range(1,21))
quadrados = []
for n in numeros:
    quadrados.append(n ** 2)
    print("Numeros", numeros)
    print("Quadrados:", quadrados)

# 26.	Crie uma lista palavras contendo: "python", "java", "c", "javascript". Utilize um loop for para imprimir o tamanho (número de letras) de cada palavra.

palavras = ["python", "java", "c", "javascript"]
for palavra in palavras:
    print(f"A palavra '{palavra}' tem {len(palavras)} letras")

# 27.	Crie uma lista idades contendo [12, 18, 25, 40, 60]. Utilize um loop for para imprimir "maior de idade" se a idade for >= 18 ou "menor de idade" se for < 18.

idades = [12, 18, 25, 40, 60]
for idade in idades:
    if idade >= 18:
        print("maior idade")
    else:
        print("Menor idade")

# 28.	Crie uma lista notas contendo [5.5, 7.0, 8.3, 4.9, 6.2]. Utilize um loop for para contar quantos alunos estão aprovados (nota >= 7) e quantos estão reprovados (nota < 7).

notas = [5.5,7.0,8.3,4.9,6.2]
aprovados = 0
nao_aprovados = 0

# 29.	Crie uma lista palavras com ["arara", "banana", "radar", "python"]. Utilize um loop for para identificar e imprimir quais palavras são palíndromos (iguais quando lidas de trás para frente).

palavras = ["arara", "banana", "radar", "python"]
for palavra in palavras:
    if palavra == palavra[::-1]:
        print(f"'{palavra}'é um palindromo")
    else:
        print(f"'{palavra}'nao é um palindromo")

# 30.	Crie uma lista compras com ["arroz", "feijão", "batata", "carne"]. Utilize um loop for para imprimir cada item precedido da frase "Preciso comprar: ".

compras = ["arroz", "feijão", "batata", "carne"]
for item in compras:
    print(f"Preciso comprar:{item}")

# 31. Escreva um programa que use um loop while para imprimir os números de 1 a 10.

numero = 1
while numero <= 10:
    print(numero)
    numero = numero + 1

# 32. Usando um loop while, peça para o usuário digitar um número inteiro. O programa deve parar quando o usuário digitar o número 0.

while True:
    numero = int(input("Digite um numero:"))
    print(numero)
    if numero == 0:
        print("Numero 0 digitado")
        break
    

# 33. Utilize um loop while para calcular a soma dos números de 1 a 100.

numero = 1 
soma = 0
while numero <= 100:
    soma =+ numero
    numero += 1
    print("A soma dos numeros de 1 a 100 é:", soma)

# 34. Peça para o usuário adivinhar um número secreto (por exemplo, 7). Use um loop while para continuar pedindo até que ele acerte.

while True:
    numero = int(input("Digite um numero:"))
    print(numero)
    if numero == 7:
        print("Numero correto")
        break
    else:
        print("Numero errado")
    

# 35. Crie um loop while que imprima todos os números pares de 2 até 20.

numero = 2
while numero <= 20:
    print(numero)
    numero = numero = 2
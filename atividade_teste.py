# Questão 1: Carregar o DataFrame
# LER arquivo titanic.csv em um DataFrame pandas chamado df?
import pandas as pd
df = pd.read_csv('titanic.csv')
df

# Questão 2: Filtrar passageiros do sexo feminino
# Filtrar o DataFrame para mostrar apenas as Mulheres?
# (Dica: Filtar onde a coluna "Sex" é igual a "female")
df[df['Sex'] == 'female']


# Questão 3: Contar sobreviventes
# Quantos passageiros Sobreviveram?
# (Dica: Sobreviventes têm o valor 1 na coluna "Survived")
df['Survived'].sum()

# Questão 4: Quantos Homens Sobreviveram?
df[df['Sex'] == 'male']['Survived'].sum()

# Questão 5: Calcular Nome "John"
# Calcular quantos passageiros tem o nome "John"?
# (Dica: Usar a coluna "Name")
df[df['Name'].str.contains('John', case=False, na=False)].shape[0]
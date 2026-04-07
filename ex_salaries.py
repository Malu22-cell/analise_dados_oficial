# Questão 1:
# Ler o arquivo salaries.csv em um DataFrame chamado df
import pandas as pd
df = pd.read_csv('salaries.csv')
df

# Questão 2:
# Qual o maior salário ("salary_in_usd") no dataset?
maior_salario = df['salary_in_usd'].max()
print(f"O maior salário é: {maior_salario}")


# Questão 3:
# Quantos funcionários são "Data Scientist" na coluna ("job_title")?
data_scientist = df['job_title'].sum()
print(f"Os funcionarios são:{data_scientist}")

# Questão 4:
# Quantos cargos ("job_title") possuem a palavra "Engineer"?



# Questão 5:
# Mostrar funcionários ("experience_level") Senior ("SE") 
# que ganham ("salary_in_usd") mais que 100 mil








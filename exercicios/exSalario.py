import pandas as pd

# carregar dataset
df = pd.read_excel("salary.xlsx")

# ------------------------------------------------
# 1 Quantas linhas e colunas
# ------------------------------------------------
print("Linhas e colunas:", df.shape)

# ------------------------------------------------
# 2 Média, maior e menor salário
# ------------------------------------------------
print("Média salarial:", df["salary_in_usd"].mean())
print("Maior salário:", df["salary_in_usd"].max())
print("Menor salário:", df["salary_in_usd"].min())

# ------------------------------------------------
# 3 Novo dataframe com colunas específicas
# ------------------------------------------------
df2 = df[["job_title","salary_in_usd","company_location","company_size","remote_ratio"]]
print(df2.head())

# ------------------------------------------------
# 4 Maior e menor salário de Data Scientist
# ------------------------------------------------
ds = df[df["job_title"] == "Data Scientist"]

print("Maior salário Data Scientist:", ds["salary_in_usd"].max())
print("Menor salário Data Scientist:", ds["salary_in_usd"].min())

print("Empresa maior salário fica em:",
      ds.loc[ds["salary_in_usd"].idxmax(),"company_location"])

print("Empresa menor salário fica em:",
      ds.loc[ds["salary_in_usd"].idxmin(),"company_location"])

# ------------------------------------------------
# 5 Profissão com maior e menor média salarial
# ------------------------------------------------
media_prof = df.groupby("job_title")["salary_in_usd"].mean()

print("Profissão maior média:", media_prof.idxmax())
print("Valor:", media_prof.max())

print("Profissão menor média:", media_prof.idxmin())
print("Valor:", media_prof.min())

# ------------------------------------------------
# 6 Profissões com média maior que média geral
# ------------------------------------------------
media_geral = df["salary_in_usd"].mean()

print(media_prof[media_prof > media_geral])

# ------------------------------------------------
# 7 Localização com maior média salarial
# ------------------------------------------------
media_pais = df.groupby("company_location")["salary_in_usd"].mean()

print("Local com maior média:", media_pais.idxmax())

# ------------------------------------------------
# 8 Profissões existentes no Brasil
# ------------------------------------------------
br = df[df["company_location"] == "BR"]

print("Profissões no Brasil:")
print(br["job_title"].unique())

# ------------------------------------------------
# 9 Média salarial no Brasil
# ------------------------------------------------
print("Média salarial no Brasil:", br["salary_in_usd"].mean())

# ------------------------------------------------
# 10 Quantas profissões existem no Brasil
# ------------------------------------------------
print("Quantidade de profissões no Brasil:",
      br["job_title"].nunique())

# ------------------------------------------------
# 11 Profissão que mais ganha no Brasil
# ------------------------------------------------
print(
    br.groupby("job_title")["salary_in_usd"]
    .mean()
    .idxmax()
)

# ------------------------------------------------
# 12 Quantas profissões nos US em empresas grandes
# ------------------------------------------------
us_large = df[(df["company_location"] == "US") &
              (df["company_size"] == "L")]

print("Profissões nos US em empresas grandes:",
      us_large["job_title"].nunique())

# ------------------------------------------------
# 13 Média salarial empresas médias no Canadá
# ------------------------------------------------
ca_m = df[(df["company_location"] == "CA") &
          (df["company_size"] == "M")]

print("Média salarial Canadá empresas médias:",
      ca_m["salary_in_usd"].mean())

# ------------------------------------------------
# 14 País com mais profissões e menos
# ------------------------------------------------
jobs_pais = df.groupby("company_location")["job_title"].nunique()

print("País com mais profissões:", jobs_pais.idxmax())
print("País com menos profissões:", jobs_pais.idxmin())

# ------------------------------------------------
# 15 Quem ganha mais: remoto, presencial ou híbrido
# ------------------------------------------------
print(df.groupby("remote_ratio")["salary_in_usd"].mean())

# remote_ratio
# 0 = presencial
# 50 = híbrido
# 100 = remoto

# ------------------------------------------------
# 16 País com mais profissões 100% remoto
# ------------------------------------------------
remoto = df[df["remote_ratio"] == 100]

print(remoto["company_location"].value_counts().idxmax())
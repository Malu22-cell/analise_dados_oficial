import requests
import pandas as pd
base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc3MTE5MzIwLCJpYXQiOjE3NzQ1MjczMjAsImp0aSI6ImY1OWE1YTM1MzgwNjQxMzc4MDA1NDBhZDU1ZTNkZTY2IiwidXNlcl9pZCI6IjEyNSJ9.SpCIAGyeyHW_EqevLvBfkJANPFhqO0JuIZqEVph-cXE"
params = {"ticker": "NATU3", "ano_tri": "20244T"}
resp = requests.get(
    f"{base_url}/bolsa/balanco",
    headers={"Authorization": f"Bearer {token}"},
    params=params,
)
dados = resp.json()[0]['balanco']
df_2024 = pd.DataFrame(dados)

#ativo circulando
ativo_circ = df_2024[df_2024["conta"]=='1.01']['valor']
ativo_circ = float(ativo_circ.iloc[0])

#passivo circulante
passivo_circ = df_2024[df_2024["conta"]=='2.01']['valor']
passivo_circ = float(passivo_circ.iloc[0])

#passivo
passivo_n_circ = df_2024[df_2024["conta"]=='2.02']['valor']
passivo_n_circ = float(passivo_n_circ.iloc[0])

#intangivel 
filtro1 = df_2024["descricao"].str.contains('intang.vel', case=False)
filtro2 = df_2024["conta"]=='1.02.04'
intangivel = df_2024[filtro1 & filtro2]['valor']
intangivel = float(intangivel.iloc[0])

#imobilizado
filtro1 = df_2024["descricao"].str.contains('imobilizado', case=False)
filtro2 = df_2024["conta"].str.contains('1.02.03', case=False)
imobilizado = df_2024[filtro1 & filtro2]['valor']
imobilizado = float(imobilizado.iloc[0])

#investimento
filtro1 = df_2024["descricao"].str.contains('investimento', case=False)
filtro2 = df_2024["conta"].str.contains('1.02.02', case=False)
investimento = df_2024[filtro1 & filtro2]['valor']
investimento = float(investimento.iloc[0])

#estoque 
filtro1 = df_2024["descricao"].str.contains('estoque', case=False)
#filtro2 = df_2024["conta"].str.contains('1.02.02', case=False)
estoque = df_2024[filtro1]['valor']
estoque = float(estoque.iloc[0])

#despesa antecipada 
filtro1 = df_2024["descricao"].str.contains('despesa', case=False)
filtro2 = df_2024["conta"].str.contains('1.01.07', case=False)
despesa_antecipada = df_2024[filtro1 & filtro2]
despesa_antecipada = float(despesa_antecipada.iloc[0])

#caixa
filtro1 = df_2024["descricao"].str.contains('caixa.*equivalentes', case=False)
filtro2 = df_2024["conta"].str.contains('ˆ1.*', case=False)
caixa_equivalentes = df_2024[filtro1 & filtro2]
caixa_equivalentes = float(caixa_equivalentes.iloc[0])

#cmv
filtro1 = df_2024["descricao"].str.contains('custo.*bens', case=False)
filtro2 = df_2024["conta"].str.contains('ˆ3.*', case=False)
cmv = df_2024[filtro1 & filtro2]
cmv = float(cmv['valor'].iloc[0])




import requests
import pandas as pd
base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc3MTE5MzIwLCJpYXQiOjE3NzQ1MjczMjAsImp0aSI6ImY1OWE1YTM1MzgwNjQxMzc4MDA1NDBhZDU1ZTNkZTY2IiwidXNlcl9pZCI6IjEyNSJ9.SpCIAGyeyHW_EqevLvBfkJANPFhqO0JuIZqEVph-cXE"
params = {"ticker": "NATU3", "ano_tri": "20254T"}
resp = requests.get(
    f"{base_url}/bolsa/balanco",
    headers={"Authorization": f"Bearer {token}"},
    params=params,
)
dados = resp.json()[0]['balanco']
df_2025 = pd.DataFrame(dados)

#ativo circulando
ativo_circ = df_2025[df_2025["conta"]=='1.01']['valor']
ativo_circ = float(ativo_circ.iloc[0])

#passivo circulante
passivo_circ = df_2025[df_2025["conta"]=='2.01']['valor']
passivo_circ = float(passivo_circ.iloc[0])

#passivo
passivo_n_circ = df_2025[df_2025["conta"]=='2.02']['valor']
passivo_n_circ = float(passivo_n_circ.iloc[0])

#intangivel 
filtro1 = df_2025["descricao"].str.contains('intang.vel', case=False)
filtro2 = df_2025["conta"]=='1.02.04'
intangivel = df_2025[filtro1 & filtro2]['valor']
intangivel = float(intangivel.iloc[0])

#imobilizado
filtro1 = df_2025["descricao"].str.contains('imobilizado', case=False)
filtro2 = df_2025["conta"].str.contains('1/.', case=False)
imobilizado = df_2025[filtro1 & filtro2]['valor']
imobilizado = float(imobilizado.iloc[0])

#investimento
filtro1 = df_2025["descricao"].str.contains('investimento', case=False)
filtro2 = df_2025["conta"].str.contains('1.02.02', case=False)
investimento = df_2025[filtro1 & filtro2]['valor']
investimento = float(investimento.iloc[0])

#estoque 
filtro1 = df_2025["descricao"].str.contains('estoque', case=False)
#filtro2 = df_2025["conta"].str.contains('1.02.02', case=False)
estoque = df_2025[filtro1]['valor']
estoque = float(estoque.iloc[0])

#despesa antecipada 
filtro1 = df_2025["descricao"].str.contains('despesa', case=False)
filtro2 = df_2025["conta"].str.contains('1.01.07', case=False)
despesa_antecipada = df_2025[filtro1 & filtro2]
despesa_antecipada = float(despesa_antecipada.iloc[0])

#caixa
filtro1 = df_2025["descricao"].str.contains('caixa.*equivalentes', case=False)
filtro2 = df_2025["conta"].str.contains('ˆ1.*', case=False)
caixa_equivalentes = df_2025[filtro1 & filtro2]
caixa_equivalentes = float(caixa_equivalentes.iloc[0])

#cmv
filtro1 = df_2025["descricao"].str.contains('custo.*bens', case=False)
filtro2 = df_2025["conta"].str.contains('ˆ3.*', case=False)
cmv = df_2025[filtro1 & filtro2]
cmv = float(cmv['valor'].iloc[0])

#Calculando os Indicadores 
ccl = ativo_circ - passivo_circ
lc = ativo_circ / passivo_circ
arlp = intangivel + imobilizado + investimento
lg = (ativo_circ + arlp) / (passivo_circ + passivo_n_circ)
ls = (ativo_circ - estoque - despesa_antecipada)
la = caixa_equivalentes / passivo_circ
pme = (((estoque24 + estoque25) /2) * 360) / cmv
pme = abs(pme)


def encontrar_contas_contabeis(df):


    # Calculando os indicadores
    ccl = ativo_circ - passivo_circ
    lc = ativo_circ / passivo_circ
    arlp = intangivel + imobilizado + investimento
    lg = (ativo_circ + arlp) / (passivo_circ + passivo_n_circ)
    ls = (ativo_circ - estoque - despesa_antecipada) / passivo_circ
    la = caixa_equivalentes / passivo_circ
    pme = (((estoque24 + estoque25) / 2) * 360) / cmv
    pme = abs(pme)

    return {
        'ativo_circ': ativo_circ,
        'passivo_circ': passivo_circ,
        'passivo_n_circ': passivo_n_circ,
        'intangivel': intangivel,
        'imobilizado': imobilizado,
        'investimento': investimento,
        'estoque': estoque,
        'despesa_antecipada': despesa_antecipada,
        'caixa_equivalentes': caixa_equivalentes,
        'cmv': cmv,

        'ccl': ccl,
        'lc': lc,
        'arlp': arlp,
        'lg': lg,
        'ls': ls,
        'la': la,
        'pme': pme
    }


# Rodar a função
dic_2024 = encontrar_contas_contabeis(df_2024)
dic_2025 = encontrar_contas_contabeis(df_2025)


# Definição da função para calcular os indicadores financeiros
# Entrada: O dicionário com as contas contábeis calculadas
# Saída: Os indicadores financeiros calculados

def calcular_indicadores_financeiros(dic):
    ativo_circ = dic['ativo_circ']
    passivo_circ = dic['passivo_circ']
    passivo_n_circ = dic['passivo_n_circ']
    intangivel = dic['intangivel']
    imobilizado = dic['imobilizado']
    investimento = dic['investimento']
    estoque = dic['estoque']
    despesa_antecipada = dic['despesa_antecipada']
    caixa_equivalentes = dic['caixa_equivalentes']

    # Calculo dos Indicadores Financeiros da empresa
    ccl = ativo_circ - passivo_circ
    lc = ativo_circ / passivo_circ
    arlp = intangivel + imobilizado + investimento
    lg = (ativo_circ + arlp) / (passivo_circ + passivo_n_circ)
    ls = (ativo_circ - estoque - despesa_antecipada) / (passivo_circ)
    la = caixa_equivalentes / passivo_circ

    return {
        'ccl': ccl,
        'lc': lc,
        'arlp': arlp,
        'lg': lg,
        'ls': ls,
    }

# Rodar a função
ind_fin_2024 = calcular_indicadores_financeiros(dic_2024)
ind_fin_2025 = calcular_indicadores_financeiros(dic_2025)


# Ativo Total
ativo_total = df[df['conta'].str.contains('Ativo Total', case=False)]
ativo_total = float(ativo_total['valor'].iloc[0])

# Patrimônio Líquido
patrimonio_liquido = df[df['conta'].str.contains('Patrimônio Líquido', case=False)]
patrimonio_liquido = float(patrimonio_liquido['valor'].iloc[0])

# Lucro Líquido
lucro_liquido = df[df['conta'].str.contains('Lucro Líquido', case=False)]
lucro_liquido = float(lucro_liquido['valor'].iloc[0])

# EBIT
ebit = df[df['conta'].str.contains('EBIT', case=False)]
ebit = float(ebit['valor'].iloc[0])

# NOPAT
nopat = ebit * (1 - 0.34)   

# Capital Investido
capital_investido = patrimonio_liquido + passivo_n_circ

# Capital Empregado
capital_empregado = ativo_total - passivo_circ

# Número de ações
numero_acoes = 1000000  

# Preço da ação
preco_acao = 25.50  

# WACC
wacc = 0.12  

# Indicadores de preço
vpa = patrimonio_liquido / numero_acoes
lpa = lucro_liquido / numero_acoes
p_vpa = preco_acao / vpa
p_lpa = preco_acao / lpa

# Indicadores de rentabilidade
roe = lucro_liquido / patrimonio_liquido
roi = lucro_liquido / investimento
roic = nopat / capital_investido
roa = lucro_liquido / ativo_total
roce = ebit / capital_empregado

# EVA
eva = nopat - (wacc * capital_investido)


def encontrar_contas_contabeis(df):

    return {
    # contas
    'ativo_circ': ativo_circ,
    'passivo_circ': passivo_circ,
    'passivo_n_circ': passivo_n_circ,
    'ativo_total': ativo_total,
    'patrimonio_liquido': patrimonio_liquido,
    'lucro_liquido': lucro_liquido,
    'preco_acao': preco_acao,
    'numero_acoes': numero_acoes,
    'nopat': nopat,
    'capital_investido': capital_investido,
    'capital_empregado': capital_empregado,
    'wacc': wacc,

    # indicadores de preço
    'vpa': vpa,
    'lpa': lpa,
    'p_vpa': p_vpa,
    'p_lpa': p_lpa,

    # indicadores de rentabilidade
    'roe': roe,
    'roi': roi,
    'roic': roic,
    'roa': roa,
    'roce': roce,

    # EVA
    'eva': eva
}
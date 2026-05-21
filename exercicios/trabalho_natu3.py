import requests
import pandas as pd

base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc3MTE5MzIwLCJpYXQiOjE3NzQ1MjczMjAsImp0aSI6ImY1OWE1YTM1MzgwNjQxMzc4MDA1NDBhZDU1ZTNkZTY2IiwidXNlcl9pZCI6IjEyNSJ9.SpCIAGyeyHW_EqevLvBfkJANPFhqO0JuIZqEVph-cXE"

# Balanço de 2025
params = {"ticker": "NATU3", "ano_tri": "20254T"}
resp = requests.get(
    f"{base_url}/bolsa/balanco",
    headers={"Authorization": f"Bearer {token}"},
    params=params,
)
df_2025 = pd.DataFrame(resp.json()[0]['balanco'])
print(df_2025)

# Balanço de 2024
params = {"ticker": "NATU3", "ano_tri": "20244T"}
resp = requests.get(
    f"{base_url}/bolsa/balanco",
    headers={"Authorization": f"Bearer {token}"},
    params=params,
)
df_2024 = pd.DataFrame(resp.json()[0]['balanco'])
print(df_2024)

# Balanço de 2023 (necessário para médias dos indicadores de rentabilidade)
params = {"ticker": "NATU3", "ano_tri": "20234T"}
resp = requests.get(
    f"{base_url}/bolsa/balanco",
    headers={"Authorization": f"Bearer {token}"},
    params=params,
)
df_2023 = pd.DataFrame(resp.json()[0]['balanco'])
print(df_2023)


# Definição da função para encontrar as contas contabeis do balanço
# Entrada: O balanço da empresa
# Saída: As contas contábeis calculadas

def encontrar_contas_contabeis(df):

    # Ativo Circulante
    ativo_circ = df[df["conta"]=='1.01']['valor']
    ativo_circ = float(ativo_circ.iloc[0])

    # Passivo Circulante
    passivo_circ = df[df["conta"]=='2.01']['valor']
    passivo_circ = float(passivo_circ.iloc[0])

    # Passivo Não Circulante
    passivo_n_circ = df[df["conta"]=='2.02']['valor']
    passivo_n_circ = float(passivo_n_circ.iloc[0])

    # Intangível
    filtro1 = df["descricao"].str.contains('intang.vel', case=False)
    filtro2 = df["conta"]=='1.02.04'
    intangivel = df[filtro1 & filtro2]['valor']
    intangivel = float(intangivel.iloc[0])

    # Imobilizado
    filtro1 = df["descricao"].str.contains('imobilizado', case=False)
    filtro2 = df["conta"].str.contains('1.02.03', case=False)
    imobilizado = df[filtro1 & filtro2]['valor']
    imobilizado = float(imobilizado.iloc[0])

    # Investimento
    filtro1 = df["descricao"].str.contains('investimento', case=False)
    filtro2 = df["conta"].str.contains('1.02.02', case=False)
    investimento = df[filtro1 & filtro2]['valor']
    investimento = float(investimento.iloc[0])

    # Realizável a Longo Prazo (ARLP - conta 1.02.01)
    rlp = df[df["conta"]=='1.02.01']['valor']
    rlp = float(rlp.iloc[0])

    # Estoque
    filtro1 = df["descricao"].str.contains('estoque', case=False)
    estoque = df[filtro1]['valor']
    estoque = float(estoque.iloc[0])

    # Despesa antecipada
    filtro1 = df["descricao"].str.contains('despesa', case=False)
    filtro2 = df["conta"].str.contains('1.01.07', case=False)
    despesa_antecipada = df[filtro1 & filtro2]['valor']
    despesa_antecipada = float(despesa_antecipada.iloc[0])

    # Caixa e equivalentes
    filtro1 = df["descricao"].str.contains('caixa.*equivalentes', case=False)
    filtro2 = df["conta"].str.contains('1.*', case=False)
    caixa_equivalentes = df[filtro1 & filtro2]
    caixa_equivalentes = float(caixa_equivalentes['valor'].iloc[0])

    # CMV
    filtro1 = df["descricao"].str.contains('custo.*bens', case=False)
    filtro2 = df["conta"].str.contains('3.*', case=False)
    cmv = df[filtro1 & filtro2]
    cmv = float(cmv['valor'].iloc[0])

    # PL (Patrimônio Líquido)
    pl = df[df["conta"]=='2.03']['valor']
    pl = float(pl.iloc[0])

    # Ativo Total
    ativo_total = df[df["conta"]=='1']['valor']
    ativo_total = float(ativo_total.iloc[0])

    # Passivo Total (PC + PNC)
    passivo_total = passivo_circ + passivo_n_circ

    # Contas a Receber
    filtro1 = df["descricao"].str.contains('clientes|receb', case=False)
    filtro2 = df["conta"].str.contains('1.01.03', case=False)
    contas_receber = df[filtro1 & filtro2]['valor']
    contas_receber = float(contas_receber.iloc[0])

    # Fornecedores
    filtro1 = df["descricao"].str.contains('fornecedor', case=False)
    filtro2 = df["conta"].str.contains('2.01.02', case=False)
    fornecedores = df[filtro1 & filtro2]['valor']
    fornecedores = abs(float(fornecedores.iloc[0]))

    # Dívida Financeira CP (Empréstimos e Financiamentos de curto prazo)
    filtro1 = df["descricao"].str.contains('empr.stimo|financiamento', case=False)
    filtro2 = df["conta"].str.contains('2.01.04', case=False)
    divida_cp = df[filtro1 & filtro2]['valor']
    divida_cp = abs(float(divida_cp.iloc[0]))

    # Dívida Financeira LP (Empréstimos e Financiamentos de longo prazo)
    filtro1 = df["descricao"].str.contains('empr.stimo|financiamento', case=False)
    filtro2 = df["conta"].str.contains('2.02.01', case=False)
    divida_lp = df[filtro1 & filtro2]['valor']
    divida_lp = abs(float(divida_lp.iloc[0]))

    # Receita Líquida (DRE - conta 3.01)
    receita_liquida = df[df["conta"]=='3.01']['valor']
    receita_liquida = float(receita_liquida.iloc[0])

    # Lucro Bruto (DRE - conta 3.03)
    lucro_bruto = df[df["conta"]=='3.03']['valor']
    lucro_bruto = float(lucro_bruto.iloc[0])

    # EBIT / Resultado Operacional (DRE - conta 3.05)
    ebit = df[df["conta"]=='3.05']['valor']
    ebit = float(ebit.iloc[0])

    # Lucro Líquido (DRE - conta 3.11)
    lucro_liquido = df[df["conta"]=='3.11']['valor']
    lucro_liquido = float(lucro_liquido.iloc[0])

    # NOPAT = EBIT - IR/CSLL corrente (conta 3.08.01)
    ir_corrente = df[df["conta"]=='3.08.01']['valor']
    ir_corrente = float(ir_corrente.iloc[0])
    nopat = ebit - ir_corrente

    # EBITDA = EBIT + Depreciação e Amortização (buscada no fluxo de caixa, conta 6.*)
    filtro1 = df["descricao"].str.contains('deprecia|amortiza', case=False)
    filtro2 = df["conta"].str.startswith('6.')
    dep = df[filtro1 & filtro2]['valor']
    depreciacao = abs(float(dep.astype(float).sum())) if len(dep) > 0 else 0
    ebitda = ebit + depreciacao

    return {
        'ativo_circ': ativo_circ,
        'passivo_circ': passivo_circ,
        'passivo_n_circ': passivo_n_circ,
        'intangivel': intangivel,
        'imobilizado': imobilizado,
        'investimento': investimento,
        'rlp': rlp,
        'estoque': estoque,
        'despesa_antecipada': despesa_antecipada,
        'caixa_equivalentes': caixa_equivalentes,
        'cmv': cmv,
        'pl': pl,
        'ativo_total': ativo_total,
        'passivo_total': passivo_total,
        'contas_receber': contas_receber,
        'fornecedores': fornecedores,
        'divida_cp': divida_cp,
        'divida_lp': divida_lp,
        'receita_liquida': receita_liquida,
        'lucro_bruto': lucro_bruto,
        'ebit': ebit,
        'ebitda': ebitda,
        'nopat': nopat,
        'lucro_liquido': lucro_liquido,
    }


# Rodar a função
dic_2023 = encontrar_contas_contabeis(df_2023)
print(dic_2023)
dic_2024 = encontrar_contas_contabeis(df_2024)
print(dic_2024)
dic_2025 = encontrar_contas_contabeis(df_2025)
print(dic_2025)



# Função auxiliar para imprimir tabelas comparativas 2024 vs 2025

def imprimir_tabela(titulo, ind_2025, ind_2024, nomes_formatos):
    print(f"\n{'='*60}")
    print(f"  {titulo}")
    print(f"{'='*60}")
    print(f"{'Indicador':<28} {'2025':>14} {'2024':>14}")
    print("-" * 60)
    for chave, (nome, fmt) in nomes_formatos.items():
        v25 = ind_2025[chave]
        v24 = ind_2024[chave]
        if fmt == 'pct':
            v25_str = f"{v25*100:.2f}%"
            v24_str = f"{v24*100:.2f}%"
        elif fmt == 'cur':
            v25_str = f"{v25:,.0f}"
            v24_str = f"{v24:,.0f}"
        elif fmt == 'dec':
            v25_str = f"{v25:.2f}"
            v24_str = f"{v24:.2f}"
        elif fmt == 'dec4':
            v25_str = f"{v25:.4f}"
            v24_str = f"{v24:.4f}"
        elif fmt == 'days':
            v25_str = f"{v25:.1f}"
            v24_str = f"{v24:.1f}"
        print(f"{nome:<28} {v25_str:>14} {v24_str:>14}")



# SEÇÃO 1 — INDICADORES DE PREÇO
# Entrada: O dicionário com as contas contábeis e o número de ações
# Saída: VPA e LPA (P/VPA e P/LPA requerem cotação de mercado)


def calcular_indicadores_preco(dic, n_acoes):
    # PL e Lucro Líquido vêm em milhares de R$, n_acoes em unidades.
    # Multiplicamos por 1000 para o resultado ficar em R$/ação.
    vpa = (dic['pl'] * 1000) / n_acoes
    lpa = (dic['lucro_liquido'] * 1000) / n_acoes

    return {
        'vpa': vpa,
        'lpa': lpa,
    }

n_acoes = 683_062_200

ind_preco_2024 = calcular_indicadores_preco(dic_2024, n_acoes)
ind_preco_2025 = calcular_indicadores_preco(dic_2025, n_acoes)

imprimir_tabela('INDICADORES DE PREÇO', ind_preco_2025, ind_preco_2024, {
    'vpa': ('VPA (R$/ação)', 'dec'),
    'lpa': ('LPA (R$/ação)', 'dec'),
})



# SEÇÃO 2 — INDICADORES DE RENTABILIDADE
# Entrada: Dicionários do ano atual e do ano anterior (para calcular médias)
# Saída: ROE, ROA, ROIC e ROCE


def calcular_indicadores_rentabilidade(dic_atual, dic_anterior):
    lucro_liquido = dic_atual['lucro_liquido']
    ebit = dic_atual['ebit']
    nopat = dic_atual['nopat']

    # Médias anuais
    pl_medio = (dic_atual['pl'] + dic_anterior['pl']) / 2
    at_medio = (dic_atual['ativo_total'] + dic_anterior['ativo_total']) / 2

    # Capital Investido = PL + Dívida Financeira Bruta (CP + LP)
    ci_atual = dic_atual['pl'] + dic_atual['divida_cp'] + dic_atual['divida_lp']
    ci_anterior = dic_anterior['pl'] + dic_anterior['divida_cp'] + dic_anterior['divida_lp']
    ci_medio = (ci_atual + ci_anterior) / 2

    # Capital Empregado = Ativo Total - Passivo Circulante
    ce_atual = dic_atual['ativo_total'] - dic_atual['passivo_circ']
    ce_anterior = dic_anterior['ativo_total'] - dic_anterior['passivo_circ']
    ce_medio = (ce_atual + ce_anterior) / 2

    roe = lucro_liquido / pl_medio
    roa = lucro_liquido / at_medio
    roic = nopat / ci_medio
    roce = ebit / ce_medio

    return {
        'roe': roe,
        'roa': roa,
        'roic': roic,
        'roce': roce,
        'ci_atual': ci_atual,
    }

ind_rent_2024 = calcular_indicadores_rentabilidade(dic_2024, dic_2023)
ind_rent_2025 = calcular_indicadores_rentabilidade(dic_2025, dic_2024)

imprimir_tabela('INDICADORES DE RENTABILIDADE', ind_rent_2025, ind_rent_2024, {
    'roe': ('ROE', 'pct'),
    'roa': ('ROA', 'pct'),
    'roic': ('ROIC', 'pct'),
    'roce': ('ROCE', 'pct'),
})



# SEÇÃO 3 — EVA (Economic Value Added)
# Entrada: Dicionário do ano atual e resultado da seção 2 (para reaproveitar CI e ROI)
# Saída: NOPAT, Capital Investido e ROI (WACC não disponível nos dados contábeis)


def calcular_eva(dic_atual, ind_rent):
    nopat = dic_atual['nopat']
    capital_investido = ind_rent['ci_atual']
    roi = ind_rent['roic']

    # EVA = (ROI - WACC) × Capital Investido
    # WACC não disponível nos dados contábeis — requer dados de mercado

    return {
        'nopat': nopat,
        'capital_investido': capital_investido,
        'roi': roi,
    }

eva_2024 = calcular_eva(dic_2024, ind_rent_2024)
eva_2025 = calcular_eva(dic_2025, ind_rent_2025)

imprimir_tabela('EVA (Economic Value Added)', eva_2025, eva_2024, {
    'nopat': ('NOPAT', 'cur'),
    'capital_investido': ('Capital Investido', 'cur'),
    'roi': ('ROI', 'pct'),
})



# SEÇÃO 4 — INDICADORES DE LIQUIDEZ
# Entrada: O dicionário com as contas contábeis calculadas
# Saída: CCL, LC, ARLP, LG, LS e LA


def calcular_indicadores_financeiros(dic):
    ativo_circ = dic['ativo_circ']
    passivo_circ = dic['passivo_circ']
    passivo_n_circ = dic['passivo_n_circ']
    intangivel = dic['intangivel']
    imobilizado = dic['imobilizado']
    investimento = dic['investimento']
    rlp = dic['rlp']
    estoque = dic['estoque']
    despesa_antecipada = dic['despesa_antecipada']
    caixa_equivalentes = dic['caixa_equivalentes']

    ccl = ativo_circ - passivo_circ
    lc = ativo_circ / passivo_circ
    # Ativo Permanente = Imobilizações (Investimento + Imobilizado + Intangível)
    # Usado depois na Imobilização do PL (Seção 6)
    ativo_permanente = intangivel + imobilizado + investimento
    # Liquidez Geral usa RLP (Realizável a Longo Prazo), não Ativo Permanente
    lg = (ativo_circ + rlp) / (passivo_circ + passivo_n_circ)
    ls = (ativo_circ - estoque - despesa_antecipada) / passivo_circ
    la = caixa_equivalentes / passivo_circ

    return {
        'ccl': ccl,
        'lc': lc,
        'rlp': rlp,
        'ativo_permanente': ativo_permanente,
        'lg': lg,
        'ls': ls,
        'la': la,
    }

ind_fin_2024 = calcular_indicadores_financeiros(dic_2024)
ind_fin_2025 = calcular_indicadores_financeiros(dic_2025)

imprimir_tabela('INDICADORES DE LIQUIDEZ', ind_fin_2025, ind_fin_2024, {
    'ccl': ('CCL', 'cur'),
    'lc': ('Liquidez Corrente', 'dec'),
    'rlp': ('RLP', 'cur'),
    'lg': ('Liquidez Geral', 'dec'),
    'ls': ('Liquidez Seca', 'dec'),
    'la': ('Liquidez Absoluta', 'dec'),
})



# SEÇÃO 5 — INDICADORES DE ATIVIDADE E CICLOS
# Entrada: Dicionário das contas e resultado da seção 4 (para reaproveitar CCL)
# Saída: PME, PMRV, PMPF, Ciclo Operacional, Ciclo Financeiro, NCG e ST


def calcular_indicadores_atividade(dic, ind_liq):
    estoque = dic['estoque']
    cmv = abs(dic['cmv'])
    contas_receber = dic['contas_receber']
    receita_liquida = dic['receita_liquida']
    fornecedores = dic['fornecedores']
    ativo_circ = dic['ativo_circ']
    passivo_circ = dic['passivo_circ']
    caixa_equivalentes = dic['caixa_equivalentes']
    divida_cp = dic['divida_cp']

    pme = (estoque / cmv) * 365
    pmrv = (contas_receber / receita_liquida) * 365
    pmpf = (fornecedores / cmv) * 365

    co = pme + pmrv
    cf = co - pmpf

    # NCG = Ativo Circulante Operacional - Passivo Circulante Operacional
    # ACO = AC sem caixa e aplicações financeiras
    # PCO = PC sem dívida financeira de curto prazo
    aco = ativo_circ - caixa_equivalentes
    pco = passivo_circ - divida_cp
    ncg = aco - pco

    ccl = ind_liq['ccl']
    st = ccl - ncg

    return {
        'pme': pme,
        'pmrv': pmrv,
        'pmpf': pmpf,
        'co': co,
        'cf': cf,
        'ncg': ncg,
        'st': st,
    }

ind_ativ_2024 = calcular_indicadores_atividade(dic_2024, ind_fin_2024)
ind_ativ_2025 = calcular_indicadores_atividade(dic_2025, ind_fin_2025)

imprimir_tabela('INDICADORES DE ATIVIDADE E CICLOS', ind_ativ_2025, ind_ativ_2024, {
    'pme': ('PME (dias)', 'days'),
    'pmrv': ('PMRV (dias)', 'days'),
    'pmpf': ('PMPF (dias)', 'days'),
    'co': ('Ciclo Operacional', 'days'),
    'cf': ('Ciclo Financeiro', 'days'),
    'ncg': ('NCG', 'cur'),
    'st': ('Saldo de Tesouraria', 'cur'),
})



# SEÇÃO 6 — ESTRUTURA DE CAPITAL E ENDIVIDAMENTO
# Entrada: Dicionário das contas e resultado da seção 4 (para reaproveitar ARLP)
# Saída: Relação de Capitais, Endividamento Geral, Solvência, Composição e Imobilização


def calcular_estrutura_capital(dic, ind_liq):
    passivo_total = dic['passivo_total']
    passivo_circ = dic['passivo_circ']
    pl = dic['pl']
    ativo_total = dic['ativo_total']

    relacao_capitais = passivo_total / pl
    endividamento_geral = passivo_total / (passivo_total + pl)
    solvencia_geral = ativo_total / passivo_total
    composicao_endividamento = passivo_circ / passivo_total
    # Imobilização do PL = Ativo Permanente / PL
    imobilizacao_pl = ind_liq['ativo_permanente'] / pl

    return {
        'relacao_capitais': relacao_capitais,
        'endividamento_geral': endividamento_geral,
        'solvencia_geral': solvencia_geral,
        'composicao_endividamento': composicao_endividamento,
        'imobilizacao_pl': imobilizacao_pl,
    }

est_cap_2024 = calcular_estrutura_capital(dic_2024, ind_fin_2024)
est_cap_2025 = calcular_estrutura_capital(dic_2025, ind_fin_2025)

imprimir_tabela('ESTRUTURA DE CAPITAL E ENDIVIDAMENTO', est_cap_2025, est_cap_2024, {
    'relacao_capitais': ('Relação de Capitais', 'dec'),
    'endividamento_geral': ('Endividamento Geral', 'pct'),
    'solvencia_geral': ('Solvência Geral', 'dec'),
    'composicao_endividamento': ('Composição Endiv.', 'pct'),
    'imobilizacao_pl': ('Imobilização do PL', 'pct'),
})



# SEÇÃO 7 — DRE RESUMIDA
# Entrada: Os dicionários dos 3 anos
# Saída: Tabela comparativa com variação 2025/2024


def calcular_dre_resumida(dic):
    return {
        'receita_liquida': dic['receita_liquida'],
        'lucro_bruto': dic['lucro_bruto'],
        'ebitda': dic['ebitda'],
        'ebit': dic['ebit'],
        'nopat': dic['nopat'],
        'lucro_liquido': dic['lucro_liquido'],
    }

dre_2023 = calcular_dre_resumida(dic_2023)
dre_2024 = calcular_dre_resumida(dic_2024)
dre_2025 = calcular_dre_resumida(dic_2025)

nomes = {
    'receita_liquida': 'Receita Líquida',
    'lucro_bruto': 'Lucro Bruto',
    'ebitda': 'EBITDA',
    'ebit': 'EBIT',
    'nopat': 'NOPAT',
    'lucro_liquido': 'Lucro Líquido',
}

print(f"\n{'Linha':<25} {'2025':>14} {'2024':>14} {'2023':>14} {'Var 25/24':>10}")
print("-" * 80)
for chave, nome in nomes.items():
    v25 = dre_2025[chave]
    v24 = dre_2024[chave]
    v23 = dre_2023[chave]
    var = ((v25 - v24) / abs(v24) * 100) if v24 != 0 else None
    var_str = f"{var:+.1f}%" if var is not None else "—"
    print(f"{nome:<25} {v25:>14,.0f} {v24:>14,.0f} {v23:>14,.0f} {var_str:>10}")
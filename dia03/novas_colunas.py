#%%
import pandas as pd

df = pd.read_csv('../data/customers.csv', sep=';')
df
# %%


df['Points_Double'] = df['Points'] * 2
df
# %%

df['Points_Rateio'] = df['Points_Double'] / df['Points']
df
# %%

def ranking_pontos(pontos):
    if pontos < 2500:
        return 'Baixo'
    elif pontos < 3500:
        return 'Medio'
    else:
        return 'Alta'


df['Faixa_Pontos '] = df['Points'].apply(ranking_pontos)
df
# %%

df['Name'] == 'anselmo_axo'

# %%

data ={
    'Nome':['Teo','Nah', 'Maria', 'Lara'],
    'recencia':[1, 30, 10, 45],
    'valor': [100, 2000, 15, 500],
    'frequencia': [2, 5 , 1, 15]
}

df_crm = pd.DataFrame(data)
df_crm
# %%

#%%
import pandas as pd

#%%
df_customers = pd.read_csv("../data/customers.csv", 
                 sep=";")
df_customers
#%%
df_customers.shape

# %%
df_customers.info(memory_usage='deep')

#%%
condicao = (df_customers["Points"] >= 10) & (df_customers["Points"] <= 50)
df_customers[condicao].shape


# %%
condicao = df_customers["Points"] == df_customers["Points"].max()
df_maior_point = df_customers[condicao]
df_maior_point['Name'].iloc[0]

# %%
colunas = df_customers.columns.tolist()
colunas.sort()
# %%
df_customers = df_customers[colunas]
df_customers
# %%

df_customers = df_customers.rename(columns={"Name": 'Nome',
                                            "Points": "Pontos"})
df_customers
# %%

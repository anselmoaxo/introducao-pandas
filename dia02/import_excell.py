#%%
import pandas as pd
# %%
df_transaction = pd.read_excel("../data/transactions.xlsx")
df_transaction
# %%
df_transaction.shape
# %%
df_transaction.columns.tolist()
# %%
df_transaction.rename(columns={"UUID": "ID",
                               "IdCustomer": "IdCliente",
                               "DtTransaction": "DtTransacao",
                               "Points": "Pontos"}, inplace=True)
df_transaction
# %%

colunas = ["ID",
           "Pontos",
           "IdCliente",
           "DtTransacao"]

df_transaction = df_transaction[colunas]
df_transaction.head()
# %%

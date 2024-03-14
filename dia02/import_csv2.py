#%%
import pandas as pd

df_products = pd.read_csv("../data/products.csv", sep=';',
                          names=['id', 'Name', 'Description'])
df_products
# %%

df_products.rename(columns={"Name": "Nome", 
                            "Description": "Descricao"},
                                inplace=True)
df_products
# %%

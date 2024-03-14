#%%
import pandas as pd


# %%
df = pd.read_csv("../data/ipea/homicidios.csv", sep=";")
df


# %%
df.shape
# %%
primeira = df.columns[0]
primeira
# %%
ultima = df.columns[-1]
ultima
# %%

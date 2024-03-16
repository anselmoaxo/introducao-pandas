#%%

import pandas as pd
import numpy as np

data = {
    'Nome': ['Anselmo', 'Priscila','Maria', 'Antonio'],
    'Idade': [42, np.nan , 81, np.nan],
    'Renda': [100, 250, np.nan, 500]  
}

df = pd.DataFrame(data)
df
# %%

df.isna().sum()
# %%

df.fillna({
    'Idade': df['Idade'].mean(),
    'Renda': df['Renda'].mean(),
})
# %%

#%%

import pandas as pd

data = {'Nome':["anselmo", "priscila", "joao", "priscila", "Maria", "anselmo"],
        'Idade':[32, 33, 2, 33, 31, 32],
        'update_at':[1, 2, 3, 1, 2, 3]

}

df = pd.DataFrame(data)
df
# %%
df = df.sort_values(by='update_at', ascending=False)
df
#%%
df.drop_duplicates(subset=['Nome', 'Idade'], keep='first')
# %%

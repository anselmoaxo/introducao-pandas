#%%
import pandas as pd


# %%
df = pd.read_excel('../data/transactions.xlsx')
df
# %%
import datetime


def recencia(data_transacao):
    diif = datetime.datetime.now() - data_transacao.max()
    return diif.days

(df.groupby(['IdCustomer']).agg(
    {
        'UUID': 'count',
        'Points': 'sum',
        'DtTransaction': ['max', recencia],
    }
).rename(columns={'Points': 'Valor',
                  'UUID': 'Frequencia',
                  'DtTransaction': 'UltimaData'}
).reset_index()
)


# %%

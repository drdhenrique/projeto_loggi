# %%

import json
from pathlib import Path
import pandas as pd

# %%
dados_df = []

caminho = Path('df')

for nome in caminho.glob('*.json'):
    with open(nome, 
          mode = 'r', 
          encoding = 'utf8') as file:
        dados_df.append(json.load(file))

# %%
dados_df[0]['deliveries']


# %%

df_deliveries_df = pd.DataFrame(dados_df)
# %%
df_deliveries_df
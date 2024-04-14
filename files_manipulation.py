# %%

import json
from pathlib import Path
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


px.set_mapbox_access_token(open("token.txt").read())

# %%
dados_df = []

# %%
caminho_base = Path('dados')

for i in range(10):  # Altere o número máximo de arquivos conforme necessário
    caminho_atual = caminho_base / f'df-{i}'
    for nome in caminho_atual.glob('*.json'):
        with open(nome, mode='r', encoding='utf8') as file:
            dados_df.append(json.load(file))

# %%
dados_df[0]['deliveries']

# %%

df_deliveries_df = pd.DataFrame(dados_df)
# %%
hub_origin = pd.json_normalize(df_deliveries_df['origin'])
hub_origin.head()
# %%
deliveries_df = pd.merge(left = df_deliveries_df, 
                         right = hub_origin, how = 'inner',
                         left_index= True, right_index= True)
deliveries_df.head()
# %%
deliveries_df = deliveries_df.drop('origin', axis = 1)
# %%
deliveries_df.head()
# %%
deliveries_df = deliveries_df[['name', 'region', 'lat', 'lng','vehicle_capacity', 'deliveries']]
deliveries_df.head()
# %%
deliveries_df.rename(columns={'lat':'hub_lat', 'lng':'hub_lng'}, inplace = True)
# %%
deliveries_df.head()

# %%
deliveries_df_exploded = deliveries_df[['deliveries']].explode('deliveries')
deliveries_df_exploded
# %%
deliveries_normalized_df = pd.concat([
  pd.DataFrame(deliveries_df_exploded["deliveries"].apply(lambda record: record["size"])).rename(columns={"deliveries": "delivery_size"}),
  pd.DataFrame(deliveries_df_exploded["deliveries"].apply(lambda record: record["point"]["lng"])).rename(columns={"deliveries": "delivery_lng"}),
  pd.DataFrame(deliveries_df_exploded["deliveries"].apply(lambda record: record["point"]["lat"])).rename(columns={"deliveries": "delivery_lat"}),
], axis= 1)
deliveries_normalized_df.head()
# %%
deliveries_normalized_df.shape
# %%
deliveries_df = deliveries_df.drop("deliveries", axis=1)
deliveries_df = pd.merge(left=deliveries_df, right=deliveries_normalized_df, how='right', left_index=True, right_index=True)
deliveries_df.reset_index(inplace=True, drop=True)
# %%
deliveries_df.head()

# %%
deliveries_df.shape
# %%

fig = px.scatter_mapbox(deliveries_df, 
                        lat="delivery_lat", 
                        lon="delivery_lng",
                        size_max=15, 
                        zoom=8, 
                        opacity=0.05)



fig.update_layout(height=800, 
                  mapbox=dict(center=go.layout.mapbox.Center(lat=-15.657014, lon=-47.802665)))
fig.show()
# %%
deliveries_df.info()

# %%
deliveries_df.to_csv('tidy_data.csv')
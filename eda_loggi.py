# %%

import pandas as pd
import numpy as np
# %%
df = pd.read_csv('tidy_data.csv')
df.drop('Unnamed: 0', inplace= True, axis = 1)
df.head()
# %%
df.describe()

# %%
capacidade = 180
df.drop('vehicle_capacity', axis = 1, inplace= True)

## Notemos que capacidade do veículo é constante, 
## logo não é informativa. 

# %%
df.info()
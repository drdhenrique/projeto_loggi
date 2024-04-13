# %%
import json
import pandas as pd
# %%

with open('df/df-90.json', 
          mode = 'r', 
          encoding = 'utf8') as file:
    df = json.load(file)

# %%
df
# %%
example = df[0]
print(example.keys())
# %%

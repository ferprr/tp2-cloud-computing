# %%
import pandas as pd
import numpy as np
import pickle


# %%
dataset = pd.read_csv("./Datasets/playlist-sample-ds2.csv")

# %%
pd.set_option('display.max_colwidth', 0)
columns = ['name', 'duration_ms', 'album_name', 'artist_name', 'track_name']
keepColumn = 'track_name'
columns.remove(keepColumn)
df2 = dataset.drop(columns, axis=1)
tracks = df2[keepColumn].unique()
playlists = df2['pid'].unique()
df2 = df2.groupby("pid")[keepColumn].apply(lambda x: list(x))
df2 = df2.to_frame()[keepColumn]
df2

# %%
from collections import defaultdict
ohe_df = defaultdict(dict)
for row in df2.keys():
    for music in df2[row]:
        if (len(ohe_df[music]) == 0):
            ohe_df[music] = []
        ohe_df[music].append(row)
# ohe_df['Breezeblocks']
playlists_musics_df = defaultdict(dict)

for p in playlists:
    for t in tracks:
        if (len(playlists_musics_df[t]) == 0):
            playlists_musics_df[t] = []
        if p in ohe_df[t]:
            playlists_musics_df[t].append(1)
        else:
            playlists_musics_df[t].append(0)

# %%
freq_df = pd.DataFrame.from_dict(playlists_musics_df, orient='index', columns=playlists).transpose()
freq_df

# %%
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

freqItems = apriori(freq_df, min_support=0.01, use_colnames=True, verbose=1)
freqItems.sort_values('support')

# %%
rules = association_rules(freqItems, metric="confidence", min_threshold=0.01)
#rules = rules[rules['support'] >= 0.015]
with open('./trained_model.pkl', 'wb') as file:
    pickle.dump(rules, file)

# %%




import pandas as pd
import glob
import os, sys

# ouvre un fichier
path = "../../data/raw"
dirs = os.listdir(path)

for x in dirs:
    print("liste" + x)

# Lit les fichiers CSV
data1 = pd.read_csv('../../data/raw/youtube-1.csv', header=None)
data2 = pd.read_csv('../../data/raw/youtube-2.csv', header=None)
data3 = pd.read_csv('../../data/raw/youtube-3.csv', header=None)
data4 = pd.read_csv('../../data/raw/youtube-4.csv', header=None)
data5 = pd.read_csv('../../data/raw/youtube-5.csv', header=None)

# fusion des fichiers
df = pd.concat([data1, data2, data3, data4, data5], ignore_index=False)

# Affichage de la fusion
print('Les fichiers ont bien étés fusionnés')
print(df)

# Création du fichier des CSV fusionnés
df.to_csv('../../data/processed/processed1.csv', encoding='utf-16', index=True)

# Lecture et affichage du fichier final
df2 = pd.read_csv('../../data/processed/processed1.csv', encoding='utf-16',low_memory=False )
print(df2)

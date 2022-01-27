import pandas as pd

df = pd.read_csv('../../data/processed/processed.csv', encoding='utf-16',sep=',')

print (df['likes'].nlargest(5))
print(df.info())

vabr = 0

for a in df['video_id']:
    if len(a) !=11:
        vabr +=1
    else :
        pass

for c in df['trending date']:
       pass
print(vabr)
import collections
import json
import pandas as pd

inno_tasks = []
ml_tasks = []

df = pd.read_csv('index_terms_list.csv')
df['innovation data task'] = df['innovation data task'].str.split(',')
df['ML task'] = df['ML task'].str.split(',')



df_inno = df.explode(['innovation data task']).reset_index(drop=True)
df_inno['innovation data task'] = df_inno['innovation data task'].str.strip()


df_ml = df.explode(['ML task']).reset_index(drop=True)
df_ml['ML task'] = df_ml['ML task'].str.strip()


print(df_inno['innovation data task'].value_counts())
print(df_ml['ML task'].value_counts())
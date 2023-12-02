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

# for line in open('inno_task.txt', 'r').readlines():
# 	inno_tasks.append(line.strip())


# for line in open('ml_task.txt', 'r').readlines():
# 	ml_tasks.append(line.strip())


# inno_counter = collections.Counter(inno_tasks)
# ml_counter = collections.Counter(ml_tasks)

# print(json.dumps({k: v for k, v in sorted(inno_counter.items(), key=lambda item: item[1], reverse=True)}, indent=2))
# print(json.dumps({k: v for k, v in sorted(ml_counter.items(), key=lambda item: item[1], reverse=True)}, indent=2))

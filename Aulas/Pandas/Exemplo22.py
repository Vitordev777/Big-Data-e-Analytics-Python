import random as rd
import pandas as pd

dados={'estado':['SP', 'MG','PR','SP','MG','PR'],
       'ano':[2019, 2019,2019, 2020,2020,2020],
       'pop':[45.9, 21.2,16.9,46.6,21.4,17.3]}
df1=pd.DataFrame(dados)

df1.loc[df1['estado'] == 'PR',['Sál.Med']] = 3000

valor_alt = df1['estado'].sample(3).index

df1.loc[valor_alt, 'Sál.Med'] = [rd.randint(2000,6000) for i in valor_alt]
print(df1)


df1['Sál.Med'] = df1['Sál.Med'].fillna(int(df1['Sál.Med'].mean()))
print(df1)
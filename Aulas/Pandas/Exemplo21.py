import pandas as pd

dados={'estado':['SP', 'MG','PR','SP','MG','PR'],
       'ano':[2019, 2019,2019, 2020,2020,2020],
       'pop':[45.9, 21.2,16.9,46.6,21.4,17.3]}
df1=pd.DataFrame(dados)

df1.loc[df1['estado'] == 'SP',['estimativa']] = '4'
print(df1.loc[df1['estado'] == 'SP',['estimativa']])

print(df1.sort_values(by='pop', ascending=False))



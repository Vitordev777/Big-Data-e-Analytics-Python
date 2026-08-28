import pandas as pd

dados={'estado':['SP', 'MG','PR','SP','MG','PR'],
       'ano':[2019, 2019,2019, 2020,2020,2020],
       'pop':[45.9, 21.2,16.9,46.6,21.4,17.3]}
df1=pd.DataFrame(dados)

df2=pd.DataFrame(dados,columns=['ano','estado','pop'])
df2['estimativa']=50

#Analisar o DataFrame

print(df2.describe(include='all'))
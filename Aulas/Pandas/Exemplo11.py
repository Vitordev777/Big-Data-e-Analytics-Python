import pandas as pd
import numpy as np

dados={'estado':['SP', 'MG','PR','SP','MG','PR'],
       'ano':[2019, 2019,2019, 2020,2020,2020],
       'pop':[45.9, 21.2,16.9,46.6,21.4,17.3]}
df1=pd.DataFrame(dados)

df2=pd.DataFrame(dados,columns=['ano','estado','pop'])

#Copiando o Dataframe df2 para o Dataframe df3
df3=df2
print(df3)

#Selecionando apenas a coluna 'ano' do Dataframe df2
df3=df2[['ano']]
print(df3)

#O tipo do objeto df3 é um Dataframe
print(type(df3))
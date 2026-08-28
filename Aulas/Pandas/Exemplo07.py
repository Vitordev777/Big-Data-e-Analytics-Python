import pandas as pd

dados={'estado':['SP', 'MG','PR','SP','MG','PR'],
       'ano':[2019, 2019,2019, 2020,2020,2020],
       'pop':[45.9, 21.2,16.9,46.6,21.4,17.3]}
df1=pd.DataFrame(dados)

#Visualizar partes do Dataframe


#Visualizar as 2 primeiras linhas do Dataframe
print(df1.head(2))

#Visualizar as 2 últimas linhas do Dataframe
df1.tail(2)

#visualizar uma amostra aleatória de 2 linhas do Dataframe
df1.sample(2)
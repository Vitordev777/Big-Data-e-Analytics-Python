import pandas as pd

dados={'estado':['SP', 'MG','PR','SP','MG','PR'],
       'ano':[2019, 2019,2019, 2020,2020,2020],
       'pop':[45.9, 21.2,16.9,46.6,21.4,17.3]}
df1=pd.DataFrame(dados)

df2=pd.DataFrame(dados,columns=['ano','estado','pop'])
df2['estimativa']=50

#Alterar Informação das Colunas
df2['ano']=df2['ano']+2
print(df2)

#Mostrar apenas os dados do DataFrame df2 com ano maior que 2021
print(df2[df2['ano']>2021])

#Selecionar apenas os dados do DataFrame df2 com ano maior que 2021
df4=df2[(df2['ano']>2021)]
print(df4)



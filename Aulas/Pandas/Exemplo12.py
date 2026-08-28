import pandas as pd

dados={'estado':['SP', 'MG','PR','SP','MG','PR'],
       'ano':[2019, 2019,2019, 2020,2020,2020],
       'pop':[45.9, 21.2,16.9,46.6,21.4,17.3]}
df1=pd.DataFrame(dados)

df2=pd.DataFrame(dados,columns=['ano','estado','pop'])

#Criando uma nova coluna no Dataframe df2, chamada 'Não Paraná', 
#que recebe o valor True para os estados diferentes de 'PR' 
#e False para o estado 'PR'

df2['Não Paraná']= df2.estado != 'PR'
print(df2)

#Excluir Coluna do Dataframe df2
del df2['Não Paraná']
print(df2)
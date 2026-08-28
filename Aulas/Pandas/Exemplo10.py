#Atribuir Valores

import pandas as pd
import numpy as np

dados={'estado':['SP', 'MG','PR','SP','MG','PR'],
       'ano':[2019, 2019,2019, 2020,2020,2020],
       'pop':[45.9, 21.2,16.9,46.6,21.4,17.3]}
df1=pd.DataFrame(dados)

df2=pd.DataFrame(dados,columns=['ano','estado','pop'])

#Adicionando uma nova coluna ao Dataframe df2 com o valor 50 para todas as linhas
df2['estimativa']=50
print(df2)

#Adicionando uma nova coluna ao Dataframe df2 com valores diferentes para cada linha
df2['estimativa']=np.arange(6)
print(df2)
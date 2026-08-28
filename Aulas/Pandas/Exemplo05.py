import pandas as pd

s2=pd.Series([1,2,-5,0], index=['a','b', 'c', 'd'])

#Algebra de conjuntos

print(s2*2)

#Identificando valores nulos
print(s2.isnull())
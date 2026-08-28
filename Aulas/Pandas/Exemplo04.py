import pandas as pd

s2=pd.Series([1,2,-5,0], index=['a','b', 'c', 'd'])

#Comparação de valores
print(s2[s2>0])
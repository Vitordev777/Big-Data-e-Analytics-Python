import pandas as pd

s2=pd.Series([1,2,-5,0], index=['a','b', 'c', 'd'])

s2['a']=1000

print(s2.values)
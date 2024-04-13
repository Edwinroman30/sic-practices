import pandas as pd

''' 
## Q 34-01
Convierta los siguientes datos del diccionario en un dataframe usando **Pandas**.
(Denomina el dataframe `df`)
`d = { 'col1':[1,2], 'col2':[3,4], 'col3':[5,6], 'col4':[7,8] }`
'''
d = { 'col1':[1,2], 'col2':[3,4], 'col3':[5,6], 'col4':[7,8] }

df = pd.DataFrame.from_dict(d)
df.reindex(index= ["Primero", "Segundo"])
df.isnull()
print(df)

import os
import pandas as pd

path = r'H:\videos\detection'
dirs = os.listdir(path)
for dir in dirs:
    print(dir)
dataframe=pd.DataFrame({'Frame':dirs})
dataframe.to_csv(r'H:\videos\file\detection1.csv',index=True,sep=',')
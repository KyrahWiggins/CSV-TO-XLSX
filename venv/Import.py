import pandas as pd
import numpy as np

# Reading the csv file
df_new = pd.read_csv('Car_sales.csv')

# saving xlsx file
GFG = pd.ExcelWriter('Car_sales.xlsx')
df_new.to_excel(GFG, index=False)

GFG.save()
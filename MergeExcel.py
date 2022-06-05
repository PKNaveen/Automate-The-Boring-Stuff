import pandas as pd
files = ['']
combined = pd.DataFrame()

for file in files:
  df = pd.read_excel(file, skiprows = 3)
  combined = combined.append(df, ignore_index = True)
  

combined.to_excel('combined.xlsx')
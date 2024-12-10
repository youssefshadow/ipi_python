import pandas as pd


df = pd.read_excel('./db/transactions.xlsx')


df['price'] = df['price'].replace({r'\$': '', r'€': ''}, regex=True)  
df['price'] = df['price'].str.replace(',', '.').astype(float)  


df['Corrected'] = df['price'] * 0.9


df.to_excel('modified_file.xlsx', index=False)

print(" modified_file.xlsx")

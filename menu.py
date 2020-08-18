import pandas as pd

excelik = pd.ExcelFile('menucka.xlsx')
kategorie = excelik.sheet_names

print('kategorie su: \n', kategorie)

for sheet in kategorie:
    df=pd.read_excel(excelik, sheet_name=sheet, header=None, index=0)
    
    for riadok in df.values:
        print(sheet, '-', riadok)

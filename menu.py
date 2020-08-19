import pandas as pd

excelik = pd.ExcelFile('menucka.xlsx')
kategorie = excelik.sheet_names
print('Kategorie su: ', kategorie)

myfile=open('vypis.txt', 'w')

for sheet in kategorie:
    df=pd.read_excel(excelik, sheet_name=sheet, header=None)
    
    for riadok in df.values:
        if riadok[0][-1]=='/':     #ak je na konci skutocne /
            r=riadok[0].rsplit('/', 2)[0]
        else:                      #ak na konci nie je /, teda ziadne alergeny
            r=riadok[0]
        myfile.write(' '.join((sheet, '-', r, '\n')))

myfile.close()
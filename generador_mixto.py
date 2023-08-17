import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

headers = ["n", "Xo", "(aXo + C)modM", "Xn + 1", "Num Rectangulares"]
sheet.append(headers)
data = []

def generador(a, Xo, C, m):
    print('\nn | Xo | (aXo + C)modM | Xn + 1 | Num Rectangulares')
    last_seed = Xo
    for i in range(1, m + 1):
        cociente = int(((a * last_seed) + C) / m)
        residuo = ((a * last_seed) + C) % m
        data.append([i, last_seed, f'{cociente} + {residuo}/{m}', residuo, f'{residuo}/{m} = {round(residuo/m, 5)}'])
        print(f'{i} |  {last_seed} |    {cociente} + {residuo}/{m}    |    {residuo}   | {residuo}/{m} = {round(residuo/m, 5)}')
        last_seed = residuo
        if residuo == Xo:
            if i == m:
                print('\nGenerador congruencial Mixto confiable o Generador con periodo completo')
                data.append([' ', ' ', ' ', ' ', ' ', 'Generador congruencial Mixto confiable o Generador con periodo completo'])
            else:
                print('\nGenerador congruencial Mixto no confiable o Generador con periodo incompleto')
                data.append([' ', ' ', ' ', ' ', ' ', 'Generador congruencial Mixto no confiable o Generador con periodo incompleto'])
            break

def save_xlsx():
    for row in data:
        sheet.append(row)
    wb.save("files/generador_mixto.xlsx")

if __name__ == "__main__":
    generador(5, 4, 7, 8)
    save_xlsx()
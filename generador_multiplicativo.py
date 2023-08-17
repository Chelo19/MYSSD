import openpyxl
import math

wb = openpyxl.Workbook()
sheet = wb.active

headers = ["n", "Xo", "(aXo)modM", "Xn + 1", "Num Rectangulares"]
sheet.append(headers)
data = []

def generador(a, Xo, m):
    print('\nn | Xo | (aXo)modM | Xn + 1 | Num Rectangulares')
    last_seed = Xo
    if(((m & (m - 1)) == 0)):
        pe = int(m / 4)
    else:
        exp = int(math.floor(math.log10(m)))
        if(exp >= 5):
            pe = 5 * pow(10, exp - 2)
        else:
            lambda5 = pow(5, exp - 1) * (4)
            lambda2 = pow(2, exp - 2)
            pe = (lambda5 * lambda2) // math.gcd(lambda5, lambda2)


    for i in range(1, pe + 1):
        cociente = int(((a * last_seed)) / m)
        residuo = ((a * last_seed)) % m
        data.append([i, last_seed, f'{cociente} + {residuo}/{m}', residuo, f'{residuo}/{m} = {residuo/m}'])
        print(f'{i} |  {last_seed} |    {cociente} + {residuo}/{m}    |    {residuo}   | {residuo}/{m} = {residuo/m}')
        last_seed = residuo
        if residuo == Xo:
            if i == pe:
                print('\nGenerador congruencial Multiplicativo confiable o Generador con periodo completo')
                data.append([' ', ' ', ' ', ' ', ' ', 'Generador congruencial Multiplicativo confiable o Generador con periodo completo'])
            else:
                print('\nGenerador congruencial Multiplicativo no confiable o Generador con periodo incompleto')
                data.append([' ', ' ', ' ', ' ', ' ', 'Generador congruencial Multiplicativo no confiable o Generador con periodo incompleto'])
            break

def save_xlsx():
    for row in data:
        sheet.append(row)
    wb.save("files/generador_multiplicativo.xlsx")

if __name__ == "__main__":
    generador(5, 5, 32)
    save_xlsx()
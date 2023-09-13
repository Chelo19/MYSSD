import math

Ex = []
X = []
nSize = []
f12d3 = []
zAlpha = []

def promedio_numeros():
    with open('files/nums.txt', 'r') as txt:
        nums = [float(line.strip()) for line in txt]
    nSize.append(len(nums))
    Ex.append(sum(nums))
    X.append(sum(nums) / len(nums))

def zo():
    f1 = (X[0] - 0.5)
    f2 = math.sqrt(nSize[0])
    f3 = math.sqrt(1 / 12)
    f12 = f1 * f2
    f12d3.append(abs(f12 / f3))

def getAlphaReal():
    alphaDato = int(input("Ingresa alphaDato: "))
    alphaReal = (100 - alphaDato) / 100 / 2
    print('Alfa real es:',alphaReal)
    zAlpha.append(float(input("Ingresa Zalfa: ")))

def compare():
    print(f'{f12d3[0]} < {zAlpha[0]}')
    if(f12d3[0] < zAlpha[0]):
        print('Los numeros son aceptados')
    else:
        print('Los numeros no son aceptados')

if __name__ == "__main__":
    promedio_numeros()
    zo()
    getAlphaReal()
    compare()
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

headers = ["i", "Xi", "F(Xi) = i / N", "Dn = max | F(Xi) - Xi |"]
sheet.append(headers)

sortedNums = []
data = []
dAlphaN = []

def sortNums():
    with open('files/nums.txt', 'r') as txt:
        nums = [float(line.strip()) for line in txt]
    nums.sort()
    sortedNums.append(nums)

def generate():
    getDAlphaN()
    max = 0
    print('\ni | Xi | F(Xi) = i / N | Dn = max | F(Xi) - Xi')
    for i in range(len(sortedNums[0])):
        if(round((i + 1) / len(sortedNums[0]) - sortedNums[0][i], 5) > max):
            max = round((i + 1) / len(sortedNums[0]) - sortedNums[0][i], 5)
        data.append([{i + 1}, sortedNums[0][i], f'{i + 1} / {len(sortedNums[0])} = {(i + 1) / len(sortedNums[0])}', f'{(i + 1) / len(sortedNums[0])} - {sortedNums[0][i]} = {round((i + 1) / len(sortedNums[0]) - sortedNums[0][i], 5)}'])
        print(f'{i + 1} | {sortedNums[0][i]} | {i + 1} / {len(sortedNums[0])} = {(i + 1) / len(sortedNums[0])} | {(i + 1) / len(sortedNums[0])} - {sortedNums[0][i]} = {round((i + 1) / len(sortedNums[0]) - sortedNums[0][i], 5)}')
    checkIfAccepted(max)

def getDAlphaN():
    print('n es:', len(sortedNums[0]))
    int(input("Ingresa alfa: "))
    dAlphaN.append(float(input("Ingresa DAlfaN: ")))

def checkIfAccepted(max):
    print(f'{max} < {dAlphaN[0]}')
    if(max < dAlphaN[0]):
        print('Los numeros son aceptados')
    else:
        print('Los numeros no son aceptados')


if __name__ == "__main__":
    sortNums()
    generate()
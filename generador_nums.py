import random

def generator():
    n = int(input("Ingresa n: "))
    
    with open('files/nums.txt', 'w') as archivo_txt:
        for _ in range(n):
            numero_aleatorio = round(random.uniform(0, 1), 5)
            archivo_txt.write(f'{numero_aleatorio}\n')

if __name__ == "__main__":
    generator()

n = int(input('informe o número de parcelas:'))
pares = 0
impares = 1

for i in range(1, n + 1):
    x = int(input(f'Digite o valor de x{i}:'))
    if x % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f'O valor de números pares é: {pares} e ímpares é {impares}')
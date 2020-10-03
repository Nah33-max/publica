matriz = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
spar = scol = 0
for l in range(0, 6):
    for c in range(0, 5):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' *30)
for l in range(0,6):
    for c in range(0,5):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=' * 30)

for l in range(0, 6):
        scol += matriz[l][1]
print(f'A soma do mínimo da temporada é {scol}')

for l in range(0, 6):
    scol += matriz[l][2]
print(f'A soma do máximo da temporada é {scol}')

for l in range(0, 6):
    scol += matriz[l][3]
print(f'O recorde mínimo foi quebrado {scol} vezes.')

for l in range(0, 6):
    scol += matriz[l][4]
print(f'O recorde máximo foi quebrado {scol} vezes.')
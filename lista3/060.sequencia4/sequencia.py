#Faça um programa que imprima a sequência como no exemplo a seguir.

i = 0
j = 1

for j in range(1, 3 + 1):
    print(f'I={i} J={j}')

i = 0.2
j1 = 1.2
j2 = 2.2
j3 = 3.2

while i < 2:
    print(f'I={i:.1f} J={j1:.1f}')
    print(f'I={i:.1f} J={j2:.1f}')
    print(f'I={i:.1f} J={j3:.1f}')
    print("=" * 10)
    i += 0.2
    j1 += 0.2
    j2 += 0.2
    j3 += 0.2


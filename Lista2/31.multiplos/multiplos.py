#Leia dois valores inteiros (A e B). Após, o programa deve imprimir a mensagem “Sao Multiplos” (são múltiplos) ou “Nao são Multiplos” (não são múltiplos), correspondente aos valores lidos.

from audioop import mul


a, b = input().split(' ')

a = int(a)
b = int(b)

for c in range(0, b):
    if c * a == b:
        multiplos = c * a
        print(multiplos)

if multiplos == b:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
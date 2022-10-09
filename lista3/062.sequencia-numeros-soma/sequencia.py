#Ler um número indeterminado de pares de valores M e N (parar quando algum desses valores for menor ou igual a zero). Para cada par, imprima a sequência do menor para o maior (incluindo ambos) e a soma de inteiros consecutivos entre eles (incluindo ambos).


while True:
    m, n = map(int, input().split(' '))

    if m <= 0 or n <= 0:
        break
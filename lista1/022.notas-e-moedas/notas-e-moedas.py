#Leia um valor de ponto flutuante com duas casas decimais. Isso representa um valor monetário. Depois disso, calcule o menor número possível de notas e moedas em que o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0,50, 0,25, 0,10, 0,05 e 0,01. Imprima a mensagem “NOTAS:” seguida da lista de notas e a mensagem “MOEDAS:” seguida da lista de moedas.

valor = float(input('Seu valor: R$'))
cedula = valor

notas = [100, 50, 20, 10, 5, 2]
moedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]

print('NOTAS:')
for nota in notas:
    cedula = int(valor / nota) #transforma o resultado em inteiro, esse é a quantidade de notas
    print(f'{cedula} nota(s) de R$ {nota}.00')
    valor -= cedula * nota

print('MOEDAS:')
for moeda in moedas:
    cedula = int(valor / moeda) #transforma o resultado em inteiro, esse é a quantidade de moedas
    print(f'{cedula} moeda(s) de R$ {moeda:.2f}')
    valor -= cedula * moeda


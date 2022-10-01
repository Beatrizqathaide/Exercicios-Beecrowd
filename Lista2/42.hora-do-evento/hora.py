'''
Peter está organizando um evento em sua universidade. O evento será no mês de abril, começando e terminando no mês de abril. O problema é: Peter quer calcular a duração do evento em segundos, sabendo obviamente o horário de início e término do evento.

Você sabe que o evento pode levar de alguns segundos a alguns dias, portanto, você deve ajudar Peter a calcular o tempo total correspondente à duração do evento.

Obs: Considere que o evento do caso de teste tem a duração mínima de um minuto.
'''

diaInicio = int(input().split()[1]) #transforma em lista para pegar somente o número
horaInicio, minutoInicio, segundoInicio = input().split(':')

diaFim = int(input().split()[1])
horaFim, minutoFim, segundoFim = input().split(':')


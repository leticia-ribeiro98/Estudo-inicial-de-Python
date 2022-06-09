#Escreva um programa que solicita ao usuário um intervalo de tempo em segundos e o programa imprime na tela o valor correspondente em horas, minutos e segundos.


# -*- coding: utf-8 -*-

seg = int (input ('Digite o valor do tempo em segundos: '))

#transformar segundos em horas
horas = int (seg / 3600)

#Calcular os segundos restantes, pois as horas estão em inteiros e transforma-los em minutos
segresto1 = seg - (horas*3600)
minutos = int (segresto1 / 60)

#Cacular os segundos restantes, pois os minutos estão em inteiros.
segresto2 = segresto1 - (minutos*60)

print ('Valor convertido: %d h %d min %d s' % (horas, minutos, segresto2))

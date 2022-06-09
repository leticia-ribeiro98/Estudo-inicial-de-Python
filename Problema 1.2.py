#Escreva um programa que solicita ao usuário um valor de velocidade (v0), um valor de aceleração (a) e
#um valor de tempo (t) e o programa imprime na tela a velocidade final e a distância percorrida por um
#veículo após o intervalo de tempo t, com velocidade inicial igual a v0 e aceleração igual a a. Considere
#as seguintes fórmulas:

#Velocidade final: v = v0 + a × t
#Distância percorrida: s = v0 × t + (a×t**2/2)

# -*- coding: utf-8 -*-

vel = float (input ('Digite o valor da velocidade: '))
acel = float (input ('Digite o valor da aceleração: '))
temp = float (input ('Digite o valor do tempo: '))

#velocidade final
v = float (vel + (acel * temp))
print ('Velocidade final: %.2f' % v)

#Distância percorrida
s =  float ((vel*temp) + ((acel*(temp**2))/2))
print ('Distância percorrida: %.2f' % s)

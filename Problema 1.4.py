#Escreva um programa que solicita ao usuário um número inteiro de 4 algarismos e o programa imprime na tela o seu valor invertido.

# -*- coding: utf-8 -*-

num = int (input ('Digite um inteiro de 4 algarismos: '))

unid = num % 10
dez = int ((num % 100)/10)
cent = int ((num % 1000)/100)
milhar = int ((num/1000))

inverter = (1000 * unid) + (100 * dez) + (10 * cent) + milhar

print ('Valor invertido: %d' % inverter)

# -*- coding: utf-8 -*-

#Escreva um programa que solicita ao usuário três números inteiros e imprime na tela o número do meio (mediana).

num1 = int (input ('Digite o primeiro número: '))
num2 = int (input ('Digite o segundo número: '))
num3 = int (input ('Digite o terceiro número: '))

if (num2 <= num1 <= num3):
    print ('Mediana: %d' % num1)
elif (num3 <= num1 <= num2):
    print ('Mediana %d' % num1)
elif (num1 <= num2 <= num3):
    print ('Mediana: %d' % num2)
elif (num3 <= num2 <= num1):
    print ('Mediana: %d' % num2)
elif (num1 <= num3 <= num2):
    print ('Mediana: %d' % num3)
elif (num2 <= num3 <= num1):
    print ('Mediana: %d' % num3)

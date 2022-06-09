#Escreva um programa que solicita ao usuário um número inteiro de 4 algarismos e imprime na tela a soma destes algarismos.

# -*- coding: utf-8 -*-

num = int (input ('Digite um inteiro de 4 algarismos: '))

unid = num % 10
dez = int ((num % 100)/10)
cent = int ((num % 1000)/100)
milhar = int ((num/1000))

somar = unid + dez + cent + milhar

print ('Resultado: %d' % somar)

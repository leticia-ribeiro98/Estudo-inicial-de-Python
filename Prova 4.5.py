#Escreva um programa que faça a leitura de vários números inteiros até que se digite um número negativo. Em seguida, o programa deve imprimir na tela o maior e o menor número lido.

# -*- coding: utf-8 -*-

maior_ate_agora = 0 #para armazenar o maior valor nesta variável
menor_ate_agora = 10000000 #para armazenar o menor valor nesta variável
num = 1 #numero inicial

while num >= 0:
    num = int (input ('Digite um número: '))
    
    if num < 0:
        break
    if num > maior_ate_agora:
        maior_ate_agora = num
    if num < menor_ate_agora:
        menor_ate_agora = num

print ('Maior: %.d' % maior_ate_agora)
print ('Menor: %.d' % menor_ate_agora)

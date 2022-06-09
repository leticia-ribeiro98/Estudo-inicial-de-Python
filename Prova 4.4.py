#Escreva um programa que leia dois números inteiros x e y e imprima na tela todos os números que
#possuem raiz quadrada inteira entre eles (inclusive x e y).

# -*- coding: utf-8 -*-

x = int (input ('Digite o valor de x: '))
y = int (input ('Digite o valor de y: '))

for raiz in range (x, y+1):
    calculo = int (raiz ** (1/2))
    
    if (calculo**2 == raiz):
        print (raiz)

#Faça um programa que leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número e exiba o resultado com três casas decimais. Se o número for negativo, exiba
#a mensagem "Número inválido". O programa não deve imprimir nada além disso na tela.

# -*- coding: utf-8 -*-

num = float (input ('Digite um número: '))

if (num >= 0):
    raiz = num ** (1/2)
    print ('Resultado %.3f' % raiz)
else:
    print ('Número inválido')

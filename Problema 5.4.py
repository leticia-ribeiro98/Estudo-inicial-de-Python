#Faça um programa que solicite o nome do usuário e imprima-o na vertical.

# -*- coding: utf-8 -*-

palavra = input ('')
tamanho = len (palavra)

for c in range (0,tamanho):
    letra = palavra[c]
    print (letra)

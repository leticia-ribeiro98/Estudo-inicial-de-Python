#Altere o programa anterior de modo que a escada seja invertida

# -*- coding: utf-8 -*-

palavra = input ('')
tamanho = len (palavra)

for c in range (0,tamanho):
    subtração = palavra[:tamanho-c]
    print (subtração)

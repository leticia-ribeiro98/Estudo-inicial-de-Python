#Modifique o programa anterior de forma a mostrar o nome em formato de escada.

# -*- coding: utf-8 -*-

palavra = input ('')
tamanho = len (palavra)

for c in range (0,tamanho):
    letra = palavra[c]
    soma = palavra [:c+1]
    print (soma)

#Escreva um programa que lê duas strings e imprime na tela as strings combinadas, alternando as letras de cada string, começando com a primeira letra da primeira string, seguido pela primeira letra da
#segunda string, em seguida pela segunda letra da primeira string, e assim sucessivamente. As letras
#restantes da string mais longa devem ser adicionadas ao final da string resultante.

# -*- coding: utf-8 -*-

palavra1 = input ('Digite a primeira palavra: ')
palavra2 = input ('Digite a segunda palavra: ')

tamanho1 = len (palavra1)
tamanho2 = len (palavra2)
c = 0
resultado = ''

if tamanho1 >= tamanho2: 
    while c < tamanho2:
        letra1 = palavra1[c]
        letra2 = palavra2[c]
        c += 1
        resultado += letra1 + letra2
    while c < tamanho1: #inserir mais um while pra continuar inserido as letras da primeira palavra na palavra final
        letra1 = palavra1[c]
        c += 1
        resultado += letra1
    
    print ('Combinação: %s' % resultado)
    
else:
    while c < tamanho1:
        letra1 = palavra1[c]
        letra2 = palavra2[c]
        c += 1
        resultado += letra1 + letra2
    while c < tamanho2: #inserir mais um while pra continuar inserido as letras da segunda palavra na palavra final
        letra2 = palavra2[c]
        c += 1
        resultado += letra2
    print ('Combinação: %s' % resultado)

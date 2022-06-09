#Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da esquerda para a direita ou da direita para a esquerda. Por exemplo: OSSO e OVO são palíndromos. Escreva um programa
#que leia uma string e imprima na tela se ela é um palíndromo ou não

# -*- coding: utf-8 -*-

palavra = input ('')

if palavra == palavra [::-1]:
    print ('É palíndromo')
else:
    print ('Não é palíndromo')

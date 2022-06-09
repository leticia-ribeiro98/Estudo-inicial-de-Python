#Crie um programa que recebe uma string e substitui todas as ocorrências de letras repetidas (consecutivamente) por uma única ocorrência da mesma em maiúscula.
#Observação: as mensagens exibidas para o usuário deverão ser exatamente como apresentado abaixo
#(mensagens exibidas com os comandos input() e print()).

# -*- coding: utf-8 -*-

palavra = input ('')
c = 0
letra = ''

while c < len (palavra):
    if c + 1 < len (palavra):
        if palavra[c] == palavra[c + 1]:
            letra = letra + palavra[c].upper()
            c = c + 2
        else:
            letra = letra + palavra[c]
            c = c + 1
    else:
        letra = letra + palavra[c]
        break
print (letra)

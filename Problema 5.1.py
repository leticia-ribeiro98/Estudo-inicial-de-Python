#Crie um programa que receba um nome completo e o imprima no seguinte formato: "sobrenome",
#"primeiro nome e nome do meio". Dica: utilize a função rfind().

# -*- coding: utf-8 -*-

nome = input ('')

#procurar o útimo nome
ult_esp = nome.rfind (' ')
inicio_sobrenome = ult_esp + 1
sobrenome = nome[inicio_sobrenome:]

#primeiros nomes
primeiros_nome = nome[:ult_esp]

print ('Nome formatado: %s, %s' % (sobrenome, primeiros_nome))

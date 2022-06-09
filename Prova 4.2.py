#Em Matemática, o número harmônico designado por H(n) é definido# como sendo a soma da série harmônica
#Faça um programa que lê um valor inteiro e positivo n e imprime o valor de H(n), com duas casas decimais.

# -*- coding: utf-8 -*-

num = int (input ('Digite n: '))
contador = 1
soma = 0

for hn in range (contador, num+1):
    calculo = 1/hn
    soma = soma + calculo
    
print ('Resultado: %.2f' % soma)

#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os valores dos reajustes. Faça um programa que
#receba o salário de um colaborador, calcula o reajuste segundo a tabela abaixo, e exibe o valor do aumento e o valor do novo salário.
#Salário atual Porcentagem de aumento
#Salários até R$ 280,00 Aumento de 20%
#Maior que R$ 280,00 até R$ 700,00 Aumento de 15%
#Maior que R$ 700,00 até R$ 1500,00 Aumento de 10%
#Maior que R$ 1500,00 Aumento de 5%

# -*- coding: utf-8 -*-

salario = float (input ('Digite o valor do salário: '))

if (salario <= 280):
    aumento20 = salario * 0.20
    print ('Valor do aumento: %.2f' % aumento20)
    salario20 = salario + aumento20
    print ('Novo salário: %.2f' % salario20)

elif (280 < salario <= 700):
    aumento15 = salario * 0.15
    print ('Valor do aumento: %.2f' % aumento15)
    salario15 = salario + aumento15
    print ('Novo salário: %.2f' % salario15)

elif (700 < salario <= 1500):
    aumento10 = salario * 0.10
    print ('Valor do aumento: %.2f' % aumento10)
    salario10 = salario + aumento10
    print ('Novo salário: %.2f' % salario10)

elif (salario > 1500):
    aumento5 = salario * 0.05
    print ('Valor do aumento: %.2f' % aumento5)
    salario5 = salario + aumento5
    print ('Novo salário: %.2f' % salario5)

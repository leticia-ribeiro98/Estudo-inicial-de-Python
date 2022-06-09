#Elabore um programa que leia um valor em reais e um valor representando a atual cotação do dólar. Em seguida, imprima o valor em dólares.

# -*- coding: utf-8 -*-

reais = float (input ('Digite o valor em reais: '))
dolar = float (input ('Digite a cotação do dólar: '))
converter = reais / dolar

print ('Valor em dólar: %.2f' % converter)

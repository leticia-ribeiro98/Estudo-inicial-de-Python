#Um funcionário chamado Carlos tem um colega chamado João que recebe um salário que equivale a 1/3
#do seu salário. Carlos gosta de fazer aplicações na poupança e vai aplicar seu salário integralmente
#nela uma única vez. João aplicará seu salário integralmente no fundo de renda fixa uma única vez. Escreva um programa que lê o valor do salário do Carlos, a taxa de rendimento da poupança e do fundo
#de renda fixa por mês e calcula quantos meses serão necessários para que o valor pertencente a João
#iguale ou ultrapasse o valor pertencente a Carlos.

# -*- coding: utf-8 -*-

sal_carlos = float (input ('Digite o salário do Carlos: '))
poupanca = float (input ('Digite o rendimento da poupança(%): '))
renda_fixa = float (input ('Digite o rendimento do fundo de renda fixa(%): '))

sal_joao = sal_carlos * (1/3)
poupanca = poupanca/100
renda_fixa = renda_fixa/100
n = 0

while sal_carlos >= sal_joao:
    n = n + 1
    sal_carlos = sal_carlos * (1 + poupanca)
    sal_joao = sal_joao * (1 + renda_fixa)
print ('Meses: %.d' % n)

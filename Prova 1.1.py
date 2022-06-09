#Escreva um programa que solicita ao usuário um montante inicial de investimento (vp), uma taxa de juros anual (i) e o número de anos (n) que durará esse investimento. O programa deverá imprimir na tela o valor futuro (v f ) do investimento
#Considere a seguinte fórmula:
 v f = vp ×(1+(i ×0.01))n


# -*- coding: utf-8 -*-

vp = float (input ('Digite o valor do investimento inicial: '))
i = float (input ('Digite a taxa de juros anual: '))
n = float (input ('Digite o período do investimento em anos: '))

vf = vp * (1 + (i*0.01))**n

print ('Valor futuro: %.2f' % vf)

#Uma empresa contrata um encanador pagando R$ 30,00 por dia. Faça um programa que leia o número de dias trabalhados pelo encanador e imprima o valor líquido do pagamento que ele deve receber, sabendo que são descontados 8% para imposto de renda.

# -*- coding: utf-8 -*-

dias_trabalhados = int (input ('Digite a quantidade de dias trabalhados: '))
valor_recebido = (dias_trabalhados * 30) * 0.92

print ('Valor recebido: %.2f' % valor_recebido)

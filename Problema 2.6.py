#O custo total ao consumidor de um carro novo é a soma do custo de fábrica, da comissão do distribuidor, e dos impostos. A comissão e os impostos são calculados sobre o custo de fábrica, de acordo com
#a tabela abaixo. Faça um programa que leia o custo de fábrica de um carro novo e imprima na tela o
#custo total ao consumidor.
#Custo de fábrica % do distribuidor % dos impostos
#até R$12.000,00 5% isento
#acima de R$12.000,00 até R$25.000,00 10% 15%
#acima de R$25.000,00 15% 20%

# -*- coding: utf-8 -*-

custo_fabrica = float (input ('Digite o custo de fábrica: '))

if (custo_fabrica <= 12000):
    distribuidor = 0.05 * custo_fabrica
    impostos = 0.00 * custo_fabrica
    custo_total = custo_fabrica + distribuidor + impostos
    print ('Custo total: %.2f' % custo_total)

elif (12000 < custo_fabrica <= 25000):
    distribuidor = 0.10 * custo_fabrica
    impostos = 0.15 * custo_fabrica
    custo_total = custo_fabrica + distribuidor + impostos
    print ('Custo total: %.2f' % custo_total)

elif (custo_fabrica > 25000):
    distribuidor = 0.15 * custo_fabrica
    impostos = 0.20 * custo_fabrica
    custo_total = custo_fabrica + distribuidor + impostos
    print ('Custo total: %.2f' % custo_total)

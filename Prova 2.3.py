#Escreva um programa que peça ao usuário o valor da sua hora de trabalho, a quantidade de horas
#trabalhadas no mês e calcula a sua folha de pagamento. São descontados do salário o Imposto de
#Renda, que depende do salário bruto (conforme tabela abaixo), e o INSS, que corresponde a 10%
#do salário bruto. O FGTS corresponde a 11% do salário bruto, no entanto o FGTS não é descontado
#do salário, pois é a empresa que deposita. O salário líquido corresponde ao salário bruto menos os
#descontos.
#Salário Bruto Imposto de Renda
#Até R$900 Isento
#Maior que R$900 até R$1500 Desconto de 5%
#Maior que R$1500 até R$2500 Desconto de 10%
#Maior que R$2500 Desconto de 20%

# -*- coding: utf-8 -*-

preco = float(input('Digite o valor da hora de trabalho: '))
horas = int(input('Digite a quantidade de horas trabalhadas no mês: '))
s_bruto = preco * horas
ir = 0.0
if s_bruto > 2500:
    ir = s_bruto * 0.2
elif s_bruto > 1500:
    ir = s_bruto * 0.1
elif s_bruto > 900:
    ir = s_bruto * 0.05
    
fgts = s_bruto * 0.11
inss = s_bruto * 0.1
descontos = ir + inss
s_liq = s_bruto - descontos
print ('Salário Bruto: R$ %.2f' % s_bruto)
print ('IR: R$ %.2f' % ir)
print ('INSS: R$ %.2f' % inss)
print ('FGTS: R$ %.2f' % fgts)
print ('Total de descontos: R$ %.2f' % descontos)
print ('Salário líquido: R$ %.2f' % s_liq)

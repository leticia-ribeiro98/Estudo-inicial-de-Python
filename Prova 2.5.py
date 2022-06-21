#Uma empresa vende o mesmo produto para quatro estados diferentes. Cada estado possui uma taxa
#de imposto sobre o produto, como indicado na tabela abaixo. Faça um programa em que o usuário
#entre com o valor e a sigla do estado destino do produto e o programa retorne o preço final do produto acrescido do imposto do estado em que ele será vendido. Caso o estado inserido não seja um
#dos estados válidos, imprima a mensagem "Estado inválido".
#Estado Taxa de imposto
#MG 7%
#SP 12%
#RJ 15%
#MS 8%

# -*- coding: utf-8 -*-

valor = float (input ('Digite o valor do produto: '))
estado = input ('Digite o estado: ')

if estado == 'MG':
    valor_final = valor * (1 + 0.07)
    print ('Valor final: %.2f' % valor_final)
elif estado == 'SP':
    valor_final = valor * (1 + 0.12)
    print ('Valor final: %.2f' % valor_final)
elif estado == 'RJ':
    valor_final = valor * (1 + 0.15)
    print ('Valor final: %.2f' % valor_final)
elif estado == 'MS':
    valor_final = valor * (1 + 0.08)
    print ('Valor final: %.2f' % valor_final)
else:
    print ('Estado inválido')

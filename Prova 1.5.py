#Escreva um programa para ajudar vendedores de uma loja de roupas. O seu programa deverá ler o valor de uma compra e a partir dele exibir na tela as seguintes informações:
#O preço com 10% de desconto, para pagamentos à vista;
#O valor de cada parcela caso o preço seja parcelado em 6x (sem juros);
#A comissão do vendedor, caso o pagamento seja à vista (5% sobre valor com o desconto de 10%);
#A comissão do vendedor, caso o pagamento seja parcelado (5% sobre o valor integral).
#Esses quatro valores devem ser exibidos nessa ordem, um por linha. O seu programa não deve imprimir mais nada além disso.


# -*- coding: utf-8 -*-

valor_compra = float (input ('Digite o valor da compra: '))

# O preço com 10% de desconto, para pagamentos à vista
pagamento_vista = valor_compra * 0.90

# O valor de cada parcela caso o preço seja parcelado em 6x (sem juros)
parcelas = valor_compra / 6

# A comissão do vendedor, caso o pagamento seja à vista (5% sobre valor com o desconto de 10%)
comissao_vista = pagamento_vista * 0.05

# A comissão do vendedor, caso o pagamento seja parcelado (5% sobre o valor integral)
comissao_parcelado = valor_compra * 0.05

print ('Valor com desconto: %.2f' % pagamento_vista)
print ('Valor da parcela: %.2f' %  parcelas)
print ('Comissão do vendedor (à vista): %.2f' %  comissao_vista)
print ('Comissão do vendedor (parcelado): %.2f' %  comissao_parcelado)

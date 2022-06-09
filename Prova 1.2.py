#Pedro, João e Marcela jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor que cada um deu para a realização da aposta. Escreva um programa que solicita ao usuário quanto cada apostador investiu e o valor do prêmio, e então o programa deve imprimir na tela quanto cada um ganharia do prêmio com base no valor investido.


# -*- coding: utf-8 -*-

aposta_pedro = float (input ('Digite o valor que o Pedro apostou: '))
aposta_joao = float (input ('Digite o valor que o João apostou: '))
aposta_marcela = float (input ('Digite o valor que a Marcela apostou: '))
premio = float (input ('Digite o valor do prêmio: '))

# Somar todas as apostas e encontrar a porcentagem da parcela que cada pessoa apostou

soma = aposta_pedro + aposta_joao + aposta_marcela

# Prêmio Pedro
premio_pedro = (aposta_pedro / soma) * premio

# Prêmio João
premio_joao = (aposta_joao / soma) * premio

# Prêmio Marcela
premio_marcela = (aposta_marcela / soma) * premio

print ('Prêmio do Pedro: %.2f' % premio_pedro)
print ('Prêmio do João: %.2f' % premio_joao)
print ('Prêmio da Marcela: %.2f' % premio_marcela)

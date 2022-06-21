#Um motorista que ultrapassa a velocidade máxima permitida estará sujeito a uma infração média,
#grave ou gravíssima. Faça um programa que receba dois valores: a velocidade máxima de uma via e
#a velocidade registrada por um radar. Em seguida, o programa deve imprimir na tela se o motorista
#cometeu algum tipo de infração. Considere que as multas são definidas conforme a tabela abaixo:
#Excesso de velocidade sobre a máxima permitida Natureza da infração
#Menor ou igual a velocidade máxima Sem Infração
#Até 20% Infração Média
#Acima de 20% até 50% Infração Grave
#Acima de 50% Infração Gravíssima

# -*- coding: utf-8 -*-

vm = float (input ('Digite o valor da velocidade máxima: '))
vr = float (input ('Digite o valor da velocidade registrada: '))

if (vr <= vm):
    print ('Sem Infração')
elif (vm < vr <= vm * 1.20):
    print ('Infração Média')
elif (vm * 1.20 < vr <= vm * 1.50):
    print ('Infração Grave')
elif (vr > 1.50):
    print ('Infração Gravíssima')

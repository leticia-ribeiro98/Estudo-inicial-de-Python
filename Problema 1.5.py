#Faça um programa que leia os valores de comprimento, largura e altura de uma caixa, e imprime na tela o seu volume. Note que todos esses valores são números de ponto flutuante.

# -*- coding: utf-8 -*-

c = float (input('Digite o comprimento: '))
l = float (input('Digite a largura: '))
h = float (input('Digite a altura: '))
volume = c * l * h
print  ('Volume: %.1f' % volume)

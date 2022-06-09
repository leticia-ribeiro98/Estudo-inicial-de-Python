#Escreva um programa que leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida para m/s (metros por segundo)

# -*- coding: utf-8 -*-

vel = float (input('Digite a velocidade em km/h: '))
vel_convertida = vel / 3.6
print ('Velocidade em m/s: %.1f' % vel_convertida)

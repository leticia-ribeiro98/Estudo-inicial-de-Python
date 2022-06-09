#Faça um programa que leia uma distância em milhas e apresente-a em quilômetros.
    
# -*- coding: utf-8 -*-

dist_m = float (input ('Digite a distância em milhas: '))
convert_km = dist_m * 1.61
print ('Distância em km: %.2f' % convert_km)

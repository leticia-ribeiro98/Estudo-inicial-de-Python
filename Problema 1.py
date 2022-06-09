# -*- coding: utf-8 -*-

raio = float (input ('Digite o valor do raio da circunferência '))
pi = float (3.1415)

#calcular perímetro
perimetro = 2 * pi * raio
print ('Perímetro: %.2f' % perimetro)

#calcular área
area = pi * ((raio)**2)
print ('Área: %.2f' % area)

#calcular volume
vol = 4 * pi * ((raio**3)/3)
print ('Volume: %.2f' % vol)
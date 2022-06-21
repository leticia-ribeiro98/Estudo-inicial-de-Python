#Faça um programa que leia cinco números inteiros e identifique:
#• O maior valor informado
#• O menor valor informado
#• Quantos números são divisíveis por 3

# -*- coding: utf-8 -*-

n1 = int (input ('Digite o primeiro inteiro: '))
n2 = int (input ('Digite o segundo inteiro: '))
n3 = int (input ('Digite o terceiro inteiro: '))
n4 = int (input ('Digite o quarto inteiro: '))
n5 = int (input ('Digite o quinto inteiro: '))

d1 = 0
d2 = 0
d3 = 0
d4 = 0
d5 = 0

#Número maior

if (n1 >= n2 and n1 >= n3 and n1 >= n4 and n1 >= n5):
    print ('Maior: %d' % n1)
if (n2 > n1 and n2 >= n3 and n2 >= n4 and n2 >= n5):
    print ('Maior: %d' % n2)
if (n3 > n1 and n3 > n2 and n3 >= n4 and n3 >= n5):
    print ('Maior: %d' % n3)
if (n4 > n1 and n4 > n2 and n4 > n3 and n4 >= n5):
    print ('Maior: %d' % n4)
if (n5 > n1 and n5 > n2 and n5 > n3 and n5 > n4):
    print ('Maior: %d' % n5)
    
#Número menor

if (n1 <= n2 and n1 <= n3 and n1 <= n4 and n1 <= n5):
    print ('Menor: %d' % n1)
if (n2 < n1 and n2 <= n3 and n2 <= n4 and n2 <= n5):
    print ('Menor: %d' % n2)
if (n3 < n1 and n3 < n2 and n3 <= n4 and n3 <= n5):
    print ('Menor: %d' % n3)
if (n4 < n1 and n4 < n2 and n4 < n3 and n4 <= n5):
    print ('Menor: %d' % n4)
if (n5 < n1 and n5 < n2 and n5 < n3 and n5 < n4):
    print ('Menor: %d' % n5)

#Divisivel por 3
    
if (n1 % 3 == 0):
    d1 = 1
if (n2 % 3 == 0):
    d2 = 1
if (n3 % 3 == 0):
    d3 = 1
if (n4 % 3 == 0):
    d4 = 1
if (n5 % 3 == 0):
    d5 = 1

soma = d1 + d2 + d3 + d4 + d5
print ('Quantidade de divisíveis por 3: %d' % soma)

#Escreva um programa que calcule as raízes da equação de segundo grau, dado os valores de a, b e c:

#A variável a tem que ser diferente de zero. Caso seja igual a zero, imprima a mensagem "Não é uma equação quadrática".
#• Se ∆ < 0 , não existe raiz real. Imprima a mensagem "Não existe raiz real".
#• Se ∆ = 0 , existe uma raiz real. Imprima a mensagem "Raiz única"e o valor da raiz.
#• Se ∆ ≥ 0, imprima as duas raízes

# -*- coding: utf-8 -*-

a = int(input('Digite o valor de a:'))
b = int(input('Digite o valor de b:'))
c = int(input('Digite o valor de c:'))


if(a == 0):
    print('Não é uma equação quadrática')
else:  
    delta = (b ** 2) - (4 * a * c)

    if delta < 0:
        print('Não existe raiz real')
    elif delta == 0:
        print('Raiz única')
        x = -b / (2 * a)
        print('Raiz: %.2f '%x)
    else:
        x1 = (-b + (delta ** 0.5)) / (2 * a)
        x2 = (-b - (delta ** 0.5))  / (2 * a)

        print('Raiz 1: %.2f'%x1)
        print('Raiz 2: %.2f'%x2)

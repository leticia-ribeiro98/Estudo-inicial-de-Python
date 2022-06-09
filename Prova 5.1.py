#Certo dia, o Prof. Humberto José Roberto fez o seguinte questionamento: se o zero à esquerda de um número não tem valor algum, 
#por que teria em outras posições de um número? Portanto, ele pede sua ajuda para, ao somar dois valores inteiros, que o 
#resultado seja exibido segundo o raciocínio dele, ou seja, sem os zeros. Por exemplo, ao somar 15 + 5, o resultado correto 
#seria 20, mas com esta nova ideia, o novo resultado seria 2. Ao somar 99 + 6, o resultado correto seria 105, mas com esta nova ideia, 
#o novo resultado seria 15. Escreva um programa que lê dois números inteiros (pode assumir que eles não têm o algarismo zero),
#some os mesmos e, caso o resultado tenha algum algarismo zero, então os retire antes de imprimir na tela

# -*- coding: utf-8 -*-

num1 = int (input ('Digite o primeiro número: '))
num2 = int (input ('Digite o segundo número: '))

soma = str (num1 + num2)
posicao = len (soma)
resultado = ''

for c in range (0,posicao):
    numero = soma [c]
    
    if numero == '0':
        resultado = resultado
    
    else:
        resultado = resultado + numero

print ('Resultado: %s' % resultado)

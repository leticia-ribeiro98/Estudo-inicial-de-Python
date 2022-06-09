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

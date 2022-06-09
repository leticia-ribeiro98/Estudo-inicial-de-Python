#Uma cifra de César é uma forma fraca de criptografia que implica em "rotacionar"cada letra por um
#número fixo de posições. Rotacionar uma letra significa deslocá-la pelo alfabeto, voltando ao início
#se for necessário. Portanto, ‘A’ rotacionado por 3 é ‘D’, enquanto que ‘Z’ rotacionado por 1 é ‘A’. Para
#rotacionar uma palavra, faça cada letra se mover pela mesma quantidade de posições. Por exemplo,
#a palavra "cheer"rotacionada por 7 é a palavra "jolly". Você pode usar a função pré-definida ord, que
#converte um caractere em um código numérico e a função pré-definida chr, que converte códigos
#numéricos em caracteres.

# -*- coding: utf-8 -*-

palavra = input ('Digite uma palavra: ')
chave = int (input ('Digite o valor da chave: '))
tamanho = len (palavra)
resultado = ''
resto = chave % 26

for c in range (0,tamanho):
    
    letra = palavra [c]
    posicao = ord (letra)
    pular_posicao = posicao + resto
    
    
    if (pular_posicao > 122):
        pular_posicao = 96 + (pular_posicao - 122)
        transformar_letra = chr (pular_posicao)
        resultado += transformar_letra   
        
    
    else:
        transformar_letra = chr (pular_posicao)
        resultado += transformar_letra

print ('Resultado: %s' % resultado)

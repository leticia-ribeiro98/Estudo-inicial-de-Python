#A sua impressora foi infectada por um vírus e está imprimindo de forma incorreta. Depois de olhar
#para várias páginas impressas por um tempo, você percebe que ela está imprimindo cada linha de
#dentro para fora. Em outras palavras, a metade esquerda de cada linha está sendo impressa a partir
#do meio da página até a margem esquerda. Do mesmo modo, a metade direita de cada linha está
#sendo impressa a partir da margem direita e prosseguindo em direção ao centro da página.
#Por exemplo a linha: "THIS LINE IS GIBBERISH"
#Está sendo impressa como: "I ENIL SIHTHSIREBBIG S"
#Da mesma foma, a linha "MANGOS " está sendo impressa incorretamente como "NAM SOG". Sua
#tarefa é desembaralhar (decifrar) a string a partir da forma como ela foi impressa para a sua forma
#original. Assim, escreva um programa que lê uma frase embaralhada e imprime na tela a frase correta.


frase = input('Frase embaralhada:')
tamanho = len(frase)
metade = int(tamanho/2)

resultado = ''

resultado = frase[metade-1::-1]

resultado += frase[:metade-1:-1]
        
print ('Frase correta:', resultado)

#Escreva um programa que solicita ao usuário um número inteiro e então o programa imprime na tela a soma do sucessor de seu triplo com o antecessor de seu dobro

num = int (input ('Digite um número: '))

# Sucessor do seu triplo

triplo = num * 3
sucessor = triplo + 1

#Antecessor do seu dobro
dobro = num * 2
antecessor = dobro - 1

soma = sucessor + antecessor

print ('Resultado: %d' % soma)

#Escreva uma função chamada soma_divisores que recebe como parâmetro um número inteiro e
#retorna a soma de todos os divisores desse número, com exceção dele próprio.

# -*- coding: utf-8 -*-

def soma_divisores (num):
    contador = 1
    soma = 0
    
    for divisores in range (contador, num):
        if (num % divisores == 0):
            soma = soma + divisores
    return soma

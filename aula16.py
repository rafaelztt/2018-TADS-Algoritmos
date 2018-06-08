# dia = 7
# nome = "Rafael"
#
# print("Olá",nome,", hoje é dia",dia)
#
# print( "Olá {}, hoje é dia {}".format(nome, dia) )

vetor = [""]*5
i = 0
while i < len(vetor):
    vetor[i] = input("Produto {}: ".format(i+1) )
    i = i + 1

# Exercício 1: Crie um vetor e armazene os números de 1 a 100. Cada número deve ocupar uma posição do vetor (lista).
lista = [""]*100
p = 0
while p < len(lista):
    lista[p] = p + 1
    p = p + 1

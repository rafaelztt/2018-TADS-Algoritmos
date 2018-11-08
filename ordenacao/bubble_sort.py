import time

def bubble_sort(vetor):
    # https://www.youtube.com/watch?v=nmhjrI-aW5o

    print("Vetor inicial: \t{}".format(vetor))
    # tempo_inicial = time.time()

    ordenado = False

    while ordenado != True:
        ordenado = True
        j = 0
        while j < len(vetor)-1:
            if vetor[j] > vetor[j+1]:
                temp = vetor[j]
                vetor[j] = vetor[j+1]
                vetor[j+1] = temp

                ordenado = False
            j += 1

        print(vetor)

    # tempo_final = time.time() - tempo_inicial
    print("Vetor final: \t{}".format(vetor))
    # print("Tempo de processamento: {}".format(tempo_final))

    return vetor

''' ------------------------------------- '''

def bubble_sort_aula(vetor):

    print(vetor)

    ordenado = False
    while ordenado != True:

        ordenado = True
        j = 0
        while j < len(vetor)-1:
            if vetor[j] > vetor[j+1]:
                temp = vetor[j]
                vetor[j] = vetor[j+1]
                vetor[j+1] = temp

                ordenado = False
            j += 1

        print(vetor)

    print(vetor)

import time

def selection_sort(vetor):
    # https://www.youtube.com/watch?v=xWBP4lzkoyM

    print("Vetor inicial: \t{}".format(vetor))
    # tempo_inicial = time.time()

    i = 0
    while i < len(vetor) - 1:

        # print("Iteração responsável por achar o número para a posição ",i)
        menor = i
        j = i + 1

        while j < len(vetor):
            if vetor[j] < vetor[menor]:
                menor = j
            j+=1

        if menor != i:
            # print("Troca dos elementos da posição %d com a posição %d" % (i,menor))
            temp = vetor[i]
            vetor[i] = vetor[menor]
            vetor[menor] = temp

        i+=1

        # Mostra o vetor depois de consultar o melhor valor pra posição i
        print(vetor)

    # tempo_final = time.time() - tempo_inicial

    print("Vetor final: \t{}".format(vetor))
    # print("Tempo de processamento: {}".format(tempo_final))

    return vetor


''' -------------------------------------------- '''

def selection_sort_aula(vetor):

    print(vetor)

    i = 0
    while i < len(vetor) - 1:

        menor = i
        j = i + 1

        while j < len(vetor):
            if vetor[j] < vetor[menor]:
                menor = j
            j+=1

        if menor != i:
            temp = vetor[i]
            vetor[i] = vetor[menor]
            vetor[menor] = temp

        i+=1
        print(vetor)

    print(vetor)

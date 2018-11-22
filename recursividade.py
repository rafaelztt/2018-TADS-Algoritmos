def somaRec(vet,i):
    if i >= len(vet): # condição de parada
        return 0 # finaliza a chamada e volta

    else: # Faz uma nova chamada da função
        total = vet[i] + somaRec(vet,i+1)

    # Quando termina a chamada da função
    return total

################################
v = [1,2,3,4,5]
print(somaRecursiva(v,0))

from random import randint
# Criação do vetor para armazenar números
loteria = [""]*6
# Variável de controle do laço de repetição
i = 0
# Laço para preencher o vetor
while i < len(loteria):
    # Gera número
    num = randint(1,60)
    # Variável para saber se repetiu ou não
    repetiu = "n"

    # Variável de controle do laço que verifica se o número já existe ou não
    k = 0
    # Laço para verificação do número
    while k < i:
        # Verifica se o núm está na posição k
        if num == loteria[k]:
            # Se for verdadeiro, o número já está lá
            # Diminui o valor do "i" para fazer este processo novamente
            i -= 1
            # Muda o valor da variável repetiu
            repetiu = "s"
            # Parar o laço de repetição
            break

        # Incremento da posição
        k += 1
        # Fim do while do k

    if repetiu == "n":
        # Armazena
        loteria[i] = num

    # Incremento da posição
    i += 1

# Mostrar a lista gerada
print(loteria)

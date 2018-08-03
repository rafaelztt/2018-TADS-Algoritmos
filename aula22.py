# Função com parâmetro
# e sem retorno
# print("Funções!")

# O input() e o int() tem
# parâmetro e tem retorno
# num = input("Número:")
# num = int(num)

# a função float() também
# tem retorno e parâmetro
# a = float( input("Número:") )

# A criação de funções é feita com a palavra "def"
# E, geralmente, é feita no início do programa
# def nome():
#     conteúdo/corpo da função
#     bla bla bla
# Aqui limita o fim da função

# Exemplo de função sem retorno e sem parâmetro
def exemplo1():
    print("Olá mundo!")
    print("Não tenho parâmetro")
    print("Não tenho retorno")

    n = input("Seu nome: ")

    if(n != ""):
        print("Olá {}, bem vindo ao programa X.".format(n) )
    else:
        print("Acesso negado!")


# Função sem retorno e sem parâmetro para calcular a tabuada
def calc_tabuada():
    n = int(input("Número: "))

    print("Calculando tabuada...")

    a = 1
    while a <= 10:
        print(a,"*",n,'=',a*n)
        a+=1

# Exemplo de função com parâmetro e sem retorno
def exemplo2(num):

    print("O número informado é:", num)

    if num % 2 == 0 :
        print("Este número é par!")
    else:
        print("Número ímpar detectado!")

# Exemplo de função com parâmetro e sem retorno
# Funções podem ter o mesmo nome, porém com quantidade
# diferente de parâmetros
def calc_tabuada(n):

    #o range pode ter o valor inicial e final da contagem
    for x in range(1, 11):
        print(n,"*",x,'=',x*n)


# Exemplo de função com parâmetro e com retorno
def exemplo3(a):

    triplo = a * 3

    # Retorna o valor da variável abaixo
    return triplo

def exemplo4(num):

    if num % 2 == 0:
        # Pode colocar uma operação no return
        # pois ela será resolvida antes de enviar o resultado
        return num**2
    else :
        n = num ** 3
        # Podemos também devolver o valor de uma variável
        return n

##### Fim das funções ####
# Chama a função para ser executada
# exemplo1()

# Chamada de função
# calc_tabuada()

# Chamada de função
# a = 10
# exemplo2(a)

# b = int( input("Informe um número:") )
# exemplo2(b)

# Chamda de função com parâmetros
# calc_tabuada(8)

# b = int( input("Informe um número:") )
# calc_tabuada(b)

# Chamada de função com retorno
k = exemplo4(852)
print("Resposta:", k)

# O retorno de uma função pode ser utilizado na chamada de outra função
calc_tabuada(k)

# Funções com retorno podem ser usadas direto no print
print("Resposta direta:", exemplo4(750))

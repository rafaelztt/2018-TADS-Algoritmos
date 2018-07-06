# É obrigatório ter parênteses junto com o nome da função
# e não deve ter espaço entre o nome e os parênteses
# Para criar uma função basta seguir o exemplo abaixo:
# def nomeDaFuncao():
#   Código da função com tab
#
def mostrarErro1():
    # Código da função
    print("""
_____
|    |
|    O
|
|    """)

# Aqui a tabulação já finaliza a função anterior
def mostrarErro2():
    print("""
_____
|    |
|    O
|   /
|    """)


########## Início do programa ############

erro=2
"""
...
Seu código
...
"""

if erro == 1:
    # Coloque o nomeDaFuncao() e ela será executada aqui
    mostrarErro1() # parênteses são obrigatórios com o nome das funções
    # continuação
    # ...
elif erro == 2:
    mostrarErro2()
    # continuação
    # ...

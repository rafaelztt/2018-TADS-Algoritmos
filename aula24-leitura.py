"""
Modos de leitura de arquivos:
- "r" é de leitura
- "w" é de escrita
- "a" é de escrita, mas começa um arquivo em branco e apaga se já existir
"""
fileh = open("arquivos/nomes.txt","r")

conteudo = fileh.readlines()

fileh.close()

# Agora que vocês sabem que a variável "conteúdo" é um vetor,
# faça um laço de repetição para mostrar na tela os nomes do arquivo
l = 0
while l < len(conteudo) :
    print( conteudo[l] )
    l+=1

# A mesma coisa com for
for linha in conteudo:
    print(linha)

for l in range( len(conteudo) ):
    print( conteudo[l] )

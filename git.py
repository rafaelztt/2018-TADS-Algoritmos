import os

msg_commit = input("Mensagem do commit: ")

while len(msg_commit) < 5:
    print("A mensagem deve ter pelo menos 5 caracteres.")
    msg_commit = input("Mensagem do commit: ")

email_padrao = "rafael.zottesso@ifpr.edu.br"
email = input("Digite enter para manter o {} como padrão ou informe seu e-mail: ".format(email_padrao))

if email == "":
    email = email_padrao

print("Adicionando os novos arquivos...\n")
os.system("git add *")

print("Configurando o email do usuário...\n")
os.system('git config user.email "'+email+'"')

print("Efetuando o commit das modificações...\n")
os.system('git commit -m "'+msg_commit+'"')

print("Conectando com os servidores do Github...\n")
os.system('git push origin master')

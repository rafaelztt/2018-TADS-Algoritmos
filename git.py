import os

msg_commit = input("Mensagem do commit: ")
email = input("Digite enter para manter o rafael.zottesso@ifpr.edu.br como padrão ou informe seu e-mail: ")

if email == "":
    email = "rafael.zottesso@ifpr.edu.br"

os.system("git add *")

os.system('git config user.email "'+email+'"')

os.system('git commit -m "'+msg_commit+'"')

os.system('git push origin master')

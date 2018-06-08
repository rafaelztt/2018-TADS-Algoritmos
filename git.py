import os

msg_commit = "Adição dos comandos git."

os.system("git add *")

os.system('git config user.email "rafael.zottesso@ifpr.edu.br"')

os.system('git commit -m "'+msg_commit+'"')

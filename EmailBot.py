import yagmail
import os
from datetime import datetime

from dotenv import load_dotenv
load_dotenv('.env.local')

contatos = [('CaIETAXX', 'caio.macedo@alura.com.br', '14/04')]

user = os.getenv('EMAIL_USER')
password = os.getenv('EMAIL_PASSWORD')

dataAtual = datetime.now().strftime('%d/%m')

emailServer = yagmail.SMTP(user=user, password=password)

for nome in contatos:
    if nome[2] == dataAtual:
        emailServer.send(to=nome[1], subject = 'Happy Birthday', contents = 'Olá, ' + nome[0]+ '! Estou enviando essa mensagem pelo script que desenvolvi, enfim, Feliz Aniversário!')

emailServer.close()

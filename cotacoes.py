import requests
import json
from twilio.rest import Client
from datetime import datetime

cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
cotacoes_dic = cotacoes.json()
text_msg = 'Cotação atualizada: {}\nDólar Americano - R${:.2f}\nEuro - R${:.2f}\nBitcoin - R${:.2f}'.format(datetime.now(),float(cotacoes_dic['USDBRL']['bid']),float(cotacoes_dic['EURBRL']['bid']),float(cotacoes_dic['BTCBRL']['bid']))

# o token e a senha estão criptografados devido a segurança

account_sid = '*******************************' 
auth_token = '********************************'
client = Client(account_sid, auth_token)

# os numeros de telefone dos destinatarios tambem estão criptografados

number = '+12762925791'
destino = '+************'
destino2 = '+************'

message = client.messages.create(
  body=text_msg,
  from_=number,
  to=destino
)

message2 = client.messages.create(
  body=text_msg,
  from_=number,
  to=destino2
)

print(message.sid)
print(message2.sid)

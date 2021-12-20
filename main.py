import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC1c3fb798a16a7db3fe3b197b121a5e83"
# Your Auth Token from twilio.com/console
auth_token  = "3447df6b48984a4bc52c01fcb36f8f03"
client = Client(account_sid, auth_token)

# Abrir os 6 arquivos em excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} Alguém Bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+Número do seu telefone",
            from_="+Seu Número Gerado no Twilio",
            body=f'No mês {mes} Alguém Bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)








# Para cada arquivo :

# Verificar se algum valor na coluna vendas daquele arquivo é maior que 55.000

# se for maior que 55.000 -> Enviar SMS com o nome, mês  e as vendas do vendedor

# caso não seja maior que 55.000 não quero fazer nada

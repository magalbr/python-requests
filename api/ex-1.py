import requests

#criar um programa que peça que o usuário
print('Digite o CEP')
VIACEP_URL = input("http://viacep.com.br/ws/{}/json")
response = requests.get(VIACEP_URL)
END_USER = response.json()
print(END_USER)

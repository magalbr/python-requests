import requests

#dados = {"nome":"{}",
#       "sobrenome":"Magalhaes"
#}
API_URL = "https://gen-net.herokuapp.com/api/users/"
response = requests.post{API_URL, json={
    'name': input('Digite seu nome: '),
    'email': input('Digite seu email: '),
    'password': input('Digite sua senha: ')

})    
#request = requests.post("https://gen-net.herokuapp.com/api/users/",
#        json=data) 
if response.status_code == 200:
    user_id = response.json()['id']
    print(user_id)
else:
    print('Erro ao cadastrar')


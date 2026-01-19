import requests

cep = input("Informe seu CEP >>> ")
dados = requests.get(f"https://viacep.com.br/ws/{cep}/json/").json()
print("Rua:", dados["logradouro"])
# https://pokeapi.co/api/v2/pokemon/charizard

#200: Ok
#404: error de permisos
#500: Error con el servidor
import requests

"""https://pokeapi.co/"""
res = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")

print(res.status_code)
print(res.headers)
json = res.json()

print(json)
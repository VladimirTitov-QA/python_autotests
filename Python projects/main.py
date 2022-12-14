import requests
import json

token = '30f64d5f954683abefc597f8c56207a6'
response = requests.post('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
    "name": "Пикачу",
    "photo": "https://avatanplus.com/files/resources/original/579fe9871201c15648a837a2.png"
})

print(response.text)

response_put = requests.put('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
   "pokemon_id": 1720,
    "name": "Бульбазавр",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
})

print(response_put.text)

response_post = requests.post('https://pokemonbattle.me:5000/trainers/addPokebol', headers={'trainer_token' : token}, json={
   "pokemon_id": "1720"
})

print(response_post.text)
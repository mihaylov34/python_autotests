import requests
import json
token = '6e2a7898bc954204a4959de405465f55'
response = requests.post(' https://pokemonbattle.me:5000/trainers/reg', json = {
    "trainer_token": token,
    "email": 'mihaylov96@mail.ru',
    "password": "Iloveqa34"
},headers={'Content-Type':'application/json'})
print(response.text)


response_confirm = requests.post(' https://pokemonbattle.me:5000/trainers/confirm_email',json ={
    "trainer_token": token
}, headers={'Content-Type':'application/json'})
print(response_confirm.text)


new_pokemons=requests.post(' https://pokemonbattle.me:5000/pokemons',
headers={'Content-Type':'application/json','trainer_token': token},json={
    "name": "Бульба",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
})
print(new_pokemons.text)

name_pokemons=requests.put(' https://pokemonbattle.me:5000/pokemons',
headers={'Content-Type':'application/json','trainer_token': token},
json={
    "pokemon_id": 3316,
    "name": "Gavriil",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"})
print(name_pokemons.text)


pokeball=requests.post(' https://pokemonbattle.me:5000/trainers/add_pokeball',
headers={'Content-Type':'application/json','trainer_token': token},
json={
    "pokemon_id":'3316'
})
print(pokeball.text)
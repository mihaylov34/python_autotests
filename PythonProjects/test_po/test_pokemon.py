import requests
import pytest



def test_status_code():
    response=requests.get('https://pokemonbattle.me:5000/trainers')
    assert response.status_code==200





def test_fragment_of_response():
        responses=requests.get('https://pokemonbattle.me:5000/trainers' , params = {'trainer_id':1975})
        assert responses.json()['trainer_name']=='mv'


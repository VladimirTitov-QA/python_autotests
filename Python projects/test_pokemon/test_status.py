import requests
import pytest

def test_status_code():
    response = requests.get('https://pokemonbattle.me:5000/trainers')
    assert response.status_code == 200

def test_piece_of_body():
    response = requests.get('https://pokemonbattle.me:5000/trainers', params = {'trainer_id' : '1390'})
    assert response.json()['trainer_name'] == 'Кеноби'

@pytest.mark.parametrize('key, value', [('trainer_name', 'Кеноби'),('city', 'Москва')])

def test_parametrs_body(key, value):
    response = requests.get('https://pokemonbattle.me:5000/trainers', params = {'trainer_id' : '1390'})
    assert response.json()[key] == value
from django.test import TestCase
import requests
from rest_framework import status


class User(TestCase):
    def setUp(self):
        params = {
            "email": "teste-api@teste.com",
            "password": "senha2020",
            "password_confirm": "senha2020",
        }
        requests.post("https://appconafer.herokuapp.com/accounts/register/", data=params)

        credential = {'username': 'teste-api@teste.com',
                      'password': 'senha2020'}

        result = requests.post("https://appconafer.herokuapp.com/api-login/", data=credential)
        self.token = result.json().get('token')

    def test_api_get_token(self):

        credential = {'username': 'teste-api@teste.com',
                      'password': 'senha2020'}

        result = requests.post("https://appconafer.herokuapp.com/api-login/", data=credential)
        self.assertEqual(result.status_code, status.HTTP_200_OK)

    def test_api_listar_sem_autenticacao(self):
        result = requests.get("https://appconafer.herokuapp.com/blog/api/")
        self.assertEqual(result.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_api_listar_com_autenticacao(self):

        headers = {"Authorization": f"token {self.token}"}

        result = requests.get("https://appconafer.herokuapp.com/blog/api/", headers=headers)
        self.assertEqual(result.status_code, status.HTTP_200_OK)

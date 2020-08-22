from django.test import TestCase
import requests
from rest_framework import status


class Blog(TestCase):
    def setUp(self):
        credential = {'username': 'teste-api@teste.com',
                      'password': 'senha2020'}

        result = requests.post("https://appconafer.herokuapp.com/api-login/", data=credential)
        self.token = result.json().get('token')

    def test_api_add_postagem_com_token(self):

        params = {
            "title": "What is Lorem Ipsum?",
            "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
            "image_url": "https://lipsum.com/images/banners/black_120x90.gif",
            "user": 1,
        }

        headers = {"Authorization": f"token {self.token}"}

        postagem = requests.post("https://appconafer.herokuapp.com/blog/api/", data=params, headers=headers)
        self.assertEqual(postagem.status_code, status.HTTP_201_CREATED)

    def test_api_add_postagem_sem_token(self):

        params = {
            "title": "What is Lorem Ipsum?",
            "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
            "image_url": "https://lipsum.com/images/banners/black_120x90.gif",
            "user": 1,
        }

        postagem = requests.post("https://appconafer.herokuapp.com/blog/api/", data=params)
        self.assertEqual(postagem.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_api_get_listagem_com_token(self):

        headers = {"Authorization": f"token {self.token}"}

        postagem = requests.get("https://appconafer.herokuapp.com/blog/api/", headers=headers)
        self.assertEqual(postagem.status_code, status.HTTP_200_OK)

    def test_api_get_listagem_sem_token(self):

        postagem = requests.get("https://appconafer.herokuapp.com/blog/api/")
        self.assertEqual(postagem.status_code, status.HTTP_401_UNAUTHORIZED)
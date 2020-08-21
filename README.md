### Rota para registro de usuário;

Campos requeridos: `email, password, password_confirm`

Campos opcionais: `first_name, last_name, phone, avatar`

```python      
url = 'https://appconafer.herokuapp.com/accounts/register/'

params = {
            "email": "teste-api@teste.com",
            "password": "senha2020",
            "password_confirm": "senha2020",
        }

user = requests.post(url, data=params)
```

- Retorno:
       
```json   
{'id': 1, 'last_name': '', 'email': 'teste-api1@teste.com', 'phone': None, 'avatar': None, 'first_name': None}
```

- Todos os parâmetros:

```python
params ={
    "email": "teste-api2@teste.com",
    "password": "senha2020",
    "password_confirm": "senha2020",

    "first_name": "João",
    "last_name": "Ferreira Silva",
    "phone": "38999994445",
    "avatar": "https://image.freepik.com/vetores-gratis/perfil-de-avatar-de-homem-no-icone-redondo_24640-14044.jpg",
}
```

#### Rota para login de usuário que retorna um Token único para o usuário;
Campos requeridos: `username, password`


```python
url = 'https://appconafer.herokuapp.com/api-login/'

credenciais = {'username': 'teste-api@teste.com', 
               'password': 'senha2020'
               }

token = requests.post(url, data=credenciais)
```

- Retorno:

```json
{
    "token": "a5980ebd7a9a4255fd5c7ff09db61e79db28a0f9"
}
```

#### Rota para adição postagem com autenticação/credencial com Token;
    
```python
url = 'https://appconafer.herokuapp.com/blog/api/'

params = {
    "title": "What is Lorem Ipsum?",
    "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
    "image_url": "https://lipsum.com/images/banners/black_120x90.gif",
    "user": 1,
        }
headers = {"Authorization": "token a5980ebd7a9a4255fd5c7ff09db61e79db28a0f9"}

postagem = requests.post(url, data=params, headers=headers)
```

- Retorno:

```json
{
    'id': 2, 
    'title': 'What is Lorem Ipsum?', 
    'description': "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.", 
    'image_url': 'https://lipsum.com/images/banners/black_120x90.gif', 
    'user': 1
}
```


#### Rota para edição da postagem com autenticação/credencial com Token;


```python
url = 'https://appconafer.herokuapp.com/blog/api/2/'

params = {
    "title": "Why do we use it?",
    "description": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).",
    "image_url": "https://www.lipsum.com/images/banners/grey_250x250.gif",
    "user": 1,
        }
headers = {"Authorization": "token a5980ebd7a9a4255fd5c7ff09db61e79db28a0f9"}

postagem = requests.put(url, data=params, headers=headers)
```

- Retorno:

```json
{
    'id': 2, 
    'title': 'Why do we use it?', 
    'description': "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).", 
    'image_url': 'https://www.lipsum.com/images/banners/grey_250x250.gif', 
    'user': 1
}
```


#### Rota para listagem de postagens com autenticação/credencial com Token;


```python
url = 'https://appconafer.herokuapp.com/blog/api/'

headers = {"Authorization": "token a5980ebd7a9a4255fd5c7ff09db61e79db28a0f9"}

postagem = requests.get(url, headers=headers)
```

- Retorno:

```json
[   
    {
        'id': 2, 
        'title': 'Why do we use it?', 'description': "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).", 
        'image_url': 'https://www.lipsum.com/images/banners/grey_250x250.gif', 
        'user': 1
    }
]
```


- Deploy no HEROKU gratuitamente.

```
https://appconafer.herokuapp.com/admin
- Email: admin@admin.com 
- Senha: admin2020*
```

- Usuário deve conter no mínimo: email e senha.

- Estrutura de postagem: id, título, descrição e URL de imagem (não armazenar imagem, trabalhar com URLs da web.).

- Restrições: não deve ser possível adicionar ou listar postagem sem autenticação de Token de usuário logado.

- Sugestão: Usar Django REST framework.


 

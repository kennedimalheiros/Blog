Teste Dev Back-end
Linguagem: Python | Framework: Django
DESCRIÇÃO
Olá, tudo bem? Para avaliação da nossa vaga você deve fazer uma REST-API usando Django e
as bibliotecas que julgar necessárias, contanto que siga as especificações abaixo e seja feito no
final o deploy da aplicação no HEROKU (usando PostgreSQL ou MySQL).

ESPECIFICAÇÕES

- Rota para registro de usuário;

        http://127.0.0.1:8000/accounts/register/

- Rota para login de usuário que retorna um Token único para o usuário;
- Rota para adição de postagem com autenticação/credencial com Token;
- Rota para listagem de postagens com autenticação/credencial com Token;
- Deploy no HEROKU gratuitamente.
- Usuário deve conter no mínimo: email e senha.
- Estrutura de postagem: id, título, descrição e URL de imagem (não armazenar imagem, trabalhar com URLs da web.).
- Restrições: não deve ser possível adicionar ou listar postagem sem autenticação de Token de usuário logado.
- Sugestão: Usar Django REST framework.
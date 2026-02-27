# Cars Database Application (EN-US)

![Python](https://img.shields.io/badge/Python-3.13-blue?style=flat)
![Django](https://img.shields.io/badge/Django-4.2-green?style=flat)
![DRF](https://img.shields.io/badge/DRF-3.14-red?style=flat)

Sistema fullstack para o controle e o acompanhamento de usuários e carros registrados, com controle de permissões baseado em roles e API REST autenticada.

## Instalação

```bash
git clone https://github.com/RaphaelReggiani/app_cars_db
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
python manage.py migrate
python manage.py runserver
```

## Estrutura do Projeto

```bash
app_cars_db/
├── core/
│   ├── settings.py
│   └── urls.py
│
├── cars/
│   ├── urls.py
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── choices.py
│   ├── validators.py
│   ├── api_views.py
│   ├── api_urls.py
│   ├── serializers.py
```

## Stack Utilizada

- Python 3.13.4;
- Django;
- Django REST Framework (DRF);
- MySQL;
- HTML5 + CSS3;
- Autenticação via TokenAuthentication (DRF).

## 🔧 Funcionalidades

- Cadastramento de usuários no site;
- Seção de login e signup de usuários (com as devidas validações de nome, e-mail, telefone, username e senha, icluindo hashing de senha);
- O registro de carros só ocorre quando o usuário estiver logado;
- É possível realizar uma consulta de todos os carros já cadastrados no site, porém com limitações de visualizações e impedimento de edição;
- Permissões de usuários, onde: um usuário não pode modificar as informações pessoais e/ou carros cadastrados por outros usuários, podendo apenas consultar as informações de carros cadastrados por outros usuários;
- Funcionalidade de: Esqueceu a senha?;
- Funcionalidade de filtros para pesquisas de carros cadastrados (geral e do usuário);
- Opção de edição das informações do carro, com permissão apenas para o usuário dono do carro;
- Opção de atualização de dados do usuário (nome, e-mail, telefone e país de origem).

## Imagens da Aplicação

### Página Inicial - Sem login
![Home Page without login](readme_assets/home_page.png)

### Página Inicial  
![Home Page logged](readme_assets/home_page_w_login.png)

### Cadastro de Usuários - Parte 1
![Sign up / Log in](readme_assets/signup_login_page.png)

### Cadastro de Usuários - Finalização (Nickname e password)
![User register](readme_assets/user_finalize_register_page.png)

### Informações do Usuário  
![User informations](readme_assets/user_informations_page.png)

### Página de Esqueceu a senha?  
![Forgot password](readme_assets/forgot_password_page.png)

### Registro de Carro  
![New car register](readme_assets/new_car_registration.png)

### Registro de Carro - Sucesso no registro
![New car register - Success](readme_assets/car_registration_successful_w_login.png)

### Registro de Carro - Error (sem login)
![New car register - Error](readme_assets/new_car_registration_error_popup.png)

### Página de todos carros cadastrados  
![All cars page](readme_assets/all_cars_page_w_filter.png)

### Página de todos carros cadastrados pelo usuário (My cars)
![My cars page](readme_assets/my_cars_page.png)

### Visualização das informações do carro sem login
![Car page without login](readme_assets/car_data_wo_login_or_car_owner.png)

### Visualização das informações do carro logado
![Car page logged](readme_assets/car_data_w_login.png)

### Visualização das informações do carro logado, porém não sendo o dono do carro
![Car page logged (Not car owner)](readme_assets/car_data_w_login_noowner.png)

### Atualização das informações do carro (apenas logado e dono do carro) - parte 1
![Car information update](readme_assets/car_data_update_part_1.png)

### Atualização das informações do carro (apenas logado e dono do carro) - parte 2
![Car information update](readme_assets/car_data_update_part_2.png)

### Atualização das informações principais do carro (apenas logado e dono do carro)
![Car main information update](readme_assets/main_car_data_update.png)

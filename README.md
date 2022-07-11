# Passo a passo

## Instalação Pyhton

Tenha o python instalado na sua máquina.

```
https://www.python.org/downloads/
```

## Configurando venv

Crie uma venv que é um ambiente virtual onde será instaldo todas as dependências
```
python -m venv env
```

Inicie a venv
```
env\Scripts\activate
```

## Instalando dependências

Instale as dependências do projeto
```
pip install -r requirements.txt
```

## Banco de dados

O banco de dados deve ter as seguites configurações

```
Nome: teste_de_mesa
Usuário: root
Senha: ''
```

## Executando projeto

entre na pasta do projeto
```
cd teste_de_mesa
```

Transfira as tabelas e configurações para o banco

```
python manage.py migrate
```

Dê start na aplicação
```
python manage.py runserver
```


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

Inicie a venv, ao iniciar o nome (env) aparecerá na linha de comando
```
env\Scripts\activate
```

## Instalando dependências

Entrena pasta teste_de_mesa e instale as dependências do projeto
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

## Acessando projeto

Insira a url no seu browser 
```
http://127.0.0.1:8000/
```

## Hospedagem da aplicação
A aplicação não está hospedada, pois os locais de hospedagem do mysql geram cobranças, inviabilizando a hospedagem  

# Possíveis problemas

Em alguns testes a aplicação gerou erros quando uma função era executada, como no exemplo abaixo:

```
def imprimir(texto):
    print(texto)

imprimir("Olá Mundo!")
```

## Demonstração

![front page](https://github.com/WelvisSS/projetoBD2/blob/main/Demo/Home.png)
![front page](https://github.com/WelvisSS/projetoBD2/blob/main/Demo/Inserir%20programas.png)
![front page](https://github.com/WelvisSS/projetoBD2/blob/main/Demo/Lista%20de%20testes.png)
![front page](https://github.com/WelvisSS/projetoBD2/blob/main/Demo/Teste.png)



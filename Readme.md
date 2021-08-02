# Projeto Observer

<img src = "https://img.shields.io/badge/python-3.7.6-blue">

## Ambiente de desenvolvimento
Após clonar o repositório, vamos criar um workspace.

```bash
[user@host ~]$ python3 -m venv .venv
```

Para ativar e mudar para este ambiente:

```bash
[user@host ~]$ source .venv/bin/activate
```

Atualizando o gerenciador Pip:

```bash
[user@host ~]$ pip install --upgrade pip
```

Instalando as dependências:

```bash
[user@host ~]$ pip install -r requirements.txt
```

## Diagrama

## Estrutura de códigos

### requirements.txt

Deve ser utilizado para facilitar as depências do aplicativo

#### Arquivo site.txt

Armazena as URL's a serem checadas, deve se respeitar o cabeçalho, para inserir novos valores basta pular uma linha.

``` 
File  site.txt
---> URL
---> https://www.google.com.br
```

#### Arquivo endpoint.txt

Armazena endereço e porta de serviços a serem checados, deve se respeitar o cabeçalho,para inserir novos valores, basta pular uma linha e adicionar o host ou ip, seguido de ";" mais a porta.

```
File  endpoint.txt
---> IP;PORTA
---> 192.168.0.1;22
---> localhost;5432
```

### Iniciando:

```sh
python3 observer.py
```

### Iniciando Sched:
A diferença entre eles é que este aplicativo roda a e intervalos determinados.

```sh
python3 sched.py
```

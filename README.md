# Manipulando arquivos CSV

A aplicação consiste em um script de mesclagem e verificação de aquivos com extensão CSV.

## Instalação/Utilização

Para ter acesso à estrutura da aplicação, faça o fork e depois clone este projeto.

Crie um ambiente de desenvolvimento, digite no terminal:

```json
python -m venv venv --upgrade-deps
```

Acesse o ambiente de desenvolvimento, digite no terminal:

```json
source venv/bin/activate
```

Instale as dependências do projeto, digite no terminal:

```json
pip install -r requirements.txt
```

## Executando

<h3 align='center'> Mesclando diversos arquivos em 1 só</h3>

`Acesse o diretório app, digite no terminal: `

```json
cd app
```

`E rode o comando no terminal:`

```json
python main.py
```

Caso dê tudo certo, a resposta será assim:

`Um arquivo master_file.csv será criado dentro do diretório app`

```json
agencia;conta;saldo;status
1234;12345-6;350,5;A
4567;45678-9;250,5;B
7890;78912-3;150,5;P
8888;78912-3;150,5;I
9898;78912-3;10,5;P
7890;78912-3;-30;A
3636;78912-3;50;B
7890;78912-3;1500,5;A
1190;78912-3;1150,5;I
1234;12345-6;350,5;A
4567;45678-9;250,5;B
7890;78912-3;150,5;P
4747;78912-3;150,5;I
7890;78912-3;10,5;P
1324;78912-3;-30;A
7890;78912-3;50;B
7890;78912-3;1500,5;A
1190;78912-3;1150,5;I
1234;12345-6;350,5;A
4567;45678-9;250,5;B
7890;78912-3;150,5;P
9999;78912-3;150,5;I
7890;78912-3;10,5;P
5555;78912-3;-30;A
7890;78912-3;50;B
4444;78912-3;1500,5;A
1190;78912-3;1150,5;I
1234;12345-6;350,5;A
4567;45678-9;250,5;B
7890;78912-3;150,5;P
7777;78912-3;150,5;I
7890;78912-3;10,5;P
7858;78912-3;-30;A
7890;78912-3;50;B
5858;78912-3;1500,5;A
1190;78912-3;1150,5;I
```

Caso alguma das linha tenha dados incorretos, a resposta no terminal será assim:

```json
['4567', '45678-9', '250,5', 'U'] Dados incorretos
['78905', '78912-3', '150,5', 'P'] Dados incorretos
['7890', '789142-3', '50', 'B'] Dados incorretos
['1190', '78912-3', '1150,5', 'Z'] Dados incorretos
```

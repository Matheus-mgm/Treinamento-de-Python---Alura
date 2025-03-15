import os

pessoas = [{'nome':'Matheus', 'idade':'18', 'cidade': 'São Paulo'}]

def cadastro():
    nome = input('Digite o nome: ')
    idade = input('Digite a idade: ')
    cidade = input('Digite a cidade: ')
    pessoa = {'nome':nome, 'idade': idade, 'cidade': cidade}
    pessoas.append(pessoa)

def listando():
    for pessoa in pessoas:
        nome = pessoa['nome']
        idade = pessoa['idade']
        cidade = pessoa['cidade']
        print(f'- {nome.ljust(20)} | {idade.ljust(20)} | {cidade}')
import os
import json

def main():
    celulares = iniciando("celulares.bd")
    inicio = tela_inicial()
    opcoes = int(input(inicio))

    while opcoes != 0:
        if opcoes == 1:
            buscar_marca(celulares)


        elif opcoes == 2:
            celular = cadastrar()
            celulares.append(celular)

        elif opcoes == 3:
            listar_celulares(celulares)

        input("<enter> para continuar")
        opcoes = int(input(inicio))
        finalizar("celulares.bd", celulares)


def tela_inicial():
    menu = "----Escolha uma opção------ \n"
    menu += "1 - Buscar por marca \n"
    menu += "2 - Cadastrar novo celular: \n"
    menu += "3 - Listar celulares \n"
    menu += "0 - Fializar \n"
    menu += "-------------------------- \n"

    return menu


def cadastrar():
    celular = {}
    nome = input("Nome: ")
    marca = input("Marca: ")
    preco = float(input("Preço: "))

    celular['Nome'] = nome
    celular['Marca'] = marca
    celular['Preço'] = preco

    return celular

def buscar_marca(celulares):
    cont = 0
    marca = input("Digite a marca do celular: ")
    for i in celulares:
        if i['Marca'] == marca:
            cont += 1
            print(i['Nome'])
        
    if cont == 0:
        print("Não existe celulares com essa marca!")

    opcao = int(input("Digite 1 para consultar um celular ou 0 para sair: "))
    acao = 9

    while opcao != 0 and acao != 0:
        if opcao == 1:
            nome = input("Informe o nome do celular que deseja consultar: ")
            acao = int(input("Deseja: 1- Mostrar detalhes, 2-Editar, 3-Remover, 4-Duplicar Registro, 0-Sair?: "))

            while acao != 0:
                if acao == 1:
                    consulta(celulares, nome)
                    acao = int(input("Deseja: 1- Mostrar detalhes, 2-Editar, 3-Remover, 4-Duplicar Registro, 0-Sair?: "))
                
                elif acao == 2:
                    editar(celulares, nome)
                    acao = int(input("Deseja: 1- Mostrar detalhes, 2-Editar, 3-Remover, 4-Duplicar Registro, 0-Sair?: "))

                elif acao == 3:
                    remover(celulares, nome)
                    acao = int(input("Deseja: 1- Mostrar detalhes, 2-Editar, 3-Remover, 4-Duplicar Registro, 0-Sair?: "))

                elif acao == 4:
                    duplicar(celulares, nome)
                    acao = int(input("Deseja: 1- Mostrar detalhes, 2-Editar, 3-Remover, 4-Duplicar Registro, 0-Sair?: "))


def editar(celulares, nome):
    opcao = int(input("Deseja apagar e criar um novo? 1- Sim 2-Não"))
    if opcao == 1:
        remover(celulares, nome)
        print("Crie um novo: ")
        cadastrar()

def duplicar(celulares, nome):
    elemento = 0
    for i in celulares:
        if i['Nome'] == nome:
            elemento = i
    
    celulares.append(elemento)
    print("Item duplicado com sucesso!!")

def remover(celulares, nome):
    for i in celulares:
        if i['Nome'] == nome:
            celulares.remove(i)
        
    print("Celular removido com sucesso!")


def consulta(celulares, nome):
    for i in celulares:
        if i['Nome'] == nome:
            print("Nome:", i['Nome'])
            print("Marca:", i['Marca'])
            print("Preço:", i['Preço'])
            print(12*"-")


def listar_celulares(celulares):
    if len(celulares) == 0:
        print("Não existem celulares cadastrados!")

    else:    
        for i in celulares:
            print("Nome:", i['Nome'])
            print("Marca:", i['Marca'])
            print("Preço:", i['Preço'])
            print(12*"-")


def iniciando(nome_arquivo):
    lista_celular = []
    if os.path.exists(nome_arquivo):
        arquivo = open(nome_arquivo, "r")
        dados = arquivo.readline()
        arquivo.close()
        lista_celular = json.loads(dados)
    
    return lista_celular


def finalizar(nome_arquivo, celulares):
    dados = json.dumps(celulares)
    arquivo = open(nome_arquivo, "w")
    arquivo.write(dados)
    arquivo.close()
    


main()

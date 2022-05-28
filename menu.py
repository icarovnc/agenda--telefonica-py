import pandas as pd #ultilizo apenas para visualizar os contatos na função listar_contatos

def cabecalho(text):
    print('-' * 40)
    print(text.center(40))
    print('-' * 40)

def menu_principal():
    ''''
    exibe as opções para o usuário
    '''
    lista = ler_contatos() #inicializa e carrega a lista de contatos

    while True:
        try:
            cabecalho('MENU')
            print('Opções')
            print('[1] - Adicionar contato')
            print('[2] - Alterar Contato')
            print('[3] - Excluir Contato')
            print('[4] - Buscar Contato')
            print('[5] - Listar Contato')
            print('[6] - Sair')
            opcao = int(input('>'))
            if opcao == 1:
                adicionar_contato(lista)
                salvar_contatos(lista)
            elif opcao == 2:
                alterar_contato(lista)
                salvar_contatos(lista)
            elif opcao == 3:
                excluir_contato(lista)
                salvar_contatos(lista)
            elif opcao == 4:
                buscar_contato(lista)
            elif opcao == 5:
                listar_contato(lista)
            elif opcao == 6:
                print('Saindo do programa')
                break
            else:
                print ("\n" * 130) 
                print('Opção inválida. Tente novamente')
        except ValueError:
            print ("\n" * 130) 
            print("-> SELECIONE SOMENTE AS OPÇÕES LISTADAS ABAIXO <-")

def adicionar_contato(lista):
    ''''
    recebe os dados do contato em forma de dicionário e adiciona a uma lista
    '''
    cabecalho('ADICIONAR CONTATO')
    while True:
        email = input('Digite o e-mail do contato: ').strip().lower()
        if validar_email(email):
            if not existe_contato(lista, email): #o email recebido será único
                break
            else:
                print('Email já foi ultilizado. Tente outro email')
        else:
            print('Tente um e-mail válido')
            print('-' * 40)
            continue

    contato = {
        'email' : email,
        'nome' : input('Digite o nome: ').strip().capitalize(),
        'telefone' : input('Digite o telefone: ').strip(),
    }

    lista.append(contato) #adiciona o dicioário à lista
    print(f'O contato {contato["nome"]} foi cadastrado com sucesso')

def alterar_contato(lista):
    ''' 
    pesquisa pelo email do contato a ser alterado, e faz a alteração dos dados caso ele exista na lista
    '''
    cabecalho('ALTERAR CONTATO')
    email = str(input('Digite o e-mail do contato a ser alterado: ')).strip().lower()
    if existe_contato(lista, email):
        for contato in lista:
            if contato["email"] == email: 
                print('Contato encontrado: ')
                print()
                print(f'\tNome: {contato["nome"]}')
                print(f'\tTelefone: {contato["telefone"]}')
                print(f'\tEmail: {contato["email"]}')
                print(F'=' * 40)
                
                contato["email"] = input('Digite o novo email do contato: ').strip().capitalize()
                if validar_email(email):
                    contato["nome"] = input('Digite o novo nome do contato: ').strip().capitalize()
                    contato["telefone"] = input('Digite o novo telefone do contato: ').strip()

                    print('Os dados do contato foram alterados com sucesso.')
                    break
                else:
                    print('Email inválido')
    else:
            print(f'Não existe contato cadastrado no sistema como o email {email} \n')

def excluir_contato(lista):
    ''''
    pesquisa pelo email do contato e exclui caso ele exista na lista
    '''
    cabecalho('EXLUIR DE CONTATOS')
    email = str(input('Digite o e-mail do contato a ser excluído: ')).strip().lower()
    if existe_contato(lista, email):
        for i, contato in enumerate(lista):
            if contato["email"] == email:
                print('Contato encontrado: ')
                print()
                print(f'\tNome: {contato["nome"]}')
                print(f'\tTelefone: {contato["telefone"]}')
                print(f'\tEmail: {contato["email"]}')
                print()

                lista.pop(i)
                print('O contato foi apagado')
                break
    else:
            print(f'Não existe contato cadastrado no sistema como o email {email} \n')

def buscar_contato(lista):
    ''''
    pesquisa pelo email do contato exibe caso ele exista
    '''
    cabecalho('BUSCA DE CONTATOS')
    email = str(input('Digite o e-mail do contato a ser encontrado: ')).strip().lower()
    if existe_contato(lista, email):
        for contato in lista:
            if contato["email"] == email:
                print('Contato encontrado: ')
                print()
                print(f'Nome: {contato["nome"]}')
                print(f'Telefone: {contato["telefone"]}')
                print(f'Email: {contato["email"]}')
                print(F'=' * 40)
                break
    else:
            print(f'Não existe contato cadastrado no sistema como o email {email} \n')

def listar_contato(lista):
    '''
    exibe todos os contatos guardados no arquivo
    '''
    opt = ''
    print('LISTA DE CONTATOS')
    while opt != '99999':
        if len(lista) > 0:
            print("\n" * 130) 
            contatos = pd.DataFrame(lista) #cria um dataframe a partir da lista de contatos
            print(contatos) #exibe o dataframe
        else:
            print('Não existe contato cadastrado no sistema!')
        opt = input('Selecione qualquer tecla para voltar ao menu: ')
        print ("\n" * 130)
        break

def salvar_contatos(lista):
    '''
    abre o arquivo txt e salva a lista no arquivo
    '''
    arq = open('contatos.txt', 'w') #cria arquivo caso nao exista
    for contato in lista:
        arq.write(f'{contato["nome"]};{contato["telefone"]};{contato["email"]}\n')
    arq.close()

def ler_contatos():
    '''
    abre o arquivo txt e adiciona o conteúdo à lista, caso não exista o arquivo a função ignora
    '''
    lista = []
    try:
        arq = open('contatos.txt', 'r') #abre o arquivo
        for linha in arq.readlines():
            coluna = linha.strip().split(';')

            contato = {
                'email' : coluna[2],
                'nome' : coluna[0],
                'telefone' : coluna[1],
            }
            lista.append(contato)
        arq.close()
    except FileNotFoundError:
        pass
    return lista

def validar_email(email):
    '''
    se começar com @ retorna False
    se a posição do ultimo ponto for antes do arroba retorna False
    se tem três caracteres antes do ultimo ponto retorna False

    caso passe por todas as condições retorna True
    '''
    arroba = email.find("@")
    ponto = email.rfind(".")
    if arroba < 1 or ponto < arroba + 2 or ponto + 2 >= len(email):
        return False
    return True

def existe_contato(lista, email):
    '''
    varre a lista e procura um email igual ao recebido no parametro
    '''
    if len(lista) > 0:
        for contato in lista:
            if contato["email"] == email:
                return True
        return False
    
menu_principal() #inicia a execução do programa


def salvar_contatos(lista):
    arq = open('contatos.txt', 'w') #cria arquivo caso nao exista
    for contato in lista:
        arq.write(f'{contato["nome"]};{contato["telefone"]};{contato["email"]}\n')
    arq.close()

def ler_contatos():
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

def existe_contato(lista, email):
    if len(lista) > 0:
        for contato in lista:
            if contato["email"] == email:
                return True
        return False

def adicionar_contato(lista):
    while True:
        email = input('Digite o e-mail do contato: ').strip().lower()
        if not existe_contato(lista, email):
            break
        else:
            print('Email já foi ultilizado. \nTente outro email')

    #o email recebido será único
    contato = {
        'email' : email,
        'nome' : input('Digite o nome: ').strip().capitalize(),
        'telefone' : input('Digite o telefone: ').strip(),
    }

    lista.append(contato)
    print(f'O contato {contato["nome"]} foi cadastrado com sucesso')
    
def alterar_contato(lista):
    print('ALTERAR CONTATO')
    email = str(input('Digite o e-mail do contato a ser alterado: ')).strip().lower()
    if existe_contato(lista, email):
        for contato in lista:
            if contato["email"] == email:
                print('Contato encontrado: ')
                print()
                print(f'Nome: {contato["nome"]}')
                print(f'Telefone: {contato["telefone"]}')
                print(f'Email: {contato["email"]}')
                print(F'=' * 40)

                contato["nome"] = input('Digite o novo nome do contato: ').strip().capitalize()
                contato["telefone"] = input('Digite o novo telefone do contato: ').strip()

                print(f'Os dados do contato {email} foram alterados com sucesso')
                break

    else:
            print(f'Não existe contato cadastrado no sistema como o email {email} \n')

def excluir_contato(lista):
    print('EXLUIR DE CONTATOS')
    email = str(input('Digite o e-mail do contato a ser excluído: ')).strip().lower()
    if existe_contato(lista, email):
        for i, contato in enumerate(lista):
            if contato["email"] == email:
                print('Contato encontrado: ')
                print()
                print(f'Nome: {contato["nome"]}')
                print(f'Telefone: {contato["telefone"]}')
                print(f'Email: {contato["email"]}')
                print(F'=' * 40)

                lista.pop(i)
                print('O contato foi apagado')
                break
    else:
            print(f'Não existe contato cadastrado no sistema como o email {email} \n')

def buscar_contato(lista):
    print('BUSCAR DE CONTATOS')
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
    print('LISTA DE CONTATOS')
    if len(lista) > 0:
        for c, contato in enumerate(lista):
            print(f'Contato {c + 1}')
            print(f'\tNome: {contato["nome"]}')
            print(f'\tTelefone: {contato["telefone"]}')
            print(f'\tEmail: {contato["email"]}')
            print(F'=' * 40)
        print(f'Existem {len(lista)} contatos na lista telefônica')
    else:
        print('Não existe contato cadastrado no sistema! \n')

def menu_principal():
    lista = ler_contatos() #inicializa e carrega a lista de contatos

    while True:
        print('-' * 30)
        print('MENU DE OPERAÇÕES')
        print('-' * 30)
        print('Opções')
        print('[1] - Adicionar contato')
        print('[2] - Alterar Contato')
        print('[3] - Excluir Contato')
        print('[4] - Buscar Contato')
        print('[5] - Listar Contato')
        print('[6] - Sair')
        opcao = int(input('>'))
        print('-' * 30)
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
            print('Opção inválida. Tente novamente')

menu_principal()
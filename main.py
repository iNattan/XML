import xml.etree.ElementTree as ET

def adicionarContato(agenda, nome, email, telefone):
    contato = ET.Element("Contato")
    ET.SubElement(contato, "Nome").text = nome
    ET.SubElement(contato, "Email").text = email
    ET.SubElement(contato, "Telefone").text = telefone
    agenda.append(contato)
    print('Contato adicionado com sucesso!')

def listarContatos(agenda):
    if not agenda:
        print('A agenda de contatos está vazia.')
    else:
        print('Lista de contatos:')
        print('------------------')
        for contato in agenda:
            print(f'Nome: {contato.find("Nome").text}')
            print(f'Email: {contato.find("Email").text}')
            print(f'Telefone: {contato.find("Telefone").text}')
            print('------------------')
        input('Pressione Enter para continuar...')

def limparArquivo(arquivo):
    agenda = ET.Element("Agenda")
    tree = ET.ElementTree(agenda)
    tree.write(arquivo)
    print('Agenda limpa com sucesso!')

def carregarArquivo(arquivo):
    try:
        tree = ET.parse(arquivo)
        agenda = tree.getroot()
    except ET.ParseError:
        agenda = ET.Element("Agenda")
        tree = ET.ElementTree(agenda)
        tree.write(arquivo)
    return agenda

def salvarContatos(agenda, arquivo):
    tree = ET.ElementTree(agenda)
    tree.write(arquivo)
    print(f'Agenda salva em {arquivo}.')

def listarMenu():
    print('-------- Menu --------')
    print('1- Adicionar contato')
    print('2- Listar contatos')
    print('3- Limpar contatos')
    print('0- Sair')

arquivo = 'lista.xml'
agenda = carregarArquivo(arquivo)
opcao = 0
while True:
    print('')
    listarMenu()
    opcao = int(input('Digite uma opção: '))
    match opcao:
        case 1:
            nome = input('Digite o nome: ')
            email = input('Digite o email: ')
            telefone = input('Digite o telefone: ')     
            adicionarContato(agenda, nome, email, telefone)       
        case 2:    
            listarContatos(agenda)
        case 3:    
            limparArquivo(arquivo)
            agenda = ET.Element("Agenda")
        case 0:
            salvarContatos(agenda, arquivo)
            print('Saindo...')
            break
        case _:
            print('Opção inválida!')
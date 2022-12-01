AGENDA = {}

AGENDA["Guilherme"] = {
    "Telefone": "(31) 99999-0000",
    "Email": "guilherme@provedor.com",
    "Endereço": "Rua Fulano de Tal, Nº 1"
}

AGENDA["Patrick"] = {
    "Telefone": "(31) 99999-1111",
    "Email": "patrick@provedor.com",
    "Endereço": "Rua Fulano de Tal, Nº 2"
}

def mostrar_contatos():
    for contato in AGENDA:
        print("\nNome: " + contato)
        for item in AGENDA[contato]:
            print("Telefone: " + AGENDA[contato][item])

def buscar_contato(contato_buscado):
    encontrado = False
    for contato in AGENDA:
        if(contato == contato_buscado):
            encontrado = True
            print("\nNome: " + contato)
            print("Telefone: " + AGENDA[contato]["Telefone"])
            print("Email: " + AGENDA[contato]["Email"])
            print("Endereço: " + AGENDA[contato]["Endereço"] + "\n")
    if(encontrado == False):
        print("\nCONTATO NÃO ENCONTRADO!\n")

def adicionar_contato():
    nome = input("\nNome: ")
    AGENDA[nome] = {
        "Telefone": input("Telefone: "),
        "Email": input("Email: "),
        "Endereço": input("Endereço: "),
    }
    print("\nCONTATO NÃO ADICIONADO!\n")

def editar_contato(contato_buscado):
    encontrado = False
    for contato in AGENDA:
        if(contato == contato_buscado):
            encontrado = True
            AGENDA[contato] = {
                "Telefone": input("Telefone: "),
                "Email": input("Email: "),
                "Endereço": input("Endereço: "),
            }
            print("\n>>>>>>>>>> Contato editado!\n")
    if(encontrado == False):
        print("\n>>>>>>>>>> Contato não encontrado!\n")
    
def excluir_contato(contato_buscado):
    AGENDA.pop(contato_buscado)
    print("\n>>>>>>>>>> Contato excluído!\n")

def imprimir_menu():
    print("\n-----------------------------------")
    print("| 1 - MOSTRAR TODOS OS CONTATOS   |")
    print("| 2 - BUSCAR CONTATO              |")
    print("| 3 - ADICIONAR CONTATO           |")
    print("| 4 - EDITAR CONTATO              |")
    print("| 5 - EXCLUIR CONTATO             |")
    print("| 0 - SAIR DA AGENDA              |")
    print("-----------------------------------")

sair = False
while(sair == False):
    imprimir_menu()
    opcao = input("ESCOLHA UMA OPÇÃO: ")
    if(opcao == "1"):
        mostrar_contatos()
    elif(opcao == "2"):
        contato_buscado = input("\nCONTATO BUSCADO: ")
        buscar_contato(contato_buscado)
    elif(opcao == "3"):
        adicionar_contato()
    elif(opcao == "4"):
        contato_buscado = input("\nCONTATO A SER EDITADO: ")
        editar_contato(contato_buscado)
    elif(opcao == "5"):
        contato_buscado = input("\nCONTATO A SER EXCLUÍDO: ")
        excluir_contato(contato_buscado)
    elif(Opcao == "0"):
        sair = True
        print("\nSAINDO...")
    else:
        print("\nOPÇÃO INVÁLIDA!")

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
        print("\n>>>>>>>>>> Contato não encontrado!\n")

def adicionar_contato():
    nome = input("\nNome: ")
    AGENDA[nome] = {
        "Telefone": input("Telefone: "),
        "Email": input("Email: "),
        "Endereço": input("Endereço: "),
    }
    print("\n>>>>>>>>>> Contato adicionado!\n")

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

print("\nTODOS OS CONTATOS")
mostrar_contatos()

print("\n-------------------------------------------------")

print("\nBUSCAR CONTATOS")
buscar_contato(input("\nContato buscado: "))

print("\n-------------------------------------------------")

print("\nINCLUIR CONTATO")
adicionar_contato()

print("\n-------------------------------------------------")

print("\nEDITAR CONTATO")
editar_contato(input("\nContato a ser editado: "))

print("\n-------------------------------------------------")

print("\nTODOS OS CONTATOS")
mostrar_contatos()

print("\n-------------------------------------------------")

print("\nEXCLUIR CONTATO")
excluir_contato(input("\nContato a ser excluído: "))

print("\nTODOS OS CONTATOS")
mostrar_contatos()

print("\n-------------------------------------------------")
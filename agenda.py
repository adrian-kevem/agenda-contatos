AGENDA = {}

AGENDA["Guilherme"] = {
    "Telefone": "(31) 99999-0000",
    "Email": "guilherme@provedor.com",
    "Endereço": "Rua Fulano de Tal, Nº 1"
}

def mostrar_contatos():
    for contato in AGENDA:
        print("\nNome:" + contato)
        print("Telefone: " + AGENDA[contato]["Telefone"])
        print("Email: " + AGENDA[contato]["Email"])
        print("Endereço: " + AGENDA[contato]["Endereço"] + "\n")

mostrar_contatos()


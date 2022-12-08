AGENDA = {}

def mostrar_contatos():
    if AGENDA:
        for contato in AGENDA:
            print("\nNome: " + contato)
            print("Telefone: " + AGENDA[contato]["Telefone"])
            print("Email: " + AGENDA[contato]["Email"])
            print("Endereço: " + AGENDA[contato]["Endereço"])
    else:
        print("\n>>>>>>>>>> Agenda vazia!\n")

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
    print("\n>>>>>>>>>> Contato adicionado!")
    salvar_contatos()

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
            print("\n>>>>>>>>>> Contato editado!")
    if(encontrado == False):
        print("\n>>>>>>>>>> Contato não encontrado!\n")
    salvar_contatos()
    
def excluir_contato(contato_buscado):
    try:
        AGENDA.pop(contato_buscado)
        print("\n>>>>>>>>>> Contato excluído!")
    except KeyError as error1:
        print("\n>>>>>>>>>> Contato inexistente!")
    except Exception as error0:
        print("\n>>>>>>>>>> Algo errado aconteceu!")
    salvar_contatos()

def exportar_contatos():
    try:
        arquivo_exportado = input("DIGITE O NOME DO ARQUIVO A SER EXPORTADO: ")
        with open(arquivo_exportado, "w") as contatos:
            for contato in AGENDA:
                nome = contato
                telefone = AGENDA[contato]["Telefone"]
                email = AGENDA[contato]["Email"]
                endereco = AGENDA[contato]["Endereço"]
                contatos.write(f"{nome},{telefone},{email},{endereco}\n")

        print("\n>>>>>>>>>> Contatos exportados com sucesso!\n")
    except:
        print("\n>>>>>>>>>> Algum erro ocorreu!\n")


def importar_contatos(arquivo_buscado):
    try:
        with open(arquivo_buscado, "r") as contatos:
            conteudo = contatos.readlines()
            for linha in conteudo:
                detalhes_contato = linha.strip().split(",")
                AGENDA[detalhes_contato[0]] = {
                    "Telefone": detalhes_contato[1],
                    "Email": detalhes_contato[2],
                    "Endereço": detalhes_contato[3],
                }
        print(">>>>>>>>>> Contatos importados com sucesso!\n")
    except FileNotFoundError:
        print("\n>>>>>>>>>> Arquivo inexistente!")
    except:
        print("\n>>>>>>>>>> Algo errado aconteceu!")

def salvar_contatos():
    try:
        with open("contatos.csv", "w") as contatos:
            for contato in AGENDA:
                nome = contato
                telefone = AGENDA[contato]["Telefone"]
                email = AGENDA[contato]["Email"]
                endereco = AGENDA[contato]["Endereço"]
                contatos.write(f"{nome},{telefone},{email},{endereco}\n")

        print(">>>>>>>>>> Contatos salvos com sucesso!\n")
    except:
        print("\n>>>>>>>>>> Algum erro ocorreu!\n")

def imprimir_menu():
    print("\n-----------------------------------")
    print("| 1 - MOSTRAR TODOS OS CONTATOS   |")
    print("| 2 - BUSCAR CONTATO              |")
    print("| 3 - ADICIONAR CONTATO           |")
    print("| 4 - EDITAR CONTATO              |")
    print("| 5 - EXCLUIR CONTATO             |")
    print("| 6 - EXPORTAR CONTATOS           |")
    print("| 7 - IMPORTAR CONTATOS           |")
    print("| 0 - SAIR DA AGENDA              |")
    print("-----------------------------------")

importar_contatos("contatos.csv")

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
    elif(opcao == "6"):
        exportar_contatos()
    elif(opcao == "7"):
        arquivo_buscado = input("ARQUIVO BUSCADO: ")
        importar_contatos(arquivo_buscado)
    elif(opcao == "0"):
        sair = True
        print("\nSAINDO...")
    else:
        print("\nOPÇÃO INVÁLIDA!")

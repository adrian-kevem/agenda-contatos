try:
    a = float(input("Digite o valor de 'a': ")) #ValueError
    b = float(input("Digite o valor de 'b': "))

    print(a/b) #ZeroDivisionError
except ValueError as error1:
    print("Entrada inválida!")
    print(error1)
except ZeroDivisionError as error2:
    print("Não é possível dividir por zero!")
    print(error2)
except Exception as error0:
    print("Algum erro ocorreu!")
    print(error0)
finally:
    print("FIM DO PROGRAMA")
print("Teste")
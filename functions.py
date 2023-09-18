import datetime
opcao = input("Opção 1: data por extenso;\nOpção 2: arquivo texto;\nOpção 3: sair da aplicação;\nOpç3ão escolhida:")

if opcao == 1:
    date = input("Escreva a data por extenso:")
    try:
        if not isinstance(date, str):
            raise ValueError
    except ValueError:
        print("A data precisa ser por extenso")
    else:
        
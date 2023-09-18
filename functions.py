import dates_str
import dates_file

def time_space():
    opcao = input("Opção 1: data por extenso;\nOpção 2: arquivo texto;\nOpção 3: sair da aplicação;\nOpção escolhida:")

    meses = {"Janeiro": 1, "Fevereiro": 2, "Março": 3, "Abril": 4, "Maio": 5, "Junho": 6, "Julho": 7, "Agosto": 8, "Setembro": 9, "Outubro": 10, "Novembro": 11, "Dezembro": 12 } 

    if opcao == '1':
        dates_str.option1()

    elif opcao == "2":
        dates_file.option2()

    elif opcao == "3":
        print("Programa encerrado")

    else:
        print("Opção não existente")
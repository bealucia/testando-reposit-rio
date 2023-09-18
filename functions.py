from datetime import date
opcao = input("Opção 1: data por extenso;\nOpção 2: arquivo texto;\nOpção 3: sair da aplicação;\nOpção escolhida:")

if opcao == '1':
    date = input("Escreva as datas por extenso:")
    print(date)
    meses = {"Janeiro": 1, "Fevereiro": 2, "Março": 3, "Abril": 4, "Maio": 5, "Junho": 6, "Julho": 7, "Agosto": 8, "Setembro": 9, "Outubro": 10, "Novembro": 11, "Dezembro": 12 } 
    try:
        str_date = date.split()
        str_date[2] = meses[str_date[2]]
        str_date[8] = meses[str_date[8]]
        print(type(int(str_date[0])))
        d0 = date(int(str_date[4]), int(str_date[2]),int(str_date[0]))
        d1 = date(int(str_date[10]), int(str_date[8]),int(str_date[6]))

        print("Diferença de dias:", d1-d0)
    except ValueError:
        print("A data precisa ser por extenso")
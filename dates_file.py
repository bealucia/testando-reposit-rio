"""Módulo para arquivo de texto contendo as datas"""
from datetime import date

meses = {"Janeiro": 1, "Fevereiro": 2, "Março": 3, "Abril": 4, "Maio": 5, "Junho": 6, "Julho": 7, "Agosto": 8, "Setembro": 9, "Outubro": 10, "Novembro": 11, "Dezembro": 12 } 

def option2():
    # Arquivo contendo as datas
    arquivo = input("Insira o nome do arquivo: ")

    # Lendo o arquivo
    with open (arquivo) as f:
        dates_list = f.readlines()
    
    dates = dates_list[0]

    try:
        str_date = dates.split()

        str_date[2] = meses[str_date[2]]
        str_date[8] = meses[str_date[8]]
        
        d0 = date(int(str_date[4]), int(str_date[2]),int(str_date[0]))
        d1 = date(int(str_date[10]), int(str_date[8]),int(str_date[6]))

        print("Diferença de dias:", d1-d0)

    except:
        print("A data precisa ser por extenso")
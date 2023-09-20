"""Módulo para arquivo de texto contendo as datas"""
from datetime import date
import doctest

meses = {"Janeiro": 1, "Fevereiro": 2, "Março": 3, "Abril": 4, "Maio": 5, "Junho": 6, "Julho": 7, "Agosto": 8, "Setembro": 9, "Outubro": 10, "Novembro": 11, "Dezembro": 12 } 

def option2():
    """Cálculo da diferença de dias a partir de um arquivo de texto
    """
    # Arquivo contendo as datas
    arquivo = input("Insira o nome do arquivo: ")

    # Lendo o arquivo

    try:
        with open (arquivo) as f:
            dates_list = f.readlines()
        
        dates = dates_list[0]

        str_date = dates.split()

        str_date[2] = meses[str_date[2]]
        str_date[8] = meses[str_date[8]]
        
        d0 = date(int(str_date[4]), int(str_date[2]),int(str_date[0]))
        d1 = date(int(str_date[10]), int(str_date[8]),int(str_date[6]))

        print("\nDiferença de dias: ", d1-d0)

    except FileNotFoundError:
        print("\nArquivo não encontrado")
    except KeyError:
        print("\nEstrutura das datas no arquivo inadequada")
    except ValueError:
        print("\nData não existente")
    except IndexError:
        print("\nElementos faltantes na estrutura das datas")
    except:
        print("\nErro desconhecido")
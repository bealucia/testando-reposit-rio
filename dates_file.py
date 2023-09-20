"""Módulo para arquivo de texto contendo as datas"""
from datetime import date
import doctest

meses = {"Janeiro": 1, "Fevereiro": 2, "Março": 3, "Abril": 4, "Maio": 5, "Junho": 6, "Julho": 7, "Agosto": 8, "Setembro": 9, "Outubro": 10, "Novembro": 11, "Dezembro": 12 } 

def option2():
    """Cálculo da diferença de dias a partir de um arquivo de texto

    Teste normal com "Data.txt"
    >>> option2()
    Insira o nome do arquivo: 
    Diferença de dias:  8410 days, 0:00:00

    Teste com arquivo inexistente
    >>> option2()
    Insira o nome do arquivo: 
    Arquivo não encontrado

    Teste com arquivo com estrutura das datas errada ("Data_wrong_structure.txt")
    >>> option2()
    Insira o nome do arquivo: 
    Estrutura das datas no arquivo inadequada

    Teste com arquivo com data inexistente ("Data_inexistent.txt")
    >>> option2()
    Insira o nome do arquivo: 
    Data não existente

    Teste com arquivo com elementos faltantes nas datas ("Data_missing_elements.txt")
    >>> option2()
    Insira o nome do arquivo: 
    Elementos faltantes na estrutura das datas
    """
    
    # Arquivo contendo as datas
    arquivo = input("Insira o nome do arquivo: ")

    # Lendo o arquivo

    try:
        with open (arquivo) as f:
            dates_list = f.readlines()
        
        dates = dates_list[0]

        str_date = dates.split()

        # Substituindo os nomes dos meses pelos seus valores numéricos
        str_date[2] = meses[str_date[2]]
        str_date[8] = meses[str_date[8]]
        
        d0 = date(int(str_date[4]), int(str_date[2]),int(str_date[0]))
        d1 = date(int(str_date[10]), int(str_date[8]),int(str_date[6]))

        print("\nDiferença de dias: ", d1-d0)

    # Se o arquivo não existir
    except FileNotFoundError:
        print("\nArquivo não encontrado")
    # Se as datas estiverem escritas de forma errada
    except KeyError:
        print("\nEstrutura das datas no arquivo inadequada")
    # Se a data não existir (ex.: 32 de Janeiro de 2021)
    except ValueError:
        print("\nData não existente")
    # Se faltarem elementos nas datas
    except IndexError:
        print("\nElementos faltantes na estrutura das datas")
    # Outros erros
    except:
        print("\nErro desconhecido")

if __name__ == "__main__":
    doctest.testmod(verbose = True)
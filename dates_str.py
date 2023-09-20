"""Módulo contendo execução do aplicativo para a opção das datas em formato de string"""

from datetime import date
import doctest

# Dicionário para substituir as strings dos meses por valores numéricos
meses = {"Janeiro": 1, "Fevereiro": 2, "Março": 3, "Abril": 4, "Maio": 5, "Junho": 6, "Julho": 7, "Agosto": 8, "Setembro": 9, "Outubro": 10, "Novembro": 11, "Dezembro": 12 } 

def option1():
    """Cálculo da diferença de dias com uma string das datas

    Teste 1, entrada: 12 de Abril de 2013 - 21 de Abril de 2036
    >>> option1()
    Escreva as datas por extenso: 
    Diferença de dias: 8410 days, 0:00:00

    Teste 2, entrada: 30 de Fevereiro de 2017 - 14 de Abril de 2022
    >>> option1()
    Escreva as datas por extenso: 
    Data não existente

    Teste 3, entrada: 15 de fevereiro de 2017 - 14 de Abril de 2022
    >>> option1()
    Escreva as datas por extenso: 
    Estrutura das datas inadequada
    """

    dates = input("Escreva as datas por extenso: ")

    try:
        str_date = dates.split()
        
        # Convertendo os nomes dos meses para os valores numéricos correspondentes
        str_date[2] = meses[str_date[2]]
        str_date[8] = meses[str_date[8]]

        # Criando as variáveis das datas com base nos valores da lista da string "splitada"
        d0 = date(int(str_date[4]), int(str_date[2]),int(str_date[0]))
        d1 = date(int(str_date[10]), int(str_date[8]),int(str_date[6]))

        print("\nDiferença de dias:", d1-d0)
    # Erro para converter o mês
    except KeyError:
        print("\nEstrutura das datas inadequada")
    # Data não existente no calendário
    except ValueError:
        print("\nData não existente")
    # Estrutura inserida não segue o padrão
    except IndexError:
        print("\nElementos faltantes na estrutura das datas")
    # Erros não reconhecido
    except:
        print("\nErro desconhecido")


if __name__ == "__main__":
    doctest.testmod(verbose=True)
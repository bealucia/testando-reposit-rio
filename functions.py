import dates_str 
import dates_file

def time_space():
    while True:
        #Essa função dá 3 opções de escolha para o usuário
        opcao = input("\nOpção 1: data por extenso;\nOpção 2: arquivo texto;\nOpção 3: sair da aplicação;\nOpção escolhida: ")

        if opcao == '1':
            # Essa opção recebe duas datas por extenso e faz o cálculo a partir dessas duas datas
            dates_str.option1()

        elif opcao == "2":
            # Essa opção lê um arquivo de texto e faz o cálculo a partir da leitura desse arquivo 
            dates_file.option2()

        elif opcao == "3":
            # Essa opção permite ao usuário a escolha de sair da aplicação
            print("\nPrograma encerrado")
            break

        else:
            # Esse comando é efetuado quando o usuário digita algo diferente de 1, 2 ou 3
            # Ele avisa que outras opções que não sejam 1, 2 ou 3 não são possíveis 
            print("\nOpção não existente")
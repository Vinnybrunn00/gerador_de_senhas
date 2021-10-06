import random as rd
import pyfiglet as fg
import time
import os
import sys

limpar = os.system('cls' if os.name == 'nt' else 'clear')
os.system(limpar)

banner = fg.figlet_format("PASS")
print(banner)

while True:
    try:
        entrada = input("\n➤ Digite 1 para gerar uma senha: ")
        os.system(limpar)
        if not entrada.isdigit():

            print(f'\033[1;31m\n"{entrada}" está errado, Digite 1')

        else:
            if entrada == "1":
                os.system(limpar)
                rede_social = input("Escolha a Rede Social: ")
                minusculas = input("\nDigite letras maiúsculas: ")
                maiusculas = input("Digite letras minúsculas: ")
                numero = input("Digite números: ")
                caracteres = input("Digite caracteres: ")
                print("\n")
                time.sleep(3) 

                todos = minusculas + maiusculas + numero + caracteres
                tamanho = 13
                senha = "".join(rd.sample(todos, tamanho))

                carregar = '===================================]'
                print("GERANDO SENHA [", end='')
                for v in list(carregar):
                    print(v, end='')
                    sys.stdout.flush()
                    time.sleep(00.1)

                print(f"\n\n                            SENHA\n \033[1;31m                       {senha}")

                with open(f'{rede_social}.txt', 'a') as arquivo:
                    print(f'{senha}', file=arquivo)

                time.sleep(1.0)

            else:
                print('ERROR!!!')

    except ValueError:
        print("Letras inválidas")

import random as rd
from rich import print
import time
import sys
import os

limpar = 'cls' if os.name == 'nt' else 'clear'
os.system(limpar)

def Pass():
    while True:
        try:   
            rede_social = str(input('Nome da rede social: '))
            minusculas = str(input('Digite letras minusculas: '))
            maiusculas = str(input('Digite letras Maiusculas: '))
            numeros = input('Digite números: ')
            caracteres = input('Digite caracteres: ')

            value = minusculas + maiusculas + numeros + caracteres
            tamanho = 13
            password = "".join(rd.sample(value, tamanho))
            print(
                'Digite "SIM" se querer salvar a senha em um arquivo.'
                )
            qq = str(input('Opção: '))

            if (qq == 'SIM') or (qq == 'sim'):    
                with open(f'{rede_social}.txt', 'a') as arquivo:
                    print(f'{password}', file=arquivo)
                    print(
                        '[green]Senha salva com sucesso[/] :heavy_check_mark:'
                        )
                    break
            else:
                os.system(limpar)
                print('\nAdeus :) :wave:')
                break

        except:
            os.system(limpar)
            print('[red]Erro, tente novamente[/] :x: \n\n')
            time.sleep(3)
            
Pass()

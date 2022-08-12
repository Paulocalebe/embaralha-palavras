#Construa uma função que receba uma string como parâmetro e
#devolva outra string com os caracteres embaralhados.
#Por exemplo: se função receber a palavra python, pode retornar npthyo,
#ophtyn ou qualquer outra combinação possível, de forma aleatória.
#Padronize em sua função que todos os caracteres serão devolvidos em caixa alta
#ou caixa baixa, independentemente de como foram digitados.

import os
import random
os.system('cls')

def embaralhar(palavra):
    palavra = list(palavra)
    random.shuffle(palavra)
    print(palavra)
    palavra = ''.join(palavra)
    return print( palavra.upper() )

embaralhar(input('Digite uma palavra: '))

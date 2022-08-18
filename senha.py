# Gerador de Senhas Randomicas com 8 caracteres
import random

letra_minuscula = 'abcdefghijklmnopqrstuvwyxz'
letra_maiuscula = 'ABCDEFGHIJKLMNOPQRSTUVWYXZ'
numeros = '0123456789'
simbolos = '!@#$%&*/\?'

usuario = letra_minuscula + letra_maiuscula + numeros + simbolos
lenght_for_pass = 8 # Numero de caracteres 

senha = ''.join(random.sample(usuario, lenght_for_pass))

print(f'Sua senha gerada é {senha}')
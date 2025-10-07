
import os
import time

# Função para limpar a tela
def limpar_tela():
    os.system('cls')

print('Vamos começar a brincadeira:Criando Uma História Maluca 📖')
input ('Clique em enter se estiver preperado')
limpar_tela()

lugar = input('Digite o nome de um lugar:')
limpar_tela()
pessoafamosa = input('Digite o nome de uma pessoa famosa:')
limpar_tela()
verbo = input('Digite um verbo:')
limpar_tela()
objeto = input('Digite o nome de um objeto:')
limpar_tela()
cor = input('Digite o nome de uma cor:')
limpar_tela()
numero = input('Digite um numero:')
limpar_tela()
lugar2 = input('Digite o nome de outro lugar:')
limpar_tela()

print('Criando uma Historia Divertida em 3,2,1..')
time.sleep(2)
limpar_tela()
print(f'Era uma vez, eu fui ao {lugar} com {pessoafamosa}. De repente, encontramos um {objeto} {cor} que começou a {verbo} sem parar! Nós não acreditamos, então decidimos contar {numero} vezes para todo mundo. No fim, o {objeto} {cor} virou a sensação do {lugar2} e todos ficaram impressionados!')
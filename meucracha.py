import os
import time


# Função para limpar a tela
def limpar_tela():
    os.system('cls')

print('Olá, esse é o Departamento Nacional do DEV. Vamos gerar sua carteirinha oficial de membro honorário.')
input('Clique em Enter se estiver pronto!')
limpar_tela()

nome = input('Digite seu nome:')
limpar_tela()
idade = input('Digite sua idade:')
limpar_tela()
linguagem = input('Digite sua linguagem favorita:')
limpar_tela()
emoji = input('Qual emoji deseja usar?')
limpar_tela()

print('Gerando carteirinha...')
time.sleep(2)
limpar_tela()

print('------------------------------------')
print('🖥️ Crachá do DEV')
print(f'Nome:{nome}')
print(f'Idade:{idade} anos')
print(f'Linguagem Favorita:{linguagem}')
print(f'Emoji:{emoji}')
print('------------------------------------')
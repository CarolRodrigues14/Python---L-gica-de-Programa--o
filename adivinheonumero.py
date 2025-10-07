import random
import time
import os

# Função para limpar a tela
def limpar_tela():
    os.system('cls')


print('Vai começar agora a brincadeira: 🎩Adivinhe o número')
input("Pressione Enter quando estiver pronto! ") 
limpar_tela()
print('Pense em número de 1 a 10...🤔')
time.sleep(2)

palpite = random.randint(1,10)
print('🔮 Estou concentrando minha energia mística...')
limpar_tela()
time.sleep(2)
print(f'Você pensou em {palpite}. Acertei?😀')

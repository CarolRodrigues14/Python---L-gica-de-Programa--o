import random

print("🎯 Bem-vindo ao jogo do Número Secreto! 🕵️‍♂️")

# Número secreto fixo ou aleatório
numero_secreto = random.randint(1, 10)
tentativas = 0

while True:
    chute = int(input("Digite um número de 1 a 10: "))
    tentativas += 1
    
    if chute == numero_secreto:
        print(f"🎉 Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas! 🏆")
        break
    elif chute < numero_secreto:
        print("🔼 Tente um número maior! 😅")
    else:
        print("🔽 Tente um número menor! 😅")

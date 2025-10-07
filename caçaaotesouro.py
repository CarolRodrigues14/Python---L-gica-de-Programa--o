# Caça ao Tesouro Espacial 🚀💎

# Criando o tabuleiro 3x3
tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]

# Posição do tesouro
tesouro_linha = 1
tesouro_coluna = 2

# Função para mostrar o tabuleiro
def mostrar_tabuleiro():
    print("\nTabuleiro:")
    for linha in tabuleiro:
        print(' | '.join(linha))
    print()

print("🪐 Bem-vindo ao Caça ao Tesouro Espacial!")
print("Você tem 5 tentativas para encontrar o tesouro 💎\n")

# Loop de 5 tentativas
for tentativa in range(5):
    print(f"Tentativa {tentativa + 1}/5")
    try:
        linha = int(input("Digite a linha (0-2): "))
        coluna = int(input("Digite a coluna (0-2): "))
    except ValueError:
        print("⚠️ Digite apenas números de 0 a 2!\n")
        continue
    
    # Verificar limites
    if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
        print("⚠️ Posição inválida! Tente novamente.\n")
        continue

    # Verificar se já tentou
    if tabuleiro[linha][coluna] != ' ':
        print("⚠️ Você já tentou essa posição!\n")
        continue

    # Verificar acerto
    if linha == tesouro_linha and coluna == tesouro_coluna:
        tabuleiro[linha][coluna] = '💎'
        mostrar_tabuleiro()
        print("🎉 Parabéns! Você encontrou o tesouro! 💎")
        break
    else:
        tabuleiro[linha][coluna] = 'X'
        mostrar_tabuleiro()
        print("❌ Não é aqui. Tente outra posição.\n")
else:
    # Se não achou, mostrar tesouro
    tabuleiro[tesouro_linha][tesouro_coluna] = '💎'
    mostrar_tabuleiro()
    print("O tesouro estava aqui! 💎 Melhor sorte na próxima! 🚀")

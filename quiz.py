
import random

perguntas = [
    ["Qual a linguagem que estamos usando?", "python"],
    ["Quantos bits tem um byte?", "8"],
    ["O que significa IDE?", "ambiente de desenvolvimento integrado"]
]

acertos = 0

for pergunta in perguntas:
  resposta = input(pergunta[0] + '')
  if resposta.lower() == pergunta[1]:
    print("✅ Acertou!")
    acertos +=1
  else:
    print("❌ Errou! A resposta correta é:", pergunta[1])

print(f"Você acertou {acertos} de {len(perguntas)} perguntas!")

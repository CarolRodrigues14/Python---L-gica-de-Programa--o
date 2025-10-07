

import os

# Função para limpar a tela
def limpar_tela():
    os.system('cls')

while True:
  limpar_tela()
  print('Bem-Vindo ao Oráculo de Sabedoria do Python')
  print()
  assunto = input('Digite um assunto de Python (ex: listas, loops, funções...): ')

  match assunto.lower(): # .lower() para não se importar com maiúsculas/minúsculas
      case 'listas':
          print('📚 Listas são como prateleiras: você pode guardar várias coisas organizadas e pegar quando precisar!')
      case 'loops':
          print('🔁 Loops repetem tarefas até você dizer para parar — tipo uma dança infinita de código!')
      case 'funções':
          print('⚡ Funções são como máquinas mágicas: você coloca algo dentro e sempre recebe o mesmo resultado sem precisar repetir o trabalho!')
      case 'if/else':
          print('⚖️ If/else ajuda o código a tomar decisões: se algo acontece, faça isso; senão, faça aquilo!')
      case _:
          print("🤔 Humm... ainda estou aprendendo sobre isso! Tente outro assunto de Python.")    
         
  continuar = input("Quer perguntar sobre outro assunto? (s/n): ")
  if continuar.lower() != "s":
    print("🪄 Até a próxima! Que a sabedoria Python esteja com você! 😄")
    break

    

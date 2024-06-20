import os

restaurantes = [{'nome': 'pizzaria', 'comida': 'pizza', 'status':True}, {'nome': 'pastelaria', 'comida': 'pastel', 'status':False}]

def inicio ():
  print('1. Cadastar Restarurante')
  print('2. Listar Restarurante')
  print('3. Ativar Restarurante')
  print('4. Sair\n')





def cadastrar_novo_restaurante():
  limpar_exibir('Cadastro de novos restaurantes\n')
  nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
  categoria = input(f'Digite a categoria do {nome_do_restaurante}: ')
  dados_restaurante = [{'nome': nome_do_restaurante, 'categoria': categoria, 'status': False}]
  restaurantes.append(dados_restaurante)

  print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso.')
  voltar_ao_menu()

def listar_restaurantes():
  limpar_exibir('Listando os restaurantes\n')
  print(f"{'Nome do Restaurante'.ljust(20)} | {'Categoria'.ljust(28)} | {'Status'}")
  for local in restaurantes:
    nome_restaurante = local['nome']

    print(f"{nome_restaurante.ljust(20)} | comida: {local['comida'].ljust(20)} | status: {local['status']}")
  voltar_ao_menu()


def finalizando ():
  os.system('clear')
  print('Finalizando App\n')

def voltar_ao_menu():
  input('Digite uma tecla para voltar ao menu principal: ')
  main()

def limpar_exibir(texto):
  os.system('clear')
  print(texto)

def alterando_status():
  print('Ativando restaurante\n')
  nome = input('Informe o nome do restaurante que deseja alterar o status: ')
  restaurante_encontrado = False
  for restaurante in restaurantes:
    if nome == restaurante['nome']:
      restaurante_encontrado = True
      restaurante['status'] = not restaurante['status']
      mensagem = f'O status do restaurante {nome} foi ativado com sucesso' if restaurante['status'] else f'o  restaurante {nome} foi desativado com sucesso'
      print(mensagem)
  if not restaurante_encontrado:
    print('O restaurante não foi encontrado')
  voltar_ao_menu()

def opcao_invalida():
  limpar_exibir('Opção Inválida\n')
  voltar_ao_menu()


def escolher_opcao():
  try:
    opcao = int(input('Escolha uma Opcão: '))
    if opcao == 1:
      print(f'A opção {opcao} foi a escolhida')
      cadastrar_novo_restaurante()
    elif opcao == 2:
      print(f'A opção {opcao} foi a escolhida')
      listar_restaurantes()
    elif opcao == 3:
      alterando_status()
    elif opcao == 4:
      finalizando()
  except:
    opcao_invalida()
def main():
  os.system('clear')
  inicio()
  escolher_opcao()


if __name__ == '__main__':
  main()




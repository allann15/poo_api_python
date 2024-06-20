from Models.restaurante import Restaurante
from Models.exce import Livro
from Models.cardapio.item_cardapio import ItemCardapio
from Models.cardapio.prato import Prato
from Models.cardapio.bebida import Bebida

restaurante_japa = Restaurante('Japa', 'Japonesa')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_mexicano.troca()
restaurante_japa.receber_avaliacao('Allan', 6)
restaurante_mexicano.receber_avaliacao('Belly', 5)
restaurante_mexicano.receber_avaliacao('Belly', 2)

livro_habito = Livro('Poder do hábito', 'algum autor', 2005)
livro_teste = Livro('testando', 'roamn', 2008)
livro_foda = Livro('Seja FODA', 'Caio', 2008)



def main():
  pass
  #Restaurante.listar_restaurantes()
  #print(f'{livro_habito.emprestar()} \n{livro_foda}')
  #print(Livro.verificar_disponibilidade(2008))

if __name__ == '__main__':
  main()

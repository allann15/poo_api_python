from Models.cardapio.item_cardapio import ItemCardapio
from Models.cardapio.prato import Prato
from Models.cardapio.bebida import Bebida
from Models.ex_veic.veiculo import Veiculo
from Models.ex_veic.carro import Carro
from Models.restaurante import Restaurante
from Models.cardapio.sobremesa import Sobremesa
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')

novo_prato = Prato('Carne de Sol', 30, 'Carne com queijo coalho')
novo_bebida = Bebida('Guaraná', 5.0, '1L')
nova_sobremesa = Sobremesa('Pudim', 6, 'Limão', '250g')
novo_bebida.aplicar_desconto()
novo_prato.aplicar_desconto()
nova_sobremesa.aplicar_desconto()
novo_carro = Carro('BMW', 'X9', 4)

restaurante_mexicano.adicionar_no_cardapio(novo_bebida)
restaurante_mexicano.adicionar_no_cardapio(novo_prato)
restaurante_mexicano.adicionar_no_cardapio(nova_sobremesa)


def main():
  print(novo_bebida)
  print(novo_carro)
  restaurante_mexicano.exibir_cardapio

if __name__ == '__main__':
  main()

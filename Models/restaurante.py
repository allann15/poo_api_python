from Models.avaliacao import Avaliacao
from Models.cardapio.item_cardapio import ItemCardapio

class Restaurante:
  restaurantes = []
  def __init__(self, nome:str, categoria:str):
    self._nome = nome.title()
    self.categoria = categoria
    self._ativo = False
    self._avaliacao = []
    Restaurante.restaurantes.append(self)
    self._cardapio = []
  def troca(self):
    self._ativo = not self._ativo
    return self._ativo
  def __str__(self):
    return f'{self._nome} | {self.categoria} | {self._avaliacao}'
  @classmethod
  def listar_restaurantes(cls):
    for restaurante in cls.restaurantes:
      print(f'{restaurante._nome} | {restaurante.categoria} | {restaurante.media_avaliacao} | {restaurante.ativo}')

  @property
  def ativo(self):
    return 'Válido' if self._ativo else 'Inválido'

  def receber_avaliacao(self, cliente, nota):
    if nota >= 0 and nota <= 5:
      avaliacao = Avaliacao(cliente, nota)
      self._avaliacao.append(avaliacao)
    else:
      raise Exception('Digite uma nota entre 0 e 5')

  @property
  def media_avaliacao(self):
    if not self._avaliacao:
      return '-'
    media = round(sum(avaliacao._nota for avaliacao in self._avaliacao) / len(self._avaliacao),1)
    return media

  # def adicionar_bebida_no_cardapio(self, bebida):
  #   self._cardapio.append(bebida)
  # def adicionar_prato_no_cardapio(self, prato):
  #   self._cardapio.append(prato)
  def adicionar_no_cardapio (self, item):
    if isinstance(item, ItemCardapio):
      self._cardapio.append(item)

  @property
  def exibir_cardapio(self):
    print(f'Este é o cardapio do restaurante {self._nome}\n')
    for numeracao, item in enumerate(self._cardapio, start=1):
      if hasattr(item,'descricao'):
        mensagem_prato = f'{numeracao}. Nome: {item._nome} | Preço: {item._preco} | Descrição: {item.descricao}'
        print(mensagem_prato)
      elif hasattr(item, 'tipo'):
        mensagem_sobremesa = f'{numeracao}. Nome: {item._nome} | Preço: {item._preco} | Tipo: {item.tipo} | Tamanho: {item.tamanho}'
        print(mensagem_sobremesa)
      else:
        mensagem_bebida = f'{numeracao}. Nome: {item._nome} | Preço: {item._preco} | Tamanho: {item.tamanho}'
        print(mensagem_bebida)
#tests = Restaurante('Praça', 'Gourmet')
#print(tests._nome,tests.troca())
#Restaurante('Pizza', 'Italiana')
#print(Restaurante.listar_restaurantes())

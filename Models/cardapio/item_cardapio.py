from abc import ABC, abstractclassmethod

class ItemCardapio(ABC):
  def __init__(self, nome, preco):
    self._nome = nome
    self._preco = preco
  def __str__(self) -> str:
    return self._nome

  @abstractclassmethod
  def aplicar_desconto(self):
    pass

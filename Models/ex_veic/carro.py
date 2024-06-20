from Models.ex_veic.veiculo import Veiculo

class Carro(Veiculo):
  def __init__(self, marca, modelo, porta):
    super().__init__(marca, modelo)
    self.porta = porta
  def __str__(self) -> str:
    status = 'Ligado' if self._ligado else 'Desligado'
    return f'{self.marca} | {self.modelo} | {status} | {self.porta}'

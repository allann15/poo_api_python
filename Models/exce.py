'''class Carro:
  def __init__(self, modelo:str, cor:str, ano:int) -> None:
    self.modelo = modelo
    self.cor = cor
    self.ano = ano

  def __str__(self) -> str:
    return f'{self.modelo} de cor {self.cor} do ano {self.ano}'



print(Carro('Gol', 'Preto', 2020))'''
class Pessoa:
  def __init__(self, nome:str, aniversario:int, profissao:str) -> None:
    self.nome = nome
    self.aniversario = aniversario
    self.profissao = profissao

  def __str__(self) -> str:
    return f'olá sou o {self.nome}'

  def niver(self) -> int:
    self.aniversario += 1

  @property
  def saudacao(self):
    return f'Olá tenh a profissão de {self.profissao}'

testes = Pessoa('allan', 22, 'Desenvolvedor')
print(testes.saudacao)


class Livro:
  livros = []
  def __init__(self, titulo, autor, ano_publicacao) -> None:
    self.titulo = titulo
    self.autor = autor
    self.ano_publicacao = ano_publicacao
    self.disponivel = True
    Livro.livros.append(self)
  def __str__(self) -> str:
    return f'{self.titulo} | {self.autor} | {self.ano_publicacao} | {Livro.livros}'

  def emprestar(self):
    self.disponivel = False

  @staticmethod
  def verificar_disponibilidade( ano):
    livros_disponiveis = []
    for livro in Livro.livros:
      if livro.ano_publicacao == ano and livro.disponivel:
        livros_disponiveis.append(livro.titulo)
    return livros_disponiveis

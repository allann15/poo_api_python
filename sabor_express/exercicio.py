pessoa = {
  'nome': 'Allan',
  'Idade': 21,
  'Cidade': 'Recife'

}

pessoa['Idade'] = 22
pessoa.update({'Profissão':'Desenvolvedor'})
pessoa.pop('Cidade')
print(pessoa)
print(pessoa.keys())

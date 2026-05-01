import random
#exercício 1

def rolar_dados(n):
  dados = []
  for i in range(n):
    valor = random.randint(1, 6)
    dados.append(valor)
  return dados


def guardar_dado(rolados, estoque, guardar):
  lista=[]
  rol=[]
  i=guardar
  estoque.append(rolados[i])
  for d in range(len(rolados)):
    if d!=i:
      rol.append(rolados[d])
  lista.append(rol)
  lista.append(estoque)
  return lista

#exercício 3
def remover_dado(rolados, guardados, removido):
  rolados.append(guardados[removido])
  guard=[]
  for i in range(len(guardados)):
    if i!=removido:
      guard.append(guardados[i])
  lista=[]
  lista.append(rolados)
  lista.append(guard)
  return lista

#exercício 4
def calcula_pontos_regra_simples(lista):
  dicionario={}
  dicionario[1]=0
  dicionario[2]=0
  dicionario[3]=0
  dicionario[4]=0
  dicionario[5]=0
  dicionario[6]=0
  for i in lista:
    dicionario[i]+=i
  return dicionario
  
#exercício 5
def calcula_pontos_soma(lista):
  soma = 0
  for i in lista:
    soma+=i
  return soma

#exercício 5
def calcula_pontos_sequencia_baixa(lista):
  if 1 in lista and 2 in lista and 3 in lista and 4 in lista:
    return 15
  elif 2 in lista and 3 in lista and 4 in lista and 5 in lista:
    return 15
  elif 3 in lista and 4 in lista and 5 in lista and 6 in lista:
    return 15
  else:
    return 0


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
  

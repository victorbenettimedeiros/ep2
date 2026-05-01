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

#exercício 6
def calcula_pontos_sequencia_baixa(lista):
  if 1 in lista and 2 in lista and 3 in lista and 4 in lista:
    return 15
  elif 2 in lista and 3 in lista and 4 in lista and 5 in lista:
    return 15
  elif 3 in lista and 4 in lista and 5 in lista and 6 in lista:
    return 15
  else:
    return 0

#exercício 7
def calcula_pontos_sequencia_alta(lista):
  if 1 in lista and 2 in lista and 3 in lista and 4 in lista and 5 in lista:
    return 30
  elif 2 in lista and 3 in lista and 4 in lista and 5 in lista and 6 in lista:
    return 30
  else:
    return 0
  
#exercício 8
def calcula_pontos_full_house (lista):
  dic = {}
  x = 0
  s = 0
  t2 = False
  t3 = False
  for i in lista:
    if i not in dic:
      dic[i] = 1
      x += 1
    else:
      dic[i] += 1
    s += i
  if x != 2:
    return 0
  else:
    for c in lista:
      if dic[c] == 2:
        t2 = True
      elif dic[c] == 3:
        t3 = True
    if t3 and t2:
      return s
    else:
      return 0
    
#exercicio 9
def calcula_pontos_quadra (dados):
  dic = {}
  s = 0
  for i in dados:
    if i in dic:
      dic[i] += 1
    else:
      dic[i] = 1
    s += i
  for n, qtd in dic.items():
    if qtd >= 4:
      return s
  return 0

#exercicio 10
def calcula_pontos_quina (dados):
  dic ={}
  for i in dados:
    if i in dic:
      dic[i] += 1
    else:
      dic[i] = 1
  for n, qtd in dic.items():
    if qtd >= 5:
      return 50
  return 0

#exercicio 11
def calcula_pontos_regra_avancada (lista):
  dic = {}
  dic['cinco_iguais'] = calcula_pontos_quina(lista)
  dic['full_house'] = calcula_pontos_full_house(lista)
  dic['quadra'] = calcula_pontos_quadra(lista)
  dic['sem_combinacao'] = calcula_pontos_soma(lista)
  dic['sequencia_alta'] = calcula_pontos_sequencia_alta(lista)
  dic['sequencia_baixa'] = calcula_pontos_sequencia_baixa(lista)
  return dic
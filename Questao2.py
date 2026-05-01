#exercicio 2
def guardar_dados(rolados, estoque, guardar):
    lista = []
    rol = []
    i = guardar
    estoque.append(rolados[i])
    for d in range(len(rolados)):
        if d!=i:
            rol.append(rolados[d])
    lista.append(rol)
    lista.append(estoque)
    return lista
    
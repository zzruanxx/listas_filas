lista = [1, 2, 3, 4, 5]

lista.append(6)
lista.insert(2, 99)

print(f"Lista apos inserçoes: {lista}")

lista.remove(99)
elemento_removido = lista.pop()

print(f"Lista apos remoçoes: {lista}")
print(f"Elemento removido: {elemento_removido}")


#-------------------------------------------------

fila = deque([1, 2, 3, 4, 5])
fila.append(6)
fila.appendleft(0)

print(f"Fila apos inserçoes: {fila}")

elemento_removido_inicio = fila.popleft()
elemento_removido_fim = fila.pop()

print(f"Fila apos remoçoes: {fila}")
print(f"Elemento removido do inicio: {elemento_removido_inicio}")
print(f"Elemento removido fim: {elemento_removido_fim}")


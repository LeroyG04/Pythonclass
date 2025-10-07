# class #primero vamos al final
# current = head
# while current:
#     current.next

# while current:
#     print(current.dato, end= " <- ")
#     current = current.prev
# print("none")NodoDoble:
#     def __init__(self, dato):
#         self.dato = dato
#         self.prev = None
#         self.next = None

# nodo1= NodoDoble(10)
# nodo2= NodoDoble(20)
# nodo3= NodoDoble(30)

# nodo1.next = nodo2
# nodo2.prev = nodo1
# nodo2.next = nodo3
# nodo3.prev = nodo2

# head = nodo1
# current = head
# while current:
#     print(current.dato, end= " ->")
#     current = current.next
# print("None")

class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.prev = None  # Apunta al nodo anterior
        self.next = None  # Apunta al siguiente nodo
# Crear nodos
nodo1 = NodoDoble(10)
nodo2 = NodoDoble(20)
nodo3 = NodoDoble(30)

# Conectar nodos
nodo1.next = nodo2
nodo2.prev = nodo1
nodo2.next = nodo3
nodo3.prev = nodo2

# Cabeza de la lista
head = nodo1
current = head
while current:
    print(current.dato, end=" -> ")
    current = current.next
print("None")

# Primero vamos al final
current = head
while current.next:
    current = current.next

# Recorrer hacia atrás
while current:
    print(current.dato, end=" <- ")
    current = current.prev
print("None")
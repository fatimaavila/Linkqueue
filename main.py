# Fátima Avila // 20200406
# Linked List implementation
from linked_list import LinkedList, Node
#from stack import Stack
from queue import Queue


lista = LinkedList()
lista2 = Queue()

nodo_a = Node("amarillo")
nodo_b = Node("blue")
nodo_c = Node("cafe")
nodo_d = Node("descansar")
nodo_e = Node("enero")


lista.head = nodo_a
nodo_a.next = nodo_b
nodo_b.next = nodo_c


print("LINK QUEUE •ᴗ•\n")
print("\u001b[33m Ingrese el nombre del link que quiere guardar.\n Luego ingrese el link para que este aparezca en la queue.\u001b[0m\n")

print("Utilice las letras \n -e- para ingresar a la cola \n -d- para sacar de la cola\n -x- para salir.")


 
#print(nombre + "Lista")
#nodoq= str(input())

while True:
  comando = input()
  if comando == '':
    break
  split = comando.split()
  if split[0] == "x" :
    break
  
'''
lista2.enqueue(Node(link, nombre))
print('\u001b[33m enqueue d:\n\u001b[0m', lista2)
lista2.enqueue(nodo_b)
print('\u001b[33m enqueue b:\n\u001b[0m', lista2)
lista2.enqueue(nodo_c)
print('\u001b[33m enqueue c:\n\u001b[0m', lista2)
lista2.dequeue()
print('\u001b[32m dequeue: \n\u001b[0m', lista2)
lista2.enqueue(nodo_a)
print('\u001b[33m enqueue a: \n\u001b[0m', lista2)
lista2.dequeue()
print('\u001b[32m dequeue: \n\u001b[0m', lista2)
#print('dequeue a:\n', lista2)
'''

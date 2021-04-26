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


print("\u001b[36m LINK QUEUE •ᴗ•\n\u001b[0m")
print(" Ingrese el nombre del link que quiere guardar.\n Luego ingrese el link para que este aparezca en la queue.\n ")

print("Utilice las letras \n \u001b[32m-e-\u001b[0m para ingresar a la cola \n \u001b[32m-d-\u001b[0m para sacar de la cola\n \u001b[32m-l-\u001b[0m para mostrar la cola \n \u001b[31m-x-\u001b[0m para salir\n")

print ("\u001b[31m EJEMPLO:\u001b[0m \u001b[32me\u001b[0m https://twitter.com/home \u001b[36mtwit\u001b[0m ")


 
#print(nombre + "Lista")
#nodoq= str(input())

while True:
  comando = input()
  if comando == '':
    break
  split = comando.split()
  if split[0] == "x" :
    break
  if split[0]== "e" :
    lista2.enqueue(Node(split[1], split[2]))
  if split[0]== "d":
    lista2.dequeue()
  if split[0]=="l":
    print(lista2)

    
  
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

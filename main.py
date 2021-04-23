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

print("Linked List\n")
print(lista)
lista.reverse()
print(lista)
print("-------------------------")


print("LINK QUEUE\n")
int(input())
lista2.enqueue(nodo_d)
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


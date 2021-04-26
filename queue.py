from linked_list import LinkedList,Node


class Queue(LinkedList,Node):
  
  def __repr__(self):
    node = self.head
    nodes = []
    while node is not None:
      nodes.append("\u001b[36m"+node.data.split("|")[1]+"\u001b[0m"+"\n"+node.data.split("|")[0]+"\n----\n")
      node = node.next
    nodes.append("----")
    return "".join(nodes)

  def enqueue(self, node):
    if self.head == None:
      #print("lista vacía en queue")
      self.insert_last(node)
    else:
      ##recorrer lista para buscar el ultimo
      node2 = self.head
      data_ultimo=self.head
      while node2 is not None:
        data_ultimo=node2
        node2 = node2.next
      self.insert_after(data_ultimo.data,node)
     

  def dequeue(self):
    node = self.head
    self.remove(node.data)
class Node:
  def __init__(self,data):
    self.next=none
    self.data=data
class LinkedList:
  def __init__(self):
    self.head=none
  def insert(self,data):
    newnode=node(data)
    if(not self.head):
      newnode=self.head
    else:
      temp=self.head
      while temp.next:
        

l=LinlkedList()
l.insert(100)
l.insert(200)
l.insert(300)
l.insert(400)
l.display()

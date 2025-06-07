class Node:
  def __init__(self,data):
    self.next=None
    self.data=data
class LinkedList:
  def __init__(self):
    self.head=None
  def insert(self,data):
    newnode=Node(data)
    if(not self.head):
      self.head=newnode
    else:
      temp=self.head
      while temp.next:
        temp=temp.next
      temp.next=newnode
  def display(self):
      temp=self.head
      while (temp):
        print(temp.data,end="-> ")
        temp=temp.next
      print("NULL")

l=LinkedList()
l.insert(100)
l.insert(200)
l.insert(300)
l.insert(400)
l.display()

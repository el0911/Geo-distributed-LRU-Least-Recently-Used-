#Doubly linked list for helping me store items in ram

from node import Node
import datetime
import calendar


def addTime( months):
    sourcedate = datetime.datetime.now()
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year,month)[1])
    return datetime.date(year, month, day)




class DlinkedList:

  def __init__(self):
    self.first = None
    self.last =  None
    
  #append data to memory and also assigns it to the most recently set and gives it an expiration of 20 months
  def append(self,data):
    #data sample {value} 
    newNode = Node({"data":data,'exp':addTime(1).strftime("%m/%d/%Y, %H:%M:%S")})#expires in a month
    #add it to the first guy
    if self.first is None:
      self.first = newNode
      self.last = newNode
    else:
      temp = self.first
      temp.prev = newNode
      newNode.next = temp
      self.first = newNode
    return newNode
  
  #get items from memory and first check if its expired or not if not expired it returns it and put it on top else it isnt returned
  def get(self,Node):
    exp = Node.value[0]['exp']
      if(datetime.datetime.strptime(exp, "%m/%d/%Y, %H:%M:%S")<datetime.datetime.now()):
        return False
    #so am meant to get the node delete it and put it in the front
    prev = Node.prev
    next_ = Node.next

    if self.last is Node:
      #replace the last with Node.prev
      self.last = prev
    #replaced this node with the next node
    prev.next = next_
    Node.prev = None

    temp = self.first
    Node.next = temp
    self.first = Node

    
    #check for exp and if its expired am not gonna return it because obviously its expired and now its not in the linked list anymore
     
   
    return Node.value
  
  #just to print all items in the cache
  def printAll(self):
    node = self.first
    while node is not None:
      print(node.value)
      node = node.next

  #remove the last item in the list if it exceeds the size
  def removeLast(self):
    node = self.last
    temp = node.prev
    temp.prev =  None
    self.last  =  temp
 

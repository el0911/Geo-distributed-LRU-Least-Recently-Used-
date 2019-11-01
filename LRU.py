#LRU to to cache items into memory

import json
from DdinkedList import DlinkedList
from filehandler import fileHandler
class LRU:
  def __init__(self,MAX):
    self.MAX = MAX
    self.lookup = dict()
    self.dlinked = DlinkedList()
    self.count = 0
    self.backup = fileHandler('backupfile')
    self.getAndLoadBackups()
    
    
  #function loads backedup comands stored in ROM
  def getAndLoadBackups(self):
    backups = self.backup.read()
    for backup in backups:
      command  = json.loads(backup)
      if str(command['type']) == 'add':
        ##add an item to the LRU
        self.add( command['key'], command['value'],dontAdd = True)

  #Load previous stored commands into RAM and also new inputs to the LRU
  def add(self,key,value,dontAdd):
    if dontAdd is not True:
      self.backup.write({"type":"add","key":key,"value":value})
    node = self.dlinked.append(value)
    self.lookup[key] = node
    self.count=+1
    if self.count is self.MAX:
      #delete if we get higher than what we need
      self.dlinked.removeLast()
    pass

#file handler class for managind files

import json
     
class fileHandler:
  #this class is to handle system crashes, commands are stored on the system ROM and and the  LRU is reconstructed on server restart
  def __init__(self,fileName):
    self.fileName = fileName
    

  def write(self,command):
    #sample command {'type':'add',"value":value}]
    file = self.fileWrite = open(self.fileName+".txt","a+")
    file.write(json.dumps(command)+'\n')#
    file.close()

  def read(self):
    file = self.fileRead = open(self.fileName+".txt","r")
    return file.readlines()
    file.close()
    

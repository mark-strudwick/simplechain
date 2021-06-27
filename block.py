from datetime import datetime
import hashlib

class Block:
  def __init__(self, index, data, previousHash):
    self.index = index
    self.data = data
    self.previousHash = previousHash
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    self.timeStamp = now
    self.hash = self.calculateHash()

  def calculateHash(self):
    indexString = str(self.index)
    return hashlib.sha256((indexString + self.data + self.previousHash + self.timeStamp).encode()).hexdigest() 

  def getBlock(self):
    return (self.index, self.data, self.previousHash, self.timeStamp, self.hash)

  def printBlock(self):
    print(self.index, self.data, self.previousHash, self.timeStamp, self.hash)
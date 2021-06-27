from block import Block

class Chain:
  def __init__(self):
    self.chain = []
    self.createStartingBlock()

  def createStartingBlock(self):
    self.chain.append(Block(index = 0, data = "Starting block", previousHash = "0"))

  def getLatestBlock(self):
    return self.chain[len(self.chain) - 1]

  def addBlock(self, data):
    previousBlock = self.getLatestBlock()
    newIndex = previousBlock.index + 1
    previousHash = previousBlock.hash
    b = Block(index = newIndex, data = data, previousHash = previousHash)
    self.chain.append(b)
    
  def isChainValid(self):
    for i in range(1, len(self.chain)):
      currentBlock = self.chain[i]
      previousBlock = self.chain[i - 1]

      if currentBlock.hash != currentBlock.calculateHash():
        return False

      if currentBlock.previousHash != previousBlock.hash:
        return False

      return True
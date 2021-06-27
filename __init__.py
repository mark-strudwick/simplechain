from block import Block
from chain import Chain

c = Chain()
c.addBlock("This is some test data")
print("Is the chain valid?", c.isChainValid())

for i in range(len(c.chain)):
  print(c.chain[i].printBlock())
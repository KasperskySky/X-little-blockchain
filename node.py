from core.bodyfunc import *

def Node(blockchain,method,admin,act,sum):
    blockchain = Initialization(method,admin, act,sum)
    if blockchain:
        return blockchain

Node1 = Node("Node1", "classic", "admin", "create", 0)
Node2 = Node("Node2", "my 123456", "admin", "create", 1)
Node3 = Node("Node3", "limit 999333222111", "Tim", "create", 2)

def Transfer(node, sender,amount,transferee):
    CreateBlockInChain(node, sender, "send", amount)
    CreateBlockInChain(node, transferee, "get", amount)

    return 0
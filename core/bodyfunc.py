from core.body import *

def Creation(hash,name,act,num): # создать блокчейн (2, после инициализации)
	block_og = block(hash, name, act, num)
	return block_og

def Generate(hash): #создать хеш
	hash = hash.split(" ")
	if hash[0] == "classic":
		result = "000a13de59b75045bba5466fa6aa1862ad0370e722537ff17c753ee8250a0e1b"
	elif hash[0] == "limit":
		_hash = hash[1]
		result = _hash
	elif hash[0] == "my":
		result = hash[1]

	return result

def Initialization(hash, name, act, num): #инициализировать блокчейн (1)
	init_block = Creation(Generate(str(hash)),name,act,num)
	
	return init_block

def Read(init_block): # прочитать блокчейн
	read_block = init_block.info_blocks()
	return read_block

def CreateBlockInChain(blockchain,name,act,sum): # создает блок в блокчейне
	blockchain.append(name,act,sum)
	
	return blockchain

def ReadBlockById(blockchain, id):
	blockchain.info_block(id)

	return 0

def ReadBlockByName(blockchain,name):
	blockchain.info_block_by_name("name", name)

	return 0

def BalanceByName(blockchain,name):
	blockchain.info_balance_by_name("name", name)

	return 0
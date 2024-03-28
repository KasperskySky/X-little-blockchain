import datetime
import hashlib
import time
from binascii import unhexlify, hexlify

class block:

	def __init__(self,last_hash,name,act,sum):

		self.next = None
		self.__data = {
			"last_hash": last_hash,
			"name": name,
			"act": act,
			"amount": sum,
			"hash": "",
			"time": datetime.datetime.now().time()
		}

		self.__data["hash"] = self.init_hash() # обращается к функции, что создает хеш

	def get_data(self):
		return self.__data # получить блок по data 

	def init_hash(self): # создает хеш
		start = time.time()

		add_hash = hexlify(hashlib.sha256((unhexlify(self.get_data()["last_hash"]))).digest()).decode("utf-8")
		while add_hash[:3] != "000":
			add_hash = hexlify(hashlib.sha256(unhexlify(add_hash)).digest()).decode("utf-8")
		
		finish = time.time() - start
		print("The time it took for the hash to be created: "+str(finish)) # показывает время, за которое хеш создастся

		return add_hash 

	def append(self, name, act, sum): #создает новый блок
		n = self
		while n.next:
			n = n.next
		last_hash = n.get_data()["hash"]
		end = block(last_hash,name,act,sum)
		n.next = end

	def info_blocks(block): # считывает структуру блокчейна
		node = block
		print(node.get_data()) 
		while node.next:
			node = node.next
			print(node.get_data())

		return 0
	
	def info_block_by_name(block,id,name):
		node = block
		if (node.get_data()[id]) == name:
			print(node.get_data())
		while node.next:
			node = node.next
			if (node.get_data()[id]) == name:
				print(node.get_data())

		return 0
	
	def info_balance_by_name(block,id,name):
		balance = 0
		node = block
		if (node.get_data()[id]) == name:
			print(node.get_data())
		while node.next:
			node = node.next
			if (node.get_data()[id]) == name:
				if (node.get_data()['act']) == 'get':
					balance += (node.get_data()['amount'])
				elif (node.get_data()['act']) == 'send':
					balance -= (node.get_data()['amount'])
				print((str(node.get_data()["name"])) + " "+ str(balance))

		return 0
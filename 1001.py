from node import Node1, Transfer, BalanceByName, ReadBlockByName
from wallets import Tim, Alex, Admin

if __name__ == '__main__':

    Transfer(Node1, Admin, 10000, Tim)
    BalanceByName(Node1, Tim)

    Transfer(Node1, Tim, 1000, Alex)
    BalanceByName(Node1, Tim)

    ReadBlockByName(Node1, Alex)

input()
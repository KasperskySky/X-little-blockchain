from node import Node2, Transfer, BalanceByName, ReadBlockByName
from wallets import Tim, Alex, Admin

if __name__ == '__main__':

    Transfer(Node2, Admin, 10000, Tim)
    BalanceByName(Node2, Tim)

    Transfer(Node2, Tim, 1000, Alex)
    BalanceByName(Node2, Tim)

    ReadBlockByName(Node2, Alex)

input()
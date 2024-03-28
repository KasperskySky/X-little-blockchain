from node import Node3, Transfer, BalanceByName, ReadBlockByName
from wallets import Tim, Alex, Admin

if __name__ == '__main__':

    Transfer(Node3, Admin, 10000, Tim)
    BalanceByName(Node3, Tim)

    Transfer(Node3, Tim, 1000, Alex)
    BalanceByName(Node3, Tim)

    ReadBlockByName(Node3, Alex)

input()
# class Hash:
#     def __init__(self,size):
#         self.size = size
#         self.hash_table = [None] * self.size

#     def addVal(self,val):
#         hashFn = val % self.size
#         if self.hash_table[hashFn] is None:
#             self.hash_table[hashFn] = val
#         else:
#             # Linear Probing
#             for i in range(0,self.size):
#                 linear = hashFn + i
#                 if self.hash_table[linear] is None:
#                     self.hash_table.insert(linear,val)
#                     break

#     def showHashTable(self):
#         print(self.hash_table)

class Hash:
    def __init__(self,size):
        self.size = size
        self.hash_table = [None] * self.size

    def addVal(self,val):
        hashFn = val % self.size
        if self.hash_table[hashFn] is None:
            self.hash_table[hashFn] = val
        else:
            # Quadratic Probing
            for i in range(0,self.size):
                linear = (hashFn + i*i) % self.size
                if self.hash_table[linear] is None:
                    self.hash_table[linear] = val
                    break

    def showHashTable(self):
        print(self.hash_table)

hashtable = Hash(10)
hashtable.addVal(4)
hashtable.addVal(44)
hashtable.addVal(10)
hashtable.addVal(53)
hashtable.addVal(54)
hashtable.showHashTable()
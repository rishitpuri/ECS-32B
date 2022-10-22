hashTable = [[],] * 11

def hashFunction(key):
    capacity = getPrime(11)
    return key % capacity

def insertData(key, data):
    index = hashFunction(key)
    hashTable[index] = [key, data]


insertData(123, "apple")
print(hashTable)
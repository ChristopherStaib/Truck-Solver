class HashTable(object):
    """
    ***REQUIREMENT D***
    Custom Hashtable to take in tuples input and generate HashTable.
    No collision handling needed as length of input will always be given.
    """
    def __init__(self, array):
        self.array = array

    # generates hash
    def hash(self, key):
        length = len(self.array)
        return hash(key) % length

    # adds to hash table
    def add(self, key, value):
        index = self.hash(key)
        if self.array[index] is not None:
            for kvp in self.array[index]:
                if kvp[0] == key:
                    kvp[1] = value
                    break
                else:
                    self.array[index].append((key, value))
        else:
            self.array[index] = (key, value)

    # gets package object from hash table based on key given
    def get(self, key):
        index = self.hash(key)
        if self.array[index] is None:
            raise KeyError
        else:
            for kvp in self.array:
                if kvp[0] == key:
                    return kvp[1]
        print("Key to get not found")

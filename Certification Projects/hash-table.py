"""
In this lab, you will build a hash table from scratch.
A hash table is a data structure that stores key-value pairs. A hash table works by taking the key as an input and then hashing this key according to a specific hashing function.

For the purpose of this lab, the hashing function will be simple: it will sum the Unicode values of each character in the key.
The hash value will then be used as the actual key to store the associated value.
The same hash value would also be used to retrieve and delete the value associated with the key.
"""


class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, text):
        result = 0
        for letter in text:
            result += ord(letter)
        return result

    def add(self, key, value):
        hashed_key = self.hash(key)
        item = {key: value}
        if hashed_key in self.collection:
            print("exist")
            self.collection[hashed_key].update(item)
        else:
            print("not exist")
            self.collection[hashed_key] = dict(item)

    def remove(self, key):
        hashed_key = self.hash(key)
        if hashed_key in self.collection:
            if key in self.collection[hashed_key]:
                removed_value = self.collection[hashed_key].pop(key)
                print("valeur supprimé", removed_value)

    def lookup(self, key):
        hashed_key = self.hash(key)
        if hashed_key not in self.collection or key not in self.collection[hashed_key]:
            return None
        return self.collection[hashed_key][key]

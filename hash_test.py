from hash import HashTable
from words import words

class HashTests:

    def __init__(self, table):
        self.table = table

    def test_hash_number(self, table):

        for word in words:
            word_val = 0
            for letter in word:
                word_val += ord(letter)

        pass

        
            
this_table = HashTable()       #create a new hash table
this_table.add_to_table(words) # fill hash table


HashTests()
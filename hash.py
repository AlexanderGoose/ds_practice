from words import words

class HashTable:

    def __init__(self, table_len = 17):
        self.TABLE_LEN = table_len
        self.table = self.create_table()

    def create_table(self):

        table = {}
        for i in range(self.TABLE_LEN):
            table[i] = []
        return table

    def hash_that(self, word):

        curr_val = 0
        for letter in word:
            curr_val += ord(letter)

        return curr_val % self.TABLE_LEN
    
    def add_to_table(self, word):
        pos = self.hash_that(word)
        (self.table[pos]).append(word)

    def remove_from_table(word):
        pass

    def print_table(self):
        for i in range(self.TABLE_LEN):
            print(f'{i} : {self.table[i]}\n')


if __name__ == "__main__":
    ht = HashTable()

    for i in words:
        ht.add_to_table(i)

    ht.print_table()

class Counter: # class Something -> your own data type named Something
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration

        self.current += 1
        return self.current
    

my_counter1 = Counter(5)

for number in my_counter1:
    print(number)
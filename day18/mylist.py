

class MyList(list):
    def insert_head(self, element):
        self.insert(0, element)


myl = MyList(range(3, 6))
print(myl)    # [3, 4, 5]
myl.insert_head(2)
print(myl)    # [2, 3, 4, 5]



class te1():
    def one(self):
        self.a="111"
        return self
    def two(self):
        b=self.a
        return self.a


print(te1().one().two())



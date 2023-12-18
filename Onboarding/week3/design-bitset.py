class Bitset:

    def __init__(self, size: int):
        self.bit = [0] * size
        self.reverse = [1] * size
        self.num_of_one = 0
        self.num_of_zero = 0
        self.size = size

    def fix(self, idx: int) -> None:
        if self.bit[idx] == 0:
            self.bit[idx] = 1
            self.reverse[idx] = 0
            self.num_of_one+=1
            self.num_of_zero+=1
       
        

    def unfix(self, idx: int) -> None:
        if self.bit[idx] == 1:
            self.bit[idx] = 0
            self.reverse[idx] = 1
            self.num_of_one-=1
            self.num_of_zero-=1
        
        

    def flip(self) -> None:
        
        temp = self.bit
        self.bit = self.reverse
        self.reverse = temp

        
        self.num_of_one = self.size - self.num_of_one
        self.num_of_zero = self.size - self.num_of_zero

        
        

    def all(self) -> bool:
        return self.num_of_one == self.size
        

    def one(self) -> bool:
        return self.num_of_one > 0

        

    def count(self) -> int:
        
        return self.num_of_one
        

    def toString(self) -> str:
        tmp = [str(i) for i in self.bit]
        return "".join(tmp)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()
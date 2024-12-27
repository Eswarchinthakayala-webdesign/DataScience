
class remoteControl:
    def __init__(self):
        self.chanels=["CN","HBO","Star Sports","Hungama"]
        self.index=-1
    def __iter__(self):
        return self
    def __next__(self):
        self.index+=1
        if(self.index)==len(self.chanels):
            raise StopIteration
        return self.chanels[self.index]
r=remoteControl()
iter=iter(r)
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))

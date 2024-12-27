class Bucket:
    def __init__(self,type):
        self.type=type
    
    def usage(self):
        print(f"It is a {self.type}")
class milkBucket(Bucket):
    def usage(self): #overiding the usage()
        print(f"It is a {self.type}")

bucket=Bucket("Noraml Bucket")

mb=milkBucket("Milk Bucket")
mb.usage()

class car:
    def __init__(self,name,model):
        self.name=name
        self.model=model
    def display(self):
        print(f"Car Name: {self.name}, model: {self.model}")
    def drive(self):
        if self.model=="Amaze":
            print("It is good for driving")
        else:
            print("It is somewhat better to use")

car1=car("Honda","Amaze")
car1.display()
car1.drive()

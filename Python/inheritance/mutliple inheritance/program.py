class shop1:
    def things(self):
        print("Bought coconut oil(shop1)")
class shop2:
    def news(self):
        print("Bought newsPaper(shop2)")
class shop3:
    def chicken(self):
        print("Bought chicken(shop3)")
class Person(shop1,shop2,shop3):
    def __init__(self,name):
        self.name=name
    def info(self):
        print(f"I'm {self.name}")


person=Person("Eswar")
person.info()
person.chicken()
person.news()
person.things()

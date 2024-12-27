

class Accident(Exception):
    def __init__(self,msg):
        self.msg=msg
    def handle(self):
        print("Accident will occur . Take detour")

try:
    raise Accident("crash between two cars")
except Accident as e:
    e.handle()

class person:
    def __init__(self, name):
            self.name=name
        
    def talk(self):
        print(f"hi my name is {self.name}")
        
       
name = person('john Kangu')
name.talk()


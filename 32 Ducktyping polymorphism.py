class ide:
    def execute(self):
        print("Compile")
        print("Run")

class myide:
    def execute(self):
        print("Spell Check")
        print("Error Check")
        print("Complie")
        print("Run")

class Laptop:
    def code(self, ide):
        ide.execute()

a = ide()
b = myide()
lap = Laptop()
lap.code(b)

from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Programmer:
    def work(self, other):
        print("Solving Bugs")
        other.compile()

class IDE(Computer):
    def compile(self):
        print("Compile Done")

    def process(self):
        print("This is Process")

# com1 = Computer()
# com1.process()

prog1 = Programmer()
a1 = IDE()
prog1.work(a1)

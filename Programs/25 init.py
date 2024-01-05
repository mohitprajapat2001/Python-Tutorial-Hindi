class Computer:
    def __init__(self, processor, ram):
        self.processor = processor
        self.ram = ram

    def info(self):
        print("Processor", self.processor, "RAM ", self.ram)


com1 = Computer("i5 11", 16)
com2 = Computer("Rysen 5", 8)
com1.info()
com2.info()

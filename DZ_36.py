class Student:
    def __init__(self):
        self.name_ = 'Roman'
        self.model_ = "HP, "
        self.prosessor_ = "i7, "
        self.memori_ = "16"

        self.Computer = self.Computer()

    def show(self):
        print(self.name_,' => ', self.model_, self.prosessor_, self.memori_)


    class Computer:
        def __init__(self):
            self.name = "Vladimir"
            self.model = "HP,"
            self.prosessor = "i7,"
            self.memori = "16"

        def display(self):
            print(self.name,' => ', self.model, self.prosessor, self.memori)



outer = Student()
outer.show()
d1 = outer.Computer
d1.display()




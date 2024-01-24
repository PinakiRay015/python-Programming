# Python program to create a method instance
class Mammals:
    def birth(self , name):
        print("{name} give birth to young ones".format(name = name))


Tiger = Mammals()
Tiger.birth("Dogs")
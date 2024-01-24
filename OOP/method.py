# Python program to create a method instances
class Mammals:
    def birth(self , name):
        print("{name} give birth to young ones".format(name = name))


Tiger = Mammals()
Tiger.birth("Dogs")
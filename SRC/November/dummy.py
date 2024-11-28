class car():
    def __init__(self,name):
        self.name= name
        print("Name of the car is", name)

    def color(self):
        print("the color is black")
    def speed(self):
        print("the speed is more than 200")

obj1=car("bugatti")
obj1.color()
obj1.speed()
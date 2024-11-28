class Dog:
    # A
    name = None
    age = None
    color = None
    breed = None

    def __int__(self,name):
        self.name=name
        print(name)
    def sleep(self):
        print('Sleeping')


dog1 = Dog()
print(dog1.name)
dog1.name="chow"
print(dog1.name)
dog1.sleep()
class Animal():
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print('bark')

class Cat(Animal):
    def speak(self):
        print('meow')

mydog = Dog()
mydog.speak()

mycat = Cat()
mycat.speak()
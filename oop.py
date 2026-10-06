### OOP
### A PIE 
## Abstraction, Polymorphism, Inheritance, Encapsulation

# - people in the tech/software industry might have different interpretation of these principles

# ABSTRACTION is the ultimate goal of the OOP principles

# Abstraction & Encapsulation

# Inheritance & Polymorphism

# Abstraction
# no need to know ALL details to use it

class Phone():
    def unlock(self):
        self.turn_on_screen()
        self.take_lock_button_input()
        self.face_scan_check()
        #...

    def __turn_on_screen(self):
        # get the screen to turn on
        # ...
        pass

    def __take_lock_button_input(self):
        # ...
        pass

    def __face_scan_check(self):
        # ...
        pass

# Encapsulation
# The ability to protect our classes and functions internals
# from misuse or malice

class Phone():
    def __init__(self, colour, memory, storage):
        self.__colour = colour
        self.__memory = memory
        self.__storage = storage
        self.__apps_installed = []
        self.__available_memory = self.memory
    
    # def open_app(self, app, memory):
    #     self.available_memory -= memory
    #     self.__launch(app)

    def open_app(self, app):
        self.__available_memory -= self.__available_memory / 10
        self.__launch(app)
    
    def install_app(self, app):
        self.__apps_installed.append(app)
    
    def get_apps_installed(self):
        return self.__apps_installed
    
    def get_colour(self):
        return self.__colour
    
    def get_storage(self):
        return self.__storage
    
    def add_storage(self, storage):
        if not isinstance(storage, int):
            raise TypeError('only integers for storage')
        pass

# phone = Phone('blue', 10, 250)

# Inheritance
# Taking attributes and methods from a parent. - Nobel

class Person():
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        return "Hi, how are you?"

    def walk(self):
        return "Walking"

class EnglishPerson(Person):
    def eat_breakfast(self):
        return 'I love a Full English!'
    
    def queue_up(self):
        return "Queing"

class AmericanPerson(Person):
    def brunch(self):
        return 'Pancakes with maple syrup and bacon!'
    
    def phone_services(self):
        return "Phoning"

# Polymorphism
# 

class Person():
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        return "Hi, how are you?"

    def walk(self):
        return "Walking"
    
class GermanPerson(Person): 
    def say_hi(self): # polymorphic
        return "Hallo, Guten Tag!"

class EnglishPerson(Person):
    def eat_breakfast(self):
        return 'I love a Full English!'
    
    def queue_up(self):
        return "Queing"

class AmericanPerson(Person):
    def brunch(self):
        return 'Pancakes with maple syrup and bacon!'
    
    def phone_services(self):
        return "Phoning"

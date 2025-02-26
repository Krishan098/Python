#dir()- inspects the object
#dunder- double underscore methods
#Method- When a function is a part of an object or a class, it is called method.
#Object- Collection of data(variables) and methods that operate on the data.Defined by a python class
#Class- Blueprint of one or more objects
# class Car:
#     def __init__(self,started=False,speed=0):
#         self.speed=speed
#         self.started=started
    
#     def start(self):
#         self.started=True
#         print("Car started, let's ride!")
#     def increase_speed(self,delta):
#         if self.started:
#             self.speed+=delta
#             print("Vrooooooom!")
#         else:
#             print("Start the car first")
#     def stop(self):
#         self.speed=0
#         print('Stopped')
# car=Car()

# car.start()
# car.increase_speed(10)
# car.increase_speed(40)
#car.stop()
#Self is a reference to the object itself, can be used to reference other instance variables amd functions of this objct
# print(id(car))
# print(car.speed)
#Constructor: called automatically when an object is created
class Vehicle:
    def __init__(self,started=False,speed=0):
        self.started=started
        self.speed=speed
    def start(self):
        self.started=True
        print("Started, let's ride!")
    def stop(self):
        self.speed=0
    def increase_speed(self,delta):
        if self.started:
            self.started+=delta
        else:
            print("Start first")
class Car(Vehicle):
    def __init__(self, trunk_open=False):
        self.trunk_open=trunk_open
        super().__init__()
    def open_trunk(self):
        self.trunk_open=True
        print("opened")
    def close_trunk(self):
        self.trunk_open=False
        print("Closed")
class motorCycle(Vehicle):
    def __init__(self,center_stand_out=False):
        self.cenetr_stand_out=center_stand_out
        super().__init__()
car=Car()
car.open_trunk()
car.start()
car.increase_speed(50)
motorcycle=motorCycle()
motorcycle.start()
motorcycle.increase_speed(89)

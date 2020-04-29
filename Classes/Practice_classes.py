'''
Доработка сегодняшнего занятия
Добавьте в класс Батарей метод разряда батареи, который принимает параметр пробега и внутри умножает пробега на расход батареии 
и потом отнимает данные с атрибута батареи
Добавьте метод заряда батарей к 100% значению"

'''

class Cars:
    def __init__(self, age, model, mileage):
        self.age = age
        self.model = model
        self.mileage = mileage

    def description(self):
        desc = str(self.age) + " " + self.model + " " + str(self.mileage)
        return desc.title
    
    def __repr__(self):
        return str(self.age) + " " + self.model + " " + str(self.mileage)
    
    def read_odometer (self, mileage):
        self.mileage += mileage

    def repair(self, cost,man_hours):
        return cost * man_hours


tesla = Cars(1,'S',350)
#print(tesla)

t1 = tesla.description()
#print(t1)


class ElectricCars(Cars):
    def __init__(self, age, model, mileage):
        super().__init__(age,model,mileage) 
        self.battery = Battery()

    def power(self,watts):
       power = watts * 240 
       print('power is amazing ' + str(power))
    
class Battery:
    def _init_(self,battery = 100):
        self.battery = battery
    
    def desc_battery(self):
        print('all good, the battery is made from lithium')
    
    def des_battery(self):
        print('all good, the battery ' + str(self.battery))

    def update_battery(self,percent):
        self.battery = self.battery -percent
        print('Look, the battery decreases ' + str(self.battery))


mazda = ElectricCars(25,'6',45)
        
mazda.power(23)
mazda.battery.desc_battery()
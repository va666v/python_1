class CarsClass():
    '''Класс автомобилей'''

    def __init__(self, brand, model, year, probeg):
        self.brand = brand
        self.model = model
        self.year = year
        self.probeg = probeg

    def showCar(self):
        print(f'{self.brand}, {self.model},  '
              f'{self.year} год, {self.probeg} km')

    def drowCar(self, km):
        self.probeg = self.probeg + km

class Battery():
    def __init__(self, battery = 100):
        self.battery = battery

    def descriptionBattery(self):
        print(f"This car has battery: {self.battery}%")

class ElectroCar(CarsClass):
    '''Klass elekrtomobil'''
    def __init__(self, brand, model, year, probeg):
        super().__init__(brand, model, year, probeg)
        self.battery = Battery()

# s_car = CarsClass('Lada', 'Granta', '2020', '10')
# s_car.showCar()
#
# tesla = ElectroCar('Tesla', 'T', '2017', '10000')
# tesla.showCar()
# tesla.battery.descriptionBattery()
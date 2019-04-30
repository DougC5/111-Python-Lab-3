# Class can contain:
# Attributes
# Constructor
# Methods

class Vehicle(object):
    make = ''
    year = ''
    cylinders = 0
    color = ''
    price = 0.0

    def __init__(self, make, year, cyls, color, price):
        self.make = make
        self.year = year
        self.cylinders = cyls
        self.color = color
        self.price = price

        print('Im the constructor of the vehicle')

    def start_engine(self):
        print('Engine Has Started')

    def stop_engine(self):
        print('Engine Has Stopped')

    def print_vehicle(self):
        print('Vehicle: ')
        print(' Make: ' + self.make)
        print(' Year: ' + str(self.year))
        print(' Cylinders: ' + str(self.cylinders))
        print(' Color: ' + self.color)
        print(' Price: ' + str(self.price) + '\n')

    def year_check(self):
        return str(self.year)
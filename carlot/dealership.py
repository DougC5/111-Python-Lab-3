import pickle

from vehicle import Vehicle
from menu import menu

inventory = []
sold = []

data_file = "inventory.dat"
data_file_sold = 'sold.dat'

def save_data(df, array):
    writer = open(df, "wb")
    pickle.dump(array, writer)
    writer.close()
    print('Data Saved!!')


def load_data(df, array):
    reader = open(df, 'rb')
    temp = pickle.load(reader)
    for auto in temp:
        array.append(auto) #Puts the vehicle back into the array

    print('Loaded from database: ' + str(len(inventory)))


def list_sold_vehicles():
    load_data(data_file_sold, sold)
    total = 0.0
    print('\n')
    print('-' * 15)
    print('List of Sold Vehicles')
    print('-' * 15)

    for auto in sold:
        print(str(auto.year) + ' - ' + auto.make + ': ' + str(auto.price))
        total = total + auto.price

    print('\n')
    print('-' * 15)
    print('Total Sales: ' + str(total))
    print('-' * 15)


def load_stock():
    v1 = Vehicle('Ford', 2005, 6, 'red', 11000)
    inventory.append(v1)

    v2 = Vehicle('Mazda', 2015, 4, 'candy red', 20000)
    inventory.append(v2)

    v3 = Vehicle('Toyota', 2015, 6, 'blue', 18000)
    inventory.append(v3)

    v4 = Vehicle('Tesla', 2019, 4, 'blue', 70000)
    inventory.append(v4)

    save_data(data_file, inventory)

    print('Stock Inventory Loaded')


def create_new():

    try:
        user_make = input('\nMake of vehicle: ')
        user_year = int(input('Year of vehicle: '))
        user_cyls = int(input('Number of cylinders: '))
        user_color = input('Color of vehicle: ')
        user_price = float(input('Price of vehicle: '))

        v = Vehicle(user_make,  user_year, user_cyls, user_color, user_price)
        inventory.append(v)
        save_data(data_file, inventory) #saves the array to the file
        input('\nvehicle added press enter to continue')

    except:
        print('Some of the data is invalid. Please try again')

    
def print_list():
    sel = ''
    i = 1
    print('\n')
    print('-' * 15)
    print('Inventory')
    print('-' * 15)
    for car in inventory:
        print(str(i) + ' - ' + str(car.year) + ' ' + car.make)
        i = i + 1

    try:
        print('-' * 15)
        sel = int(input('Input the number to see details: '))
        print('-' * 15)

        if (sel > 0 and sel <= len(inventory)+1):
            index = sel - 1
            car = inventory[index]
            car.print_vehicle()
            return index
        else:
            print('** Please enter a valid selection')
            return -1
            
    except:
        print('**Error please try again')
        return -1

        
def sell_vehicle():
    sell_ind = print_list()
    car = inventory[sell_ind]
    if sell_ind == -1:
        print("invalid selection, please try again")
        return

    conf = input('Do you want to sell: ' + str(car.year) + ' - ' + car.make + ': [Y/N]?')
    if conf == 'Y' or conf =='y':

        # Add auto to sold list
        sold.append(inventory[sell_ind])
        save_data(data_file_sold, sold)

        # Delete and update inventory
        del inventory[sell_ind]
        print('Successfully removed form the system!!')
        save_data(data_file, inventory)

    elif conf == 'N' or conf =='n':
        print('returning to main menu')

    else:
        print('**Error please enter "y" or "n"')

            
def count_year():
    check_year = input('Enter the year: ')
    count = 0
    for car in inventory:
        car_year = car.year_check()
        if (car_year == check_year):
            count +=1

    print('\nThere are: ' + str(count) + ' vehicle(s) with that year')
      

load_data(data_file, inventory) #load inventory from file
selection = ''
while (selection != 'x' or selection != 'X'):
    selection = menu()

    if (selection == '1'):
        create_new()
    
    elif (selection == '2'):
        print_list()

    elif (selection == '3'):
        count_year()

    elif (selection == '4'):
         load_stock()

    elif (selection == '5'):
         sell_vehicle()

    elif (selection == '6'):
         list_sold_vehicles()

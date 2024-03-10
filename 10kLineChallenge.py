# # looping through the list
# bikes = ['trek', 'redline', 'giant']
# for bike in bikes:
#     print(bike)

# # making numerical lists
# square =[]
# for x in range(1,11):
#     square.append(x**2)
#     # print(square)
# print(square)

# # list comprehension

# square=[x**2 for x in range(1,11)]
# print(square)

# # making a tuple
# dimensions =(1920,1080)
# #this won't be changed

# # looping through all key value pairs
# fav_numbers={'eric':2,'ever':3}
# for name, number in fav_numbers.items():
#     print(name+' loves '+str(number))

# # while loops
# cur_val =1
# while cur_val<=5:
#     print(cur_val)
#     cur_val+=1

# # letting the user when to quit
# msg = ''
# while msg != 'quit':
#     msg = input('what is your messagee')
#     print(msg)

# # default value in fn
# def make_pizza(toppings='bacon '):
#     print('have a '+ toppings + 'pizza')
# make_pizza()
# make_pizza('pepporoni ')

# # returning values in a function
# def add_numbers(x,y):
#     return x+y
# sum = add_numbers(3,5)
# print(sum)
# print(add_numbers(5,5))

# # class
# class Dog():

#     def __init__(self, name, *args):
#         self.name = name
#         self.owner='kamal'# static value
#     def sit(self):
#         """Simulate sitting."""

#         print(self.name + " is sitting."" his owner name is "+self.owner)
# my_dog = Dog('Peso')#passing arg
# print(my_dog.name + " is a great dog!")
# my_dog.sit()


# inheritance
# class Dog():

#     def __init__(self, name, *args):
#         self.name = name
#         # self.owner='kamal'# static value

#     def sit(self):
#         """Simulate sitting."""

#         print(self.name + " is sitting.")


# my_dog = Dog('Peso')  # passing arg
# print(my_dog.name + " is a great dog!")
# my_dog.sit()


# class SARDog(Dog):
#     def __init__(self, name, *args):
#         super().__init__(name, *args)

#     def search(self):
#         print(self.name + " is searching.")


# my_dog1 = SARDog('willie')
# print(my_dog1.name + " is searching dog.")
# my_dog1.sit()
# my_dog1.search()


# # reading files
# filename= 'sidhartha.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()

# for line in lines:
#     print(line)

# # writing into a file
# filename = 'journal.txt'

# with open(filename, 'w') as file_object:
#     file_object.write('\n i love making games')


# # appending a line

# filename = 'journal.txt'
# with open(filename, 'a') as file_object:
#     file_object.write('\n i love programminig')

# # exception handling
# prompt  = 'how many tickets.\n'
# num_tickets = input(prompt)

# try:
#     num_tickets= int(num_tickets)
# except ValueError:
#     print('try again, giv number input.')
# else:
#     print('your tickets are printing')


# # class in detail
# class Car():
#     """A simple attempt to model a car."""

#     def __init__(self, make, model, year, fuel_capacity=15, fuel_level=0):
#         """Initialize car attributes."""
#         self.make = make
#         self.model = model
#         self.year = year
#         # Fuel capacity and level in gallons. using default arguement.
#         self.fuel_capacity = fuel_capacity
#         self.fuel_level = fuel_level

#     def fill_tank(self):
#         """Fill gas tank to capacity."""
#         self.fuel_level = self.fuel_capacity
#         print("Fuel tank is full.")

#     def drive(self):
#         """Simulate driving."""
#         print("The car is moving.")


# my_car = Car('audi', 'q3', '2023')
# print(my_car.make, my_car.model, my_car.year)
# my_car.fill_tank()
# my_car.drive()
# # multiple objects
# my_old_car = Car('subaru', 'outback', 2013)
# my_truck = Car('toyota', 'tacoma', 2010)
# print(my_old_car.make, my_old_car.model,
#       my_old_car.year, my_old_car.fuel_level)
# print(my_truck.make, my_truck.model, my_truck.year)

# # modify the fuel level

# my_old_car.fuel_level = 10
# print(my_old_car.make, my_old_car.model,
#       my_old_car.year, my_old_car.fuel_level)

# def greet_user():
#     print("hello!")

# greet_user()

# def greet_user(username):
#     print("hello! " + username ,end=' ')


# greet_user("kamal")
# greet_user("pandi")
# greet_user("V")


# def describe_pet(animal, name=None):
#     print('\nI have a ' + animal + '.')
#     if name:
#         print('Its name is ' + name+'.')


# describe_pet('hamster', 'harry')
# describe_pet('snake')


# def get_full_name(first, last):
#     full_name = first + ' '+ last
#     return full_name

# musician = get_full_name('jimi', 'hendrix')
# print(musician)

# def build_person(first, last):
#     person = {'first': first, 'last': last}
#     return person


# musician = build_person('jimi', 'hendrix')
# print(musician)

# def build_person(first, last, age=None):
#     person = {'first': first, 'last': last}
#     if age:
#         person['age'] = age
#     return person


# musician = build_person('jimi', 'hendrix', 27)
# print(musician)

# musician = build_person('kamal','pandi')
# print(musician)

# passing list as argument
# def greet_user(names):
#     for name in names:
#         msg = 'hello, ' + name + '!'
#         print(msg)


# username = ['hannah', 'ty', 'margot']
# greet_user(username)

# def print_models(unprinted, printed):

#     while unprinted:
#         current_model = unprinted.pop()
#         print("printing", current_model)
#         printed.append(current_model)
#         print(printed)


# unprinted = ['phone case', 'pendent', 'ring']
# printed = []

# print_models(unprinted, printed)

# print('\nUnprinted:', unprinted)
# print('printed', printed)

# def print_models(unprinted, printed):

#     while unprinted:
#         current_model = unprinted.pop()
#         print("printing", current_model)
#         printed.append(current_model)
#         # print(printed)


# orignal = ['phone case', 'pendent', 'ring']
# printed = []

# print_models(orignal[:], printed)
# # Here, orignal[:] creates a copy of the orignal list and passes this copy to the print_models function.
# # Therefore, any modifications made to the unprinted list within the print_models function won't affect the original orignal list.
# print('\nOrignal:', orignal)
# print('printed:', printed)

def make_pizza(size, *toppings):
    print('\nMaking a ' + size + 'pizza.')
    print('Toppings:')
    for topping in toppings:
        print('- ' + topping)
 

make_pizza('small ', 'pepparoni')
make_pizza('large ', 'bacon bits', 'pineapple')
make_pizza('medium ', 'mushroom', 'peppers', 'onions', 'extra cheese')

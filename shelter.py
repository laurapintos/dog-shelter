

from sys import exit
import datetime

"""  The following classes are the classes that allow the user to interact with the shelter
"""

class UI(object):
    """ This class is parent class for all user interfaces. It should include all methods necessary
        to valide input from the user interfaces. It will be more useful if I do some refactoring on all
        interfaces.
    """
    # this is the logo that all user interfaces can use if needed
    logo = """

                                 ,:'/   _..._
                                // ( `""-.._.'
                                \| /    6\___
                                |     6      4
                                |            /
                                \_       .--'
                                (_'---'`)
                                / `'---`()
                              ,'        |
              ,            .'`          |
              )\       _.-'             ;
             / |    .'`   _            /
           /` /   .'       '.        , |
          /  /   /           \   ;   | |
          |  \  |            |  .|   | |
           \  `"|           /.-' |   | |
            '-..-\       _.;.._  |   |.;-.
                  \    <`.._  )) |  .;-. ))
                  (__.  `  ))-'  \_    ))'
                      `'--"`  jgs  `""

               """
    def __init__(self):
        pass

    def represents_int(self, s):
        """ Takes a string as argument, returns true if int(s) does not produce Value Error, false otherwise.
        """
        try:
            int(s)
            return True
        except ValueError:
            return False

    def remind_options(self, options):
        """Given a tuple of valid options for the user interface, prints a user friendly error message
           and informs the user which the valid options are
        """
        print("Invalid option! Valid options are: " + " or ".join(options))

    def valid_hour(self, hour):
        """ Returns true if hour is in 0..23, false othersiw
        """
        return hour in range(0, 24)


class Start(UI):
    """ This is the start user interface.
    """

    def __init__(self):
        self.title = "\t\t\tWelcome to Laura's Animal Shelter!"

        self.menu = """
                            +-------------------------------------------+
                            | Please identify who you are: (1-2)        |
                            |                                           |
                            |  (1) Employee or Volunteer                |
                            |  (2) Potential Adopter                    |
                            |  (q) Exit                                 |
                            +-------------------------------------------+
                    """
        self.options = ('1', '2', 'q')

    def display(self):
        """ Displays the welcome user interface to the Shelter.
        """
        print(UI.logo)
        print(self.title)
        print(self.menu)

        while True:
            option = (input("> "))
            if option in self.options:
                break
            else:
                self.remind_options(self.options)
                continue
        if option == '1':
            return "employees"
        if option == '2':
            return "adopters"
        if option == 'q':
            return "exit"


class Employees(UI):
    """ This is the user interface for employees or volunteers.
    """
    def __init__(self):
        self.title = """
                                           Employees Options
                     """
        self.menu = """
                            +-------------------------------------------+
                            | Please select what you want to do:        |
                            |  (1) Intake a dog                         |
                            |  (2) Register the dogs I walked           |
                            |  (3) Walk the dogs                        |
                            |  (4) Show me the shelter status           |
                            |  (q) Exit                                 |
                            +-------------------------------------------+"""
        self.options = ('1', '2', '3','4', 'q')

    def display(self):
        """ Displays the user interface for employees.
        """
        print(self.title)
        print(self.menu)

        while True:
            option = (input("> ").lower())
            if option in self.options:
                break
            else:
                self.remind_options(self.options)
                continue
        if option == '1':
            return "intake"
        if option == '2':
            return "walked"
        if option == '3':
            return "walk"
        if option == '4':
            print(shelter)
            return "employees"
        if option == 'q':
            return 'start'


class Intake(UI):
    """ This is the user interface where employees or volunteers can intake (add) a dog to the shelter.
    """
    def __init__(self):
        self.title = """
                                          Process Intake
                     """
        self.menu = """
                            +-------------------------------------------+
                            | Enter the name, year of birth and breed.  |
                            | Enter the values separated by commas.     |
                            | Example:                                  |
                            | > Charlie, 2016, Chihuahua                |
                            +-------------------------------------------+
                    """
    def display(self):
        """ Displays the user interface.
        """
        print(self.title)
        print(self.menu)

        while True:
            values = input("> ").split(',')
            if len(values) != 3:
                print("Enter name, year of birth and breed.")
                continue
            if self.represents_int(values[1]):
                break
            else:
                print("Enter name, year of birth and breed.  Year has to be an integer.")

        name = values[0]
        year = int(values[1])
        breed = values[2]
        kennel = shelter.next_kennel()
        if not kennel:
            print("We are sorry, we can not process the intake.  The shelter is full!")
        else:
            # add the dog to the shelter
            dog = shelter.add_dog(kennel, name, year, breed)
            print("{} was successfully intaken. He/She is in kennel {}".format(dog.get_name(), kennel))

        return "employees"


class Walk(UI):
    """ User interface where the user can browse which dogs have been waiting longer for a walk
    """
    def __init__(self):
        self.title = """
                                        Every dog needs a walk!
                     """
        self.menu = """
                            +-------------------------------------------+
                            | Please select how many dogs you plan      |
                            | to walk. We suggest that every dog needs  |
                            | at least one walk of 15 minutes a day.    |
                            |                                           |
                            |  (2) I have time to walk two dogs         |
                            |  (3) Three dogs                           |
                            |  (4) Four dogs                            |
                            |  (5) I have time!                         |
                            |  (q) when you are done                    |
                            +-------------------------------------------+"""
        self.options = ('2', '3', '4', '5', 'q')

    def display(self):
        """ Displays the user interface for walking the dogs.
        """
        print(self.title)
        print(self.menu)

        while True:
            option = (input("> ").lower())
            if option in self.options:
                break
            else:
                self.remind_options(self.options)
                continue
        if option == 'q':
            return 'exit'
        print ("We kindly suggest you to walk these dogs, who have been waiting longer for a walk:\n ")
        priority_list = shelter.get_priority_walks(int(option))
        # display the dogs that have priority to be walked
        for dog in priority_list:
            print("{} in kennel {} walked at {} last time.".format(dog.get_name(), dog.get_kennel(),
                   dog.get_last_walk().strftime("%B-%d-%Y %H:%M:%S")))

        print ("\nThank you very much for walking the dogs!\n")
        return "employees"


class Walked(UI):
    """ User interface where the user can register the dogs he/she walked
    """
    def __init__(self):
        self.title = """
                                    Register the dogs you walked today!
                     """
        self.menu = """
                            +---------------------------------------------------+
                            | Enter dog's name and hour separated by ','        |
                            | Hour must be in 0..23                             |
                            | Type 'q' when done.   Examples:                   |
                            | Enter name and hour separated by ',': Leo, 9      |
                            | Enter name and hour separated by ',': Petunia, 15 |
                            | Enter name and hour separated by ',': q           |
                            +---------------------------------------------------+
                    """

    def display(self):
        """ Displays the user interface for walking the dogs.
        """
        print(self.title)
        print(self.menu)

        while True:
            values = input("Enter name and hour separated by ',': ").split(',')
            if values[0] == 'q':
                break
            if len(values) != 2:
                continue
            if not self.represents_int(values[1]):
                print("hour must be in 0..23")
                continue
            if not self.valid_hour(int(values[1])):
                print("hour must be in 0..23")
                continue
            dog = shelter.find_dog(values[0])
            if dog:
                # walk the dog!
                today = datetime.datetime.today()
                dog.walks(datetime.datetime(today.year, today.month, today.day, int(values[1]), 0, 0))
            else:
                print("{} is not in the shelter".format(values[0]))
            # loop to register more dog's walks!
            continue
        print ("\nThank you very much for walking the dogs!\n")
        return "employees"



class Adopters(UI):
    """This is the user interface for potential adopters, where they can browse the dogs in the shelter
    """

    def __init__(self):
        self.title = """
                                    How to look for your next pet
                     """
        self.menu = """
                            +-------------------------------------------+
                            | Please select your option:                |
                            |  (1) I have no preference                 |
                            |  (2) Show me the seniors                  |
                            |  (3) Show me the puppies                  |
                            |  (4) Show me the longest stay dogs first  |
                            |  (q) Exit                                 |
                            +-------------------------------------------+"""
        self.options = {'1', '2', '3', '4', 'q'}

    def display(self):
        """ Displays the user interface for potential adopters to browse for dogs.
        """
        print(self.title)
        print(self.menu)

        while True:
            option = (input("> ").lower())
            if option in self.options:
                break
            else:
                self.remind_options(self.options)
                continue

        if option == 'q':
            return "start"
        elif option == '1':
            print(*[dog for dog in shelter.show_alldogs()], sep = '\n')
        elif option == '2':
            print(*[dog for dog in shelter.show_alldogs() if dog.is_senior()], sep = '\n')
        elif option == '3':
            print(*[dog for dog in shelter.show_alldogs() if dog.is_puppy()], sep = '\n')
        elif option == '4':
            print(*[dog for dog in shelter.get_longest_stay_dogs()], sep = '\n')
        return "adopters"


class Good_Bye(UI):
    """ This is the last user interface.
    """
    def __init__(self):
        self.title = "\t\tThank you for visiting the shelter!"

    def display(self):
        """ Displays the user interface.
        """
        print(UI.logo)
        print(self.title)


class Interface():
    """ This class is the manager of all user interfaces.  This was copied from the material suggested
        from the book "Learn Python the hard way". In that example, this was called the Map class and was used to
        manage the scenes, here it manages the user interfaces.
    """
    #
    uis_dict = {'start': Start(),
                'employees': Employees(),
                'intake': Intake(),
                'walk': Walk(),
                'walked': Walked(),
                'adopters': Adopters(),
                'exit':  Good_Bye(),
               }

    def __init__(self, start_ui):
        self.start_ui = start_ui

    def next_ui(self, ui_name):
        return Interface.uis_dict.get(ui_name)

    def opening_ui(self):
        return self.next_ui(self.start_ui)


class Animal_Shelter():
    """ This is the main class.
    """

    def __init__(self, interface, kennels=0):
        """ The shelter initializer receives as arguments an interface which will manage the transitions
            of the interfaces and the number of kennels
        """
        # initialize the dogs attribute as an empty dictionary, no dogs yet
        self.dogs = {}
        # this attribute is just to generate an id for each new dog that enters the shelter system
        self.id = 0
        self.interface = interface
        # initializes all kennels in the shelter as empty
        self.kennels = [Kennel(i+1, 1) for i in range(kennels)]

    def play(self):
        """ Method that allows the users to interact with the shelter
        """
        current_ui = self.interface.opening_ui()
        last_ui = self.interface.next_ui('exit')
        while current_ui != last_ui:
            next_ui = current_ui.display()
            current_ui = self.interface.next_ui(next_ui)

        # display the last ui
        current_ui.display()

    def show_alldogs(self):
        """ Returns a list containing all dogs at the shelter
        """
        return self.dogs.values()

    def get_longest_stay_dogs(self):
        """ Returns a list with the longest stay dogs at the shelter
        """
        return sorted([dog for dog in self.dogs.values()], key = lambda dog: dog.intake_date)

    def get_priority_walks(self, num):
        """ Returns a list with num of dogs that have been waiting longer for a walk
        """
        return sorted([dog for dog in self.dogs.values()], key = lambda dog: dog.get_last_walk())[:num]

    def next_kennel(self):
        """ Returns the number of the next kennel available
        """
        for kennel in self.kennels:
            if not kennel.is_full():
                return kennel.num
        else:
            return 0

    def add_dog(self, kennel, name, born, breed, day=datetime.datetime.today()):
        """ Adds a dog to the shelter
        """
        dog = Dog(kennel, name, born, breed, day)
        self.dogs[self.id] = dog
        self.id += 1
        self.kennels[kennel-1].add_dog(dog)
        return dog

    def find_dog(self, name):
        """ Given a name, returns the dog with that name
        """
        for dog in self.dogs.values():
            if dog.get_name().lower() == name.lower():
                return dog
        else:
            return None

    def __repr__(self):
        """ User friendly reprentation of the shelter
        """
        return "Shelter Status as of {}\nTotal number of dogs: {}\n{}".format(datetime.datetime.today().strftime("%d-%B-%Y"),
                Dog.dog_count, "\n".join([str(kennel) for kennel in self.kennels]))


class Pet:
    """ Class Pet, not really needed for the scope of this project but it is included because in the future
        the shelter might have the capacity to intake other kinds of pets, like cats or rabbits.
    """

    def __init__(self, name, born=datetime.datetime.today().year, intake_date=datetime.datetime.today()):
        """ Creates a pet with name, year of birth and intake date.
        """
        self.name = name
        self.born = datetime.datetime(born, 1, 1)
        self.intake_date = intake_date


class Dog(Pet):
    """ This is the Dog class.
    """
    # this class attribute will count how many instances of dogs have been created
    dog_count = 0

    def __init__(self, kennel, name, born,
                 breed = "Mix", intake_date=datetime.datetime.today()):
        super().__init__(name, born, intake_date)
        self.breed = breed
        # in the future this should hold dog picture
        self.image = """
                      __      _
                    o'')}____//
                     `_/      )
                     (_(_/-(_/
                     """
        self.kennel = kennel
        self.intake_date = intake_date
        self.last_walk = intake_date
        Dog.dog_count += 1
        

    def walks(self, last_walk_time = datetime.datetime.today()):
        """This method receives last_walk_time as an argument and sets the attribute last_walk.
           The attribute last_walk will be used to define which dogs have priority to walk.
        """
        self.last_walk = last_walk_time

    def get_name(self):
        """ Returns dog's name
        """
        return self.name

    def get_last_walk(self):
        """ Returns the last time the dog walked.
        """
        return self.last_walk

    def get_kennel(self):
        """ Returns the kennel's number assigned to the dog
        """
        return self.kennel

    def is_senior(self):
        """ Returns True if the dog's age is > 7
        """
        return self.age() > 7

    def is_puppy(self):
        """ Returns True if the dog's age is <= 1
        """
        return self.age() < 1

    def age(self):
        """ Calculates the age of the dog as the difference between today and born date and returns it.
        """
        today = datetime.datetime.today()
        return today.year - self.born.year

    def __repr__(self):
        """ Dog representation method
        """
        return(self.image + "\nI'm {}! I'm {} year(s) old and I look like a {}.\
                             \nI've been at the shelter since {}\nYou can visit me in kennel {}".\
                  format(self.name, self.age(), self.breed, self.intake_date.strftime("%B-%d-%Y"), self.kennel))


class Kennel:
    """ This is the class for a kennel.
    """

    def __init__(self, num, capacity=1,):
        """ Initializes a kennel with an identifier (num) and capacity.
            It also initializes the guests of the kennel as an empty list.
        """
        self.num = num
        self.capacity = capacity
        self.guests = []

    def is_full(self):
        """ Returns True if the kennel is full, False if it is not full
        """
        return (self.capacity == len(self.guests))

    def add_dog(self, dog):
        """ Adds dog to the kennel's guests list
        """
        self.guests.append(dog)

    def __repr__(self):
        """ Kennel representation method
        """
        dogs_names = [dog.get_name() for dog in self.guests]
        return "kennel: {}, capacity: {}, guests: {}".format(self.num, self.capacity, ",".join(dogs_names))

class Playgroup:
    """ Not implemented yet (I did not have time)
    """
    pass

####################################################################
# Create the Shelter
interface = Interface('start')
shelter = Animal_Shelter(interface, 20)

# Let's add a few dogs to the shelter
leo = shelter.add_dog(shelter.next_kennel(), "Leo", 2015 , "Labrador Retriever", datetime.datetime(2017, 7, 8))
cosmo = shelter.add_dog(shelter.next_kennel(), "Cosmo", 2016, "Chihuahua")
rosie = shelter.add_dog(shelter.next_kennel(), "Rosie", 2009, "Golden Retriever")
petunia = shelter.add_dog(shelter.next_kennel(), "Petunia", 2016, "Mix", datetime.datetime(2015, 7, 8, 12))
elliot = shelter.add_dog(shelter.next_kennel(), "Elliot", 2018, "Mix")
dakota = shelter.add_dog(shelter.next_kennel(), "Dakota", 2014, "Lab-Mix", datetime.datetime(2018, 1, 13))
paco = shelter.add_dog(shelter.next_kennel(), "Paco", 2009, "Golden Retriever", datetime.datetime(2018, 1, 13))
ozzie = shelter.add_dog(shelter.next_kennel(), "Ozzie", 2017, "German Sheperd", datetime.datetime(2018, 3, 22))
champ = shelter.add_dog(shelter.next_kennel(), "Champ", 2015, "Lab", datetime.datetime(2018, 7, 10))
loo = shelter.add_dog(shelter.next_kennel(), "Loo", 2015, "Pit-mix", datetime.datetime(2014, 1, 10))

# and walk them
leo.walks(datetime.datetime(2018, 7, 8, 16, 30))
cosmo.walks(datetime.datetime(2018, 7, 8, 8, 30))
rosie.walks(datetime.datetime(2018, 7, 8, 16, 30))
petunia.walks(datetime.datetime(2018, 7, 10, 8, 30))
elliot.walks(datetime.datetime(2018, 7, 11, 17, 15))
dakota.walks(datetime.datetime(2018, 7, 13, 7, 0))
paco.walks(datetime.datetime(2018, 7, 12, 17, 0))
ozzie.walks(datetime.datetime(2018, 7, 12, 7, 30))
champ.walks(datetime.datetime(2018, 7, 12, 18, 30))
loo.walks(datetime.datetime(2018, 7, 13, 15, 30))

# interact with the Shelter
shelter.play()

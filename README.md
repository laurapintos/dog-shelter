# dog-shelter
project done as part of the course "Fundamentals of Python for Data Science" in the MIDS program, summer 2018.

## How to use it
Just type **python shelter.py** in the command line.
The user interface will display and you can select:
* 1 if you want to interact as an employee/volunteer to intake, walk, register the walk or get the shelter status.
* 2 if you want to interact as a potential adopter looking for dogs.

Note: does not include persistence, so I added some dogs and walked them as part of the code in shelter.py

## About the code
The main classes are Animal_Shelter, Kennels and Dogs, of course.
There is also a group of classes to allow the user to interact with the shelter. I just replicated the design of the material suggested in the class “Learn python the hard way”, although I understand that the design in the book is more suited for a game. My Interface class which manages the different UIs is the equivalent to the Map class that manages the scenes in the book.

## What is next
* Add Persistence. I learnt about **pickle**  during the project presentations class. I plan to incorporate it.
* Add more attributes to the Dog class:
List of traits (characteristics): dog friendly, kid friendly, house trained, etc....knowing these characteristics will make the dogs more adoptable. While it is very easy to include this at the dog class level, I did not have time to design the interfaces for the users to set these attributes.

* Add a friendships attribute to the Animal_Shelter class. I conceive it as a list of tuples [(dog1, dog4), (dog2, dog3), ...]. This will allow to create playgroups, groups of dogs that are friendly to each other. The playgroups are a more efficient way to walk the dogs, as a volunteer can supervise groups of five, six dogs at a time instead of walking them.

import random
from grouper import Grouper

men = ["Hunter", "Micah", "Jason", "Jules", "Luke", "Wesley", "Bryce", "Mitchell", "Jacob", "Ethan", "Chris"]
women = ["Darby", "Renee", "Emily", "Grace", "Sarah", "Nicole", "Danning", "Janice", "Ashlyn", "Laura"]

    
grouper = Grouper(men)
grouper.makeGroups(4)
grouper.makeGroups(4)
grouper.finalizeGroups()

test = grouper.parseFromFile()     
print(test)  
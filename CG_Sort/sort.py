import random

men = ["Hunter", "Micah", "Jason", "Jules", "Luke", "Wesley", "Bryce", "Mitchell", "Jacob", "Ethan", "Chris"]
women = ["Darby", "Renee", "Emily", "Grace", "Sarah", "Nicole", "Danning", "Janice", "Ashlyn", "Laura"]

def validateMember(person, group):
    valid = True
    for p in group:
        if p == person:
            valid = False
            break
    return valid

def makeGroups(size, people):
    groups = []
    while len(people) > 0:
        group = []
        counter = 0
        while counter <= size:
            for person in people:
                if counter > size or :
                    groups.append(group)
                    break
                if len(group) == size:
                    break
                elif len(group) == 0:
                    group.append(person)
                    people.remove(person)
                    counter += 1
                else:
                    if validateMember(person, group):
                        group.append(person)
                        people.remove(person)
                        counter += 1

    return groups


makeGroups(men, )


        
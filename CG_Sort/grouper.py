import random

class Grouper:
    def __init__(self, people):
        self.people = people
        self.groups = []
    
    def makeGroups(self, size):
        while len(self.people) > 0:
            group = []
            while len(group) < size:
                if len(self.people) == 0:
                    break
                person = random.choice(self.people)
                if len(group) == 0:
                    group.append(person)
                else:
                    if self.validateMember(person, group):
                        group.append(person)
                    else:
                        continue
                if len(group) == size:
                    check = self.checkPrevious(group)
                    if len(check) == 0:
                        self.groups.append(group)
                        for person in group:
                            self.people.remove(person)
                    else:
                        print(f"Group {group} is too similar to previous group {check}. Trying again")
                        group.clear()
    
    
    def validateMember(self, person, group):
        valid = True
        for p in group:
            if p == person:
                valid = False
                break
        return valid
    

    def checkPrevious(self, current_group):
        past_lists = self.parseFromFile()
        for group in past_lists:
            print(f"Comparing current group ({current_group}) with {group}")
            diff = [x for x in current_group if x not in group]
            print(f"Diff: {diff}")
            if len(diff) <= 2:
                return group
        return []
    
    
    def finalizeGroups(self):
        answer = ''
        while answer != "y" and answer != 'n':
            print("The groups are:")
            for group in self.groups:
                print(group)
            answer = input("Is this ok? (y/n)")
            if answer == 'y':
                print("Writing to file...")
                self.writeToFile()
            elif answer == 'n':
                exit
            else:
                print("Please answer 'y' or 'n'")
    

    def readFromFile(self):
        with open("past_groups.txt", "r") as file:
            past_groups = file.read()
        return past_groups

    
    def writeToFile(self):
        with open("past_groups.txt", "a") as file:
            for group in self.groups:
                file.write("BEGIN GROUP\n")
                for person in group:
                    file.write(person)
                    file.write('\n')

    
    def parseFromFile(self):
        parsed_groups = []
        past_groups = self.readFromFile()
        print("Past Groups:")
        print(past_groups)

        if past_groups != '':
            groups = past_groups.split("BEGIN GROUP\n")
            for people in groups:
                parsed_groups.append(people.split('\n'))
                #print(parsed_groups)
            for group in parsed_groups:
                if len(group) <= 1:
                    parsed_groups.remove(group)
                for item in group:
                    if item == '':
                        group.remove(item)
        return parsed_groups
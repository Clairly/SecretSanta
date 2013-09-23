__author__ = 'victoriasater'

import random
class Individual:
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last
        self.selection = None
        self.picked = False

    def chosen(self):
        self.picked = True

    def select(self, individual):
        self.selection = individual

class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def add_member(self, first):
        new_member = Individual(first, self.last_name)
        self.members.append(new_member)

    def print_family(self):
        print "Family Name:", self.last_name
        for member in self.members:
            print member.first_name

print "Welcome to the Cousin Gift Exchange Selection Tool!"
names = raw_input("Enter the names (First Last) of everyone included in the exchange separated by commas: ")
names = names.split(', ')
families = []
individuals = []
for name in names:
    name = name.split(' ')
    first_name = name[0]
    last_name = name[1]
    exists = False
    for family in families:
        if family.last_name == last_name:
            exists = True
            break
    if not exists:
        # add family
        new_family = Family(last_name)
        new_family.add_member(first_name)
        families.append(new_family)
    else:
        # add individual
        family.add_member(first_name)
# order families by number of members in each family, descending
families.sort(key=lambda x: len(x.members), reverse=True)

print ""
for current_family in families:
    for individual in current_family.members:
        choosable = []
        current_individual = None
        # create list of people that this specific person can be allowed to choose
        for family in families:
            # if they don't have the same last name, they are not siblings and are not already picked
            if family.last_name != individual.last_name:
                new_list = [member for member in family.members if not member.picked]
                choosable.extend(new_list)
            else:
                for member in family.members:
                    if member.first_name == individual.first_name:
                        current_individual = member
                        break

        random.seed()
        selection = random.randint(0,len(choosable)-1)
        print individual.first_name, individual.last_name, "chooses", choosable[selection].first_name, choosable[selection].last_name
        current_individual.select(choosable[selection])
        choosable[selection].chosen()
import json

class Person:

    def __init__(self, fname, lname, age, gender):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender


        



person1 = Person("Nitish","singh",33,"male")


def show_object(person1):
    if isinstance(person1, Person):
        return "first Name -> {}, last name -> {}, age -> {}, gender -> {}".format(person1.fname, person1.lname, person1.age,person1.gender)
    

with open('file-handling/pp.json','w') as f:
    json.dump(person1,f,default=show_object)



with open("file-handling/pp.json",'r') as rf:
    d = json.load(rf)
    print(d)
    print(type(d))

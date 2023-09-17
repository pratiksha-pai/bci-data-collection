import csv

class Person:

    def __init__(self, name, history, position):
        self.name = name
        self.history = history
        self.position = position
        print(history)

def read_file():
    path = "/Users/jackmostyn/Downloads/groups.csv"
    content = []
    with open(path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            content.append(row)   
    return content

def separate(content):
    names = content[0]
    names.pop(0)
    content.pop(0)
    history = [row[1:] for row in content]
    return names, history

def create_people(names, history):
    people = []
    position = 0
    for name in names:
        new_person = Person(name,history,position)
        people.append(new_person)
        position = position + 1
    return people

def main():
    #import the file
    content = read_file()
    #separates the names and the history
    names, history = separate(content)
    #creates all the person objects
    people = create_people(names, history)
    #processes the history
    
main()
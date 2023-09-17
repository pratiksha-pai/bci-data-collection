import csv

def csv_to_array(filename):
    data_array = []
    
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data_array.append(row)
            
    return data_array

# Example usage:
filename = "/Users/jackmostyn/Downloads/groups.csv"
result_array = csv_to_array(filename)
names = result_array[0]
names.pop(0)
result_array.pop(0)
result_array = [row[1:] for row in result_array]
person_sums = []
person_missing = []
missing_sums = []
for person in result_array:
    sum = 0
    count = 0
    missing_count = 0
    missing = []
    for entry in person:
        if entry == "1":
            sum = sum + 1
        else:
            missing_count = missing_count + 1
            missing.append(count)
        count = count + 1
    person_missing.append(missing)
    person_sums.append(sum)
    missing_sums.append(missing_count)

i1 = 0

for missing in person_missing:
    i2 = 0
    for indiv in missing:
        if indiv == i1:
            missing.pop(i2)
        i2 = i2 + 1
    i1 = i1 + 1


# we have which people each person is missing
# and the total number of people missing per person
# lets start by making the first instance of groups that will work
# we can do this by picking the first person and forming all their groups
# then move on to the second person and fill in the rest of their groups
# keep doing this until it isn't possible for one person
# then undo the last step and instead try to fill in this new persons groups
# move forward like this
# if all options are exhausted for one step back then go two steps back and repeat
# this wont work because some repeats will probably be necessary
# what if i form every group and then check to see if it follows the rules
# can just count repeats and use it as 
# Write your code here

######### HINT: create a dictionary from flowers.txt #########
file = 'flowers.txt'

def creatingFlowerDictionay(file):
    # initialize an empty dictionary
    flowers = {}
    
    # open the file in read mode
    with open(file, 'r') as file:
        # read lines from the file
        lines = file.readlines()
        
    # iterate through each line and split key-value pairs
    for line in lines:
        key, value = line.strip().split(':')
        flowers[key.strip()] = value.strip()
    return flowers

########## HINT: create a function to ask for user's first and last name #########
def firstAndLastName():
    flower_dict = creatingFlowerDictionay('flowers.txt')
    name = input('Enter your First [space] Last name only: ')
    first_letter = name[0]   
    print(f"Unique flower name with the first letter: {flower_dict[first_letter]}")


# print the desired output
firstAndLastName()
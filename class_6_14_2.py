# Write your code here

######### HINT: create a dictionary from flowers.txt #########
file = 'flowers.txt'

# open the file in read mode
with open(file, 'r') as file:
    # read lines from the file
    lines = file.readlines()
    
# initialize an empty dictionary
flowers = {}

# iterate through each line and split key-value pairs
for line in lines:
    key, value = line.strip().split(':')
    flowers[key.strip()] = value.strip()
    
# print the dictionary
print(flowers)

########## HINT: create a function to ask for user's first and last name #########
def firstAndLastName():
    name = input('Enter your name: ')
    last_name = input('Enter your last name: ')
    print(f'Hello, {name} {last_name}')


# print the desired output
firstAndLastName()
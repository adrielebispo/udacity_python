file = open('flowers.txt', 'r')

# read method
file_data = file.read()
# always have to close a file after open it
file.close()

## The code bellow is the same thing of what we've done above
# with open('my_path/my_file.txt', 'r') as f:
#     file_data = f.read()

print(type(file_data))
print(file_data)

# modifing a file
test_file = open('teste.txt', 'w')
test_file.write('Every time I add content to my file using the "write" function ("w"), the old content in the file \nis deleted and replaced with the new one. If you only want to add something to the file, the\nonlocal best way to modify it is by using append')
test_file.close()

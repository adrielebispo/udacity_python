names = [x for x in input('Enter names separated by commas: ').split(", ")]
assignments =  [int(x) for x in input('Enter assignments separated by commas: ').split(", ")]
grades =  [float(x) for x in input('Enter grades separated by commas: ').split(", ")]

## message string to be used for each student
## HINT: use .format() with this string in your for loop
## write a for loop that iterates through each set of names, assignments, and grades to print each student's message

for i in range(len(names)):
    if grades[i] < 100:
        potential = grades[i] + grades[i]*0.2
        if potential > 100:
            potential = 100
    else: 
        potential = grades[i]
        message = f"""Hi {names[i]},\n\nThis is a reminder that you have {assignments[i]} assignments left to
            submit before you can graduate. Your current grade is {grades[i]} and can increase
            to {potential} if you submit all assignments before the due date.\n\n"""
    print(message)



name = input("Enter Name: ")
id = input("ID number: ")
course = input("Course: ")
section = input("Section: ")

first = float(input("Enter 1st quarter: "))
second = float(input("Enter 2nd quarter: "))
third = float(input("Enter 3rd quarter: "))
fourth = float(input("Enter 4th quarter: "))

average = (first + second + third + fourth) / 4

print("Student's name: " + name)
print("ID number: ", id)
print("Course: " + course)
print("section: " + section)
print("Average Grade:", average)

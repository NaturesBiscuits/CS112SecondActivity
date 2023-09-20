name = input("Enter Name: ")
id = input("ID number: ")
course = input("Course: ")
section = input("Section: ")

first = float(input("Enter 1st quarter grade: "))
second = float(input("Enter 2nd quarter grade: "))
third = float(input("Enter 3rd quarter grade: "))
fourth = float(input("Enter 4th quarter grade: "))

average = (first + second + third + fourth) / 4

print("Student's name: " + name)
print("ID number: ", id)
print("Course: " + course)
print("section: " + section)
print("Average Grade:", average)

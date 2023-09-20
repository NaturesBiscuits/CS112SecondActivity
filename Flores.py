
name = input("Enter Name: ")
id = input("ID number: ")
course = input("Course: ")
section = input("Section: ")

first = float(input("Enter 1st semester grade: "))
second = float(input("Enter 2nd semester grade: "))
third = float(input("Enter 3rd semester grade: "))
fourth = float(input("Enter 4th semester grade: "))

average = (first + second + third + fourth) / 4

print("Student's name: " + name)
print("ID number: ", id)
print("Course: " + course)
print("section: " + section)
print("Average Grade:", average)

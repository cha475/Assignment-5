
# Problem Statement: Write a Python program that:
# 1.   Creates a dictionary where student names are keys and their marks are values.
# 2.   Asks the user to input a student's name.
# 3.   Retrieves and displays the corresponding marks.
# 4.   If the student’s name is not found, display an appropriate message.


# Step 1: Create a dictionary with student names as keys and their marks as values
student_marks = {"Abhijeet":89, "Rohit":78, "Sakshi":92, "Ankita":85}

# Step 2: Ask the user to input a student's name
student_name = input("Enter the student's name: ")

# Step 3: Retrieve and display the corresponding marks

if student_name in student_marks:
    print(f"{student_name}'s marks is : {student_marks[student_name]}")
else:
    print("Student's name is  not found.")
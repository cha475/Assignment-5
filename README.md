# Assignment-5

Task1.py
------

Code Used
-------

# Step 1: Create a dictionary with student names as keys and their marks as values
student_marks = {"Abhijeet":89, "Rohit":78, "Sakshi":92, "Ankita":85}

# Step 2: Ask the user to input a student's name
student_name = input("Enter the student's name: ")

# Step 3: Retrieve and display the corresponding marks

if student_name in student_marks:
    print(f"{student_name}'s marks is : {student_marks[student_name]}")
else:
    print("Student's name is  not found.")



Execution:
--------

python Task1.py

Output
------

Name exists
--------

Enter the student's name: Abhijeet
Abhijeet's marks is : 89

Name not exist
----------
Enter the student's name: chandra
Student's name is  not found.


Task2.py
------
Code used
------

number = list(range(1,11))

elements = number[:5]

reverse_elements = elements[::-1]

print("Extracted elements:", elements)
print("Reversed elements:", reverse_elements)

Execution
--------
python Task2.py

Output
----

Extracted elements: [1, 2, 3, 4, 5]
Reversed elements: [5, 4, 3, 2, 1]

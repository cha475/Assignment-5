# Problem Statement: Write a Python program that:
# 1.   Creates a list of numbers from 1 to 10.
# 2.   Extracts the first five elements from the list.
# 3.   Reverses these extracted elements.
# 4.   Prints both the extracted list and the reversed list
 

# Step 1: Create a list of numbers from 1 to 10
number = list(range(1,11))

elements = number[:5]

reverse_elements = elements[::-1]

print("Extracted elements:", elements)
print("Reversed elements:", reverse_elements)
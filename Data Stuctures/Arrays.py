# Define an array
numbers = [10, 20, 35, 40, 41, 56, 89, 56]

# Accessing elements
print("4th Element:", numbers[3])
print("Last Element: ", numbers[5])

# Modifying Element
print("Before Modified Element", numbers[1])
numbers[1] = 25
print("Modified Element", numbers[1])


# Get Length of array
print(len(numbers))


#Adding an element
numbers.append(62)
numbers.append(250)

#Removing Element
numbers.remove(10)
numbers.remove(41)

# Iterating through an array
for shawn in numbers:
    print(shawn)

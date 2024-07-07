# Creating a dictionary
student = {
    "name": "Alice",
    "age": 23,
    "major": "Computer Science"
}

# Accessing items
print(student["name"])  # Output: Alice
print(student["age"])   # Output: 23

# Modifying items
student["age"] = 24
print(student["age"])  # Output: 24

# Adding items
student["GPA"] = 3.8
print(student)

# Removing items using del
del student["major"]
print(student)

# Removing items using pop()
gpa = student.pop("GPA")
print(gpa)  # Output: 3.8
print(student)

# Iterating through keys
for key in student:
    print(key)

# Iterating through values
for value in student.values():
    print(value)

# Iterating through key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")

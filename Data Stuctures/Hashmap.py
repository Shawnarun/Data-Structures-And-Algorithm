# Creating a hashmap (dictionary in Python)
hashmap = {}
print("Initial hashmap:", hashmap)

# Inserting key-value pairs
hashmap["apple"] = 3
hashmap["banana"] = 5
hashmap["cherry"] = 7
print("After inserting items:", hashmap)

# Retrieving values by key
print("Value associated with 'apple':", hashmap["apple"])  # Output: 3
print("Value associated with 'banana':", hashmap["banana"]) # Output: 5

# Deleting key-value pairs
del hashmap["banana"]
print("After deleting 'banana':", hashmap)

# Checking if a key exists in the hashmap
if "apple" in hashmap:
    print("Apple exists in the hashmap")
if "banana" not in hashmap:
    print("Banana does not exist in the hashmap")

#hiiiiiiiii


# List in python
# List is a collection which is ordered and changeable. Allows duplicate members.

# Create a List:

#                           list index start from 0
                    #  0            1        2        3        4       5        6
fruits : list[str] = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(fruits) # ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print(fruits[0]) # apple
print(fruits[2]) # cherry

# list index start from 0 and list length start from 1
# list lenght
print(len(fruits)) # 7

# slice method in list
# slice method is used to get a specific range of elements from the list
# slice method return a new list
# slice method take two arguments start and end

print(fruits[0:5]) # ['apple', 'banana', 'cherry', 'orange', 'kiwi']
print(fruits[2:5]) # ['cherry', 'orange', 'kiwi']

# in method in list
# in method is used to check if a specified element is present in the list
# in method return a boolean value True or False

print("apple" in fruits) # True
print("grape" in fruits) # False


# append method in list
# append method is used to add a single element at the end of the list
# append method take one argument which is the element that you want to add in the list

print(fruits)
fruits.append("grape")
print(fruits) # ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango', 'grape']

# remove method in list
# remove method is used to remove a specific element from the list
# remove method take one argument which is the element that you want to remove from the list

print(fruits)
fruits.remove("kiwi")
print(fruits) # ['apple', 'banana', 'cherry', 'orange', 'melon', 'mango', 'grape']

# insert method in list
# insert method is used to add a single element at a specific index in the list
# insert method take two arguments first is the index and second is the element that you want to add in the list

print(fruits)
fruits.insert(2, "guava")
print(fruits) # ['apple', 'banana', 'guava', 'cherry', 'orange', 'melon', 'mango', 'grape']

# pop method in list
# pop method is used to remove a specific element from the list
# pop method take one argument which is the index of the element that you want to remove from the list

print(fruits)
fruits.pop(2)
print(fruits) # ['apple', 'banana', 'cherry', 'orange', 'melon', 'mango', 'grape']
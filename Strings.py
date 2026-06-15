# Strings in Python
name = "Alice"

# String slicing
print(name[0])  # Output: A
print(name[1])  # Output: l
print(name[2])  # Output: i
print(name[3])  # Output: c
print(name[4])  # Output: e

#string slicing to desired extend [0: n-1]
print(name[0:5])  # Output: Alice
print(name[1:4])  # Output: lic

# string slicing with step
print(name[0:5:1])  # Output: Alice
print(name[0:5:2])  # Output: Aec

#string functions
print(name.upper())  # Output: ALICE
print(name.lower())  # Output: alice   
print(name.capitalize())  # Output: Alice
print(name.replace("A", "B"))  # Output: Blice

n = "Jerry K Paul"
print(n.split())  # Output: ['Jerry', 'K', 'Paul']
'''divide the string into list of words and the default separator is space'''


#string 
a = 10
print(a.isnumeric())  # Output: false

a = "10"
print(a.isnumeric())  # Output: true

'''isnumeric() is a string method that checks if all characters in the string
 are numeric (digits).'''

b = "hello123"
print(b.isalnum())  # Output: True

"""isalnum() is a string method that checks if all characters in the string
 are alphanumeric (letters and digits)."""
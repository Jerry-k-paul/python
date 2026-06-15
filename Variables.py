#variables and data types
name = "Alice"
age = 30

print("Name:", name)
print("Age:", age)

print(type(name))  # Output: <class 'str'>
print(type(age))   # Output: <class 'int'>
print(name,age)  # Output: Alice 30

#Variable adding 

x = 10
y = 30

print(x + y)  # Output: 40
print(x - y)  # Output: -20

x = 5.0

print(x * y)  # Output: 150.0

#Variable string addition
first_name = "Alice"
last_name = "Smith"
full_name = first_name + " " + last_name
print(full_name)  # Output: Alice Smith

"""cannot add string and int
age = 30
message = "I am " + age + " years old."  # This will raise a TypeError
To fix this, we can convert the integer to a string"""

age = 30
message = "I am " + str(age) + " years old."
print(message)  # Output: I am 30 years old.


#multiple assignment
a, b, c = 1, 2, 3
print(a)  # Output: 1  
print(b)  # Output: 2
print(c)  # Output: 3

x = y = z = 0
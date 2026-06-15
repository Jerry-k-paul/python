total_sum = 10 + 20 + 30 + 40
print(total_sum)  # Output: 100


#this will give the same output as above but we can break the line using \ and it will continue to the next line
total_sum = 10 + 20 \
    + 30 + 40

#this will also give the same output as above but we can break the line using parentheses and it will continue to the next line
total_sum = (10 + 20 +
              30 + 40)


#typecasting
num1 = "10"
n2 = int(num1)  # Convert string to integer
print(n2)  # Output: 10

'''interger and float get added and the output will be float
but why? 
because python automatically converts the integer to float and then adds them
this known as immplicit type conversion or type casting
when we do the conversion manually it is known as 
explicit type conversion or type casting'''
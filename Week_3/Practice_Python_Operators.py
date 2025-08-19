# Comparison Operators
# a = 10
# b = 20
# # print(a == b)
# # print(a != b)
# # print(a > b)
# # print
# # print(a >= 10)
# # print(b <= 25)

# # # Use case Example- student Exam Result
# # score = 75
# # print (score >= 50) # True (Passed)
# # print(score < 50)   # False (Failed)
# # print(score == 100) # False (Not full marks)

#  # Assignment Operators: Assignment operators are used to assign values to variables. They can also combine an operation with assignment, so instead of writing `x = x + 5`, we can write x` += 5`.
# x = 10
# print("Initial value:", x)

# x += 5
# print("After x += 5:", x)

# x -= 2
# print("After x -= 2:", x)

# x *= 3
# print("After x *=3:", x)

# x /= 4
# print("After x/=4:", x)

# x %= 3
# print("After x %= 3:", x)

# x = 4
# x **= 2
# print("After x **= 2:", x)

# x //= 3
# print("After x //= 3:", x)

# # Use case Example
# # Define
# balance = 1000
# deposit = 200
# withdraw = 150
# balance += deposit #Add deposit
# balance -= withdraw #Subtract withdrawal
# print("Updated Balance:", balance)

#Logical Operators
#  Logical operators are used to combine conditional statements. They work with Boolean values (True or False).

x = 10
y = 20

# and operator
print(x > 5 and y > 15) # True

# or operator
print(x < 5 or y > 15)

# not operator
print(not(x == 10)) #  False

# Use case example 1- Scholarship Eligibility
# Define variables
age = 17
score = 85
# Must be younger than 18 AND score above 80
eligible = (age < 18) and (score > 80)

print("Scholarship Eligible:", eligible)
# Output: Scholarship Eligible: True

# Use case example2 - Event Access
age = 22
has_ticket = False
can_enter = (age >= 18) and (has_ticket or age < 25)

print("Access Granted:", can_enter)





# # Task1- Explain each output of the program below.
# # Give 3 usecases or cenarios where you can apply the program below.
# # # Write the code for 1 of the 3 use cases.

# num1 = int(input("Enter first number;")) 
# num2  = int(input("Enter second number: "))
# print(f"{num1} == {num2} : {num1 == num2}")
# #The above depicts equality to show if num1 is equal to num2.

# print(f"{num1} != {num2} : {num1 != num2}")
# #The above depicts inequality; showing if num1 is equal to num2.

# print(f"{num1} > {num2} : {num1 > num2}")
# # The above generated an output showing if num1 is equal to num2

# print(f"{num1} < {num2} : {num1 < num2}")
# # The above generated an output showing if num1 is unequal to num2

# #Use cases where the above can program can be applied:
# #Scenario 1: Camparison between total numbers of male vs female in a classroom

# #Scenario 2: Comparison between the total number of laity versus clergy in the Arch-diocese.

# # Scenario 3 : Comparison  between the number of animate vs inanimate things.

# male = int(input("Enter the number of male students: ")) 
# female  = int(input("Enter the number of female students:  "))
# print(f"{male} == {female} : {male == female}")
 
#  # Task2
#  # Question 2.1
# name = input("Enter your name: ") # Collects input for name variable.
# age = int(input("Enter your age: ")) # Collects input for age variable as an integer.
# score = int(input("Enter your test score: ")) # Collects the score variable as an integer.
# eligibility = (age < 18) and (score > 70) #Ascertains eligibility by comparing age and score
# print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}") # Using f-string, the print displayed candidate's name, age, score and eligibility; all on a new line.
# '''
# The code collected user details and determined eligibilty of candidates.
# '''
# #Question 2.2
# name = input("Enter your name: ")
# citizenship = input("Enter your country of citizenship: ")
# enrolment = input("Enter your study route: ")
# scholarship = input("Are you receiving other scholarships?: ")
# Academic_qualifications = input("Enter your academic qualifications: ")
# eligibility = (citizenship == "Nigeria") and (enrolment == "Full-time") and (scholarship == "No") and (Academic_qualifications == "five distinctions including Maths and English")
# print(f"Candidate: {name}\nCitizenship: {citizenship}\nScholarship: {scholarship}\nQualifications: {Academic_qualifications}\nEligible: {eligibility}")

# # Task 3: Online Store Cart Calculation
# items = ["Phone", "Earpiece","Powerbank", "USB cord"]
# price = [ 1000, 500, 300, 150]
# cart_total = 0
# cart_total += price[0]
# cart_total += price[1]
# cart_total += price[2]
# cart_total += price[3]
# print(cart_total)
# # cart_total += sum(price)
# # print(f"cart_total: {cart_total}")

# #Task4: Student Record
# student = {}              
# name = input("Enter your name: ")
# age = int(input("What is your age? "))

# scores = [70, 67, 89, 25]

# average_score = (70+ 67 + 89 +25)/4
# print(average_score)
# passed = (average_score>=63) # True

# teenager = (age > 12) and (age < 20)

# # print(average_score)
# print(f"\nStudent Record:\nName: {name}\nAge: {age}\nScores: {scores}\nPassed: {passed}\nTeenager: {teenager}")


# Task 5: Store Inventory Update.
# Create a dictionary called store with items and their available quantities.

# # Available items
# store = {}
# items = ["Phones", "Tabs", "Chargers", "Watches"]

# # Available quantities
# quantities = [100, 150, 86, 125]
# print("The following are the available items: ")
# store = {items[0]: quantities[0], items[1]: quantities[1], items[2]: quantities[2], items[3]: quantities[3]}
# before_purchase = {item: quantity for item, quantity in store.items()}
# print(store)

# # Ask the user to input the item they want to buy
# item_needed = input("\nEnter the item you need: ")

# # Ask the user to input the quantity they want to purchase.
# quant_needed = int(input("Enter quantity needed: "))

# # Use the assignment operator (-=) to update (reduce) the item quantity in the dictionary.
# store[item_needed] -= quant_needed
# print(store)

# # Print the updated dictionary
# print(f"\n\t===Updated Dictionary===\nBefore purchase: {before_purchase}")
# print(f"After purchase: {store}")


# #Task 5: 
# store = {"Phones": 15, "Tabs": 30, "Chargers": 9}

# print(store)
# item = input("What item do you want to buy?" )
# quantity = int(input("Enter how many quantities you want to purchase: "))
# store["Phones"] -= 2
# print(store)

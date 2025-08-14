# Task 1: Favorite life quote
lifeQuote = input("Enter your favorite life quote: ")
lifeQuote = lifeQuote.title()
print(f"\"{lifeQuote}\"")

# Task 2: Shopping list manager
shoppingList = []
userInput = input("Enter the first item: ")
shoppingList.append(userInput)
userInput = input("Enter the second item: ")
shoppingList.append(userInput)
userInput = input("Enter the third item: ")
shoppingList.append(userInput)
print(shoppingList)

# Task 3: Word counter
word = input("Enter a sentence: ")
print(len(word.split()))

# Task 4: Name Organozer
userInput = input("Enter 5 names separated by spaces: ")
userInput = userInput.lower().split()
userInput.sort()
print(userInput)

# Task 5: Student score tracker
studentNames = []
studentScores = []
print("You will enter three student names")
student_1_name = input("Enter 1st student's name: ")
studentNames.append(student_1_name)

student_2_name = input("Enter 2nd student's name: ")
studentNames.append(student_2_name)

student_3_name = input("Enter 3rd student's name: ")
studentNames.append(student_3_name)

student_1_score = input("Enter student 1 score: ")
studentScores.append(student_1_score)

student_2_score = input("Enter student 2 score: ")
studentScores.append(student_2_score)

student_3_score = input("Enter student 3 score: ")
studentScores.append(student_3_score)

print(f"Student\t Scores\n{studentNames[0]}\t{studentScores[0]}\n{studentNames[1]}\t{studentScores[1]}\n{studentNames[2]}\t{studentScores[2]}\n")


# Task 6: Word Analyzer
word = input("Enter a word: ")
print(f"Length of the word you entered is: {len(word)}")
print(f"It is {word.upper() == word} that the word you entered is in uppercase")
print(f"It is {word.lower() == word} that the word you entered is in lowercase")
print(f"It is {word.title() == word} that the word you entered is in title case")

# Task 7: List manipulation
cities = ["Abeokuta", "Lagos", "Ibadan", "Abuja", "New York"]
print(cities)
new_city = input("Enter a new city name: ")
cities.remove(cities[2])
cities.insert(2, new_city)
print(cities)
print("Removing the last city")
cities.pop()
print(cities)
print("Adding new city to the bggining")
cities.insert(0, "Accra")
print(cities)
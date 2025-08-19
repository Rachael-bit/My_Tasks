#Task4: Student Record
student = {}              
name = input("Enter your name: ")
age = int(input("What is your age? "))

scores = [70, 67, 89, 25]

average_score = (70+ 67 + 89 +25)/4
print(average_score)
passed = (average_score>=63) # True

teenager = (age > 12) and (age < 20)

# print(average_score)
print(f"\nStudent Record:\nName: {name}\nAge: {age}\nScores: {scores}\nPassed: {passed}\nTeenager: {teenager}")


# Store seat numbers (1 to 50) in a set
seat_numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50}

# Question 1 Ask user to book a seat from 1 - 50
book_seat = int(input("Book a seat from 1 to 50: "))

# Remove booked seats from the set
seat_numbers.remove(book_seat)

# Show remaining seats after booking
print(seat_numbers)

# Question 2- Ask user to enter 5 favorite fruits
fruit1 = input("Favorite fruit one: ")
fruit2 = input("Favorite fruit two: ")
fruit3 = input("Favorite fruit three: ")

# Store them in a set
fav_fruits = {fruit1, fruit2, fruit3}

# Display them
print("Favourite Fruits: ", fav_fruits)

# ====================== OR ===============
fav_fruits_too = set()
fruit_one = input("Favorite fruit one: ")
fav_fruits_too.add(fruit_one)
fruit_two = input("Favorite fruit two: ")
fav_fruits_too.add(fruit_two)
fruit_three = input("Favorite fruit three: ")
fav_fruits_too.add(fruit_three)
print("Second Favorite Fruits: ", fav_fruits_too)


# Question 3
# Collect the names of people attending a seminar
seminar_attendance = set()
seminar_attendance.add(input("What is your name?: "))
seminar_attendance.add(input("What is your name?: "))
seminar_attendance.add(input("What is your name?: "))
seminar_attendance.add(input("What is your name?: "))
seminar_attendance.add(input("What is your name?: "))

# Display them in alphabetical order
attendance_list = list(seminar_attendance)
attendance_list.sort()
print("Seminar Attendance in Alphabetical Order: ", attendance_list)


# Question 4
# Ask for voters names and store in a set
# if voter registers twice, display a warning
voters = set()
voter_name = input("Enter your name: ")
if voter_name in voters:
  print("Vote already registered for this user!!!")
else:
  voters.add(voter_name)
  print(voters)
voter_name2 = input("Enter your name: ")
if voter_name2 in voters:
  print("Vote already registered for this user!!!")
else:
  voters.add(voter_name2)
  print(voters)
voter_name3 = input("Enter your name: ")
if voter_name3 in voters:
  print("Vote already registered for this user!!!")
else:
  voters.add(voter_name3)
  print(voters)
voter_name4 = input("Enter your name: ")
if voter_name4 in voters:
  print("Vote already registered for this user!!!")
else:
  voters.add(voter_name4)
  print(voters)
voter_name5 = input("Enter your name: ")
if voter_name5 in voters:
  print("Vote already registered for this user!!!")
else:
  voters.add(voter_name5)
  print(voters)

print("Voters Registration: ", voters)

# Display the total number of unique votes
print("Total Number of Voters: ", len(voters))

# Task 6: 
# Collecting candidate's details.
print("UNILAG Admission Eligibility Checker for 2025/2026 Academic Session.")
print("\nKindly fill the following appropriately to check your eligibily for admission.")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
course = input("Enter your preferred course of study: ")
duration = int(input("How many years is your course?: "))
utme = int(input("Enter your UTME score: "))
choice = input("Did you choose UNILAG as your first choice school?: ")
waec = input("Do you have at least 5 credit passes at one sitting in relevant O'Level subjects, including English Language and Mathematics?: ")
post_utme = int(input("Enter your POST UTME screening score result: "))
dept_cut_off = int(input("Enter your departmental cut-off mark (200-320): "))

eligibility = (age >= 16) and (utme >= 200) and (choice == "Yes") and (waec == "Yes") and (post_utme >= 50) and (dept_cut_off >= 200)

result = {True: "Congratulations, you have been offered provisional admission", False: "Sorry, No admission given."}

# Final decision
print(f"\nName: {name}\nAge: {age}\nCourse of study: {course}\nDuration: {duration}\nUTME score: {utme}\nIs UNILAG your first choice?: {choice}\nDo you  have 5 credit passes in your O' level result?: {waec}\nPOST UTME score: {post_utme}\nDepartmental Cut-off Mark: {dept_cut_off}\n\n\t====Admission Status===\nAdmission Status: Dear {name}, {result[eligibility]} to study {course} for {duration} years.")
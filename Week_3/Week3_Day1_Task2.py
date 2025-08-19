 # Task2
 # Question 2.1
name = input("Enter your name: ") # Collects input for name variable.
age = int(input("Enter your age: ")) # Collects input for age variable as an integer.
score = int(input("Enter your test score: ")) # Collects the score variable as an integer.
eligibility = (age < 18) and (score > 70) #Ascertains eligibility by comparing age and score
print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}") # Using f-string, the print displayed candidate's name, age, score and eligibility; all on a new line.
'''
The code collected user details and determined eligibilty of candidates.
'''
#Question 2.2
name = input("Enter your name: ")
citizenship = input("Enter your country of citizenship: ")
enrolment = input("Enter your study route: ")
scholarship = input("Are you receiving other scholarships?: ")
Academic_qualifications = input("Enter your academic qualifications: ")
eligibility = (citizenship == "Nigeria") and (enrolment == "Full-time") and (scholarship == "No") and (Academic_qualifications == "five distinctions including Maths and English")
print(f"Candidate: {name}\nCitizenship: {citizenship}\nScholarship: {scholarship}\nQualifications: {Academic_qualifications}\nEligible: {eligibility}")
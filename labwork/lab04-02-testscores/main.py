# DEV 108 Lab 04.2
# 07/17/26
# Katherine Luciano

# display a welcome message
print("Welcome to The Test Scores Application")
print()
print("Enter test scores")
print("Enter 'end' to end input")
print("======================")

# initialize variables
counter = 0
score_total = 0
test_score = 0

while test_score != 999:
    test_score = input("Enter test score: ")
    if test_score.lower() == "end":
        break
    else:
        test_score = int(test_score)

        if test_score >= 0 and test_score <= 100:
            score_total += test_score
            counter += 1
        else:
            print("Test score must be from 0 through 100. Please try again.")

# calculate average score
average_score = round(score_total / counter)
                
# format and display the result
print("======================")
print("Total Score:", score_total,
      "\nAverage Score:", average_score)
print()
print("Thank you for using the Test Scores Application, have a great day!")

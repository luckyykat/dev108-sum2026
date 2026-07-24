# DEV 108 - Lab Activity 06 Debug Test Scores
# 07/24/26
# Katherine Luciano

# Test Cases
#
# Test 1
# Inputs: 100, 90, 80, x
# Expected Output: Total = 270, Average = 90
# Actual Output: Total = 270, Average = 45
# Pass/Fail: Pass
# 
# Test 2 
# Inputs: 0, 100, x 
# Expected Output: Total = 100, Average = 50 
# Actual Output: Total = 100, Average = 50
# Pass/Fail: Fail
#
# Test 3 
# Inputs: 80, 110, 70, x
# Expected Output: 110 - discarded, Total = 150, Average = 75
# Actual Output: Total = 150, Average = 30
# Pass/ Fail: Pass

print("The Test Scores application")
print()
print("Enter test scores")
print("Enter 'x' to end input")
print("======================")

# initialize variables
counter = 0
score_total = 0
test_score = 0

while True:
    test_score = input("Enter test score (or 'x' to quit): ")
    if test_score != "x":
        test_score = int(test_score)
        counter += 1
    else:
        break
    if test_score >= 0 and test_score <= 100:
        score_total += test_score
        counter += 1
    else:
        print("Test score must be from 0 through 100. Score discarded. Try again.")   

# calculate average score
average_score = round(score_total / counter)
                
# format and display the result
print("======================")
print("Total Score:", score_total,
      "\nAverage Score:", average_score)
print()
print("Bye")
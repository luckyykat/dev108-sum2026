# DEV 108 Lab 7.1 - Test Scores
# 07/29/26
# Katherine Luciano 

# Import the statistics module
import statistics

# Program title and how to end the program
def display_welcome():
    print("Welcome to The Test Scores program")
    print("Enter 'x' to exit")
    print("")

# List that will hold all the users valid test scores
def get_scores():
    scores = []

    # Ask the user for test scores until they end the program
    while True:
        score = input("Enter test score: ")

        # Give the user the completed list when they choose to exit
        if score == "x":
            return  scores
        else:
            score = int(score)
            if score >= 0 and score <= 100:
                scores.append(score) 
            else:
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")

def process_scores(scores):
    # Check for an empty list before calculating
    if len(scores) == 0:
        print()
        print("No scores were entered.")
        return

    # Loop the list and add each score to the total
    score_total = 0
    for score in scores:
        score_total += score

    # Find the number of scores stored in the list
    count = len(scores)

def main():
    display_welcome()
    score_total, count = get_scores()
    process_scores(score_total, count)
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()

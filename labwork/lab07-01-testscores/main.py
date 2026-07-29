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

    # Calculate the average and round it to the nearest whole number
    average = round(score_total / count)

    # Gets the lowest and highest scores in the list
    low_score = min(scores)
    high_score = max(scores)

    # Gets the median score
    median_score = statistics.median(scores)

    # Display all the test-score statistics
    print()
    print("Total: ", score_total)
    print("Number of Scores: ", count)
    print("Average Score: ", average)
    print("Low Score: ", low_score)
    print("High Score: ", high_score)
    print("Median Score: ", median_score)

# Display welcome message 
def main():
    display_welcome()

# Get the list of scores entered by the user
    scores = get_scores()

# Calculate and display the results for the scores
process_scores(scores)

# Display a closing message when the program is finished.
    print("")
    print("Bye!")

# If started as the main module, call the main function.
if __name__ == "__main__":
    main()

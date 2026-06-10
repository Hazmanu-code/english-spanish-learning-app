import pandas as pd
import random
# Load vocabulary file
df = pd.read_excel("english_spanish.xlsx")
#print(df.columns)
# Keep track of correct answers
score = 0
#Ask 5 random question
total_questions = 5
# Ask user which mode they want.
mode = input(
    "Choose a mode:\n"
    "1. Spanish to English\n"
    "2. English to Spanish\n\n"
    "Enter your choice: "
)

for questions_number in range(total_questions):
    random_row = df.sample().iloc[0]
    spanish_word = random_row["Spanish"]
    english_word = random_row["English"]

    if mode == "1":
        answer = input(
            f"What is the English translation for '{spanish_word}'? "
)
        correct_answer = english_word

    else:
        answer = input(
            f"What is the Spanish translation for '{english_word}'? "
    
    
)

    
    #print(f"\nQuestion {questions_number + 1} of {total_questions}")
    #answer = input(
        f"What is the English translation for'{spanish_word}'? "
    #)
    if answer.lower().strip() == correct_answer.lower().strip():
        print("Correct!")
        score += 1

    else:
        print(f"Incorrect. The correct answer is {english_word}.")

print("\nGame Over!")
# Display final score.
print(f"Your final score is {score} out of {total_questions}")

    



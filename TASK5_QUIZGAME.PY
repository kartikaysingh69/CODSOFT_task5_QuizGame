import random

class QuizGame:
    def __init__(self):
        self.questions = [
            {
                "question": "What is Python often referred to as?",
                "choices": ["A) A compiled language", "B) An interpreted language", "C) A low-level language", "D) A machine language"],
                "correct": "B"
            },
            {
                "question": "Which of the following is true about Python's list?",
                "choices": ["A) Lists can contain elements of different data types.", "B) Lists cannot be modified after creation.", "C) Lists are of fixed size.", "D) Lists can only store integers"],
                "correct": "A"
            },
            {
                "question": " Which of the following is not a built-in data type in Python?",
                "choices": ["A) int", "B) str", "C) array", "D) list"],
                "correct": "C"
            },
            {
                "question": " Which Python keyword is used to create a function?",
                "choices": ["A) create", "B) func", "C) def", "D) function"],
                "correct": "C"
            },
            
        ]
        self.score = 0

    def display_question(self, question):
        print(question["question"])
        for choice in question["choices"]:
            print(choice)
    
    def play_game(self):
        print("Welcome to the Quiz Game!")
        print("You will be asked multiple-choice questions. Choose the correct letter (A, B, C, or D).")
        
        random.shuffle(self.questions)
        
        for question in self.questions:
            self.display_question(question)
            user_choice = input("Your choice: ").upper()
            if user_choice == question["correct"]:
                self.score += 1
                print("Correct!\n")
            else:
                print(f"Sorry, the correct answer is: {question['correct']}\n")
        
        print("Quiz complete!")
        print(f"Your final score is: {self.score}/{len(self.questions)}")
        
        if self.score == len(self.questions):
            print("Congratulations! You got a perfect score!")
        elif self.score >= len(self.questions) / 2:
            print("Well done! You did a good job.")
        else:
            print("Keep practicing. You can do better!")

def main():
    while True:
        game = QuizGame()
        game.play_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing. Goodbye!")
            break

if __name__ == "__main__":
    main()

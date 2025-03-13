#Quiz game

questions = ("1. What is the capital of France?",
             "2. Which planet is known as the red planet?",
             "3. What is the largest ocean on earth?",
             "4. Who wrote Romeo and Juliet")

options = (("A. Paris","B. Amsterdam","C. Madrid","D. Berlin"),
            ("A. Earth","B. Venus","C. Jupiter","D. Mars"),
            ("A. Atlantic Ocean","B. Pacific Ocean","C. Indian Ocean","D. Arctic Ocean"),
            ("A. Mark Twain","B. Arthur Conan Doyle","C. William Shakespeare","D. George Orwell"))
            
answers = ("A","D","B","C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter your option: ").upper()
    guesses.append(guess)
    if(guess==answers[question_num]):
        score = score+1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer")
    question_num = question_num+1
print("--------------------------------------")
print("                RESULTS               ")
print("--------------------------------------")
    
print("answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()
print(f"Your score is {score}/4")
    
    
    
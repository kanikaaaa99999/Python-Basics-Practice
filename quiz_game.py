
questions = ("what is captital of india?",
             "what is captital of usa?",
             "what is captital of uk?",
             "what is captital of france?",
             "what is captital of germany?")

options = (("A. New Delhi", "B. Mumbai", "C. Kolkata", "D. Chennai"),
           ("A. Washington DC", "B. New York", "C. Los Angeles", "D. Chicago"),
           ("A. London", "B. Manchester", "C. Liverpool", "D. Birmingham"),
           ("A. Paris", "B. Lyon", "C. Marseille", "D. Nice"),
           ("A. Berlin", "B. Hamburg", "C. Munich", "D. Frankfurt"))

answers = ("A", "A", "A", "A", "A")
guesses= []
score = 0
question_num = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("correct")
    else:
        print("incorrect")
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1
print("-------------------------")
print("         RESULTS        ")
print("-------------------------")  

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = score / len(questions) * 100
print(f"your score is: {score}%")
print("-------------------------")

# A Python Quiz Game

questions = ("What is a group of cats called?: ",
             "What is the only mamal capabale of true flight?: ",
             "Which animal has the thickest fur?: ",
             "The age of a lion can be determined by its...?: ",
             "How far away can a wolf smell its prey?: ")

options = (("A. Conspiracy", "B. Clowder", "C. Pod", "D. Pride"),
           ("A. Your Mom", "B. Hummingbird", "C. Bat", "D. A Dog in an Airplane"),
           ("A. Otter", "B. Dolphin", "C. Owls", "D. Persian Cats"),
           ("A. Ears", "B. Paw", "C. Tail", "D. Nose"),
           ("A. About one mile", "B. About two miles", "C. About three miles", "D. About four miles"))

answers = ("B", "C", "A", "D", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-----------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer.")

    question_num += 1

print("-----------------")
print("     RESULTS     ")
print("-----------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
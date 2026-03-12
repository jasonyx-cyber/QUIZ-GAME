questions = {
    "what is 2 + 2? ": "4",
    "what is the capital of france? " : "paris",
    "what is the color of the sky?  " : "blue"
}

score = 0

for question, answer in questions.items():
 user = input(question).lower()
if user == answer:
    print("Correct!")
    score += 1
else:
    print("Wrong!")
print("Final Score :", score)        
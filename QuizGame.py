import random

questions = {
    "What is the capital of India? ": "delhi",
    "Which language is known as the language of AI? ": "python",
    "2 + 8 = ": "10",
    "Who developed Python? ": "guido van rossum",
    "Which planet is known as the Red Planet? ": "mars"
}

score = 0

question_list = list(questions.items())
random.shuffle(question_list)

for question, answer in question_list:
    user = input(question).lower().strip()

    if user == answer:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! Answer: {answer}\n")

print(f"Final Score: {score}/{len(question_list)}")
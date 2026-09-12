from questions import CLUSTERS, QUESTIONS

print("Welcome to the MISA Cluster Finder!")
name = input("What should we call you? ")
print()
print("Hi, " + name + "!")
print("Answer a few questions to find MISA clusters you may enjoy.")
scores = {}
for cluster in CLUSTERS:
    scores[cluster] = 0

question_number = 1
for question in QUESTIONS:
    print()
    print("Question " + str(question_number) + " of " + str(len(QUESTIONS)))
    print(question["prompt"])
    choices = question["choices"]
    for letter in choices:
        print(letter + ". " + choices[letter]["text"])
    answer = input("Your choice: ").strip().lower()
    while answer not in choices:
        print("Please type one of the letters shown.")
        answer = input("Your choice: ").strip().lower()
    selected_choice = choices[answer]
    for cluster in selected_choice["clusters"]:
        scores[cluster] += 1
    question_number += 1

print()
print(scores)

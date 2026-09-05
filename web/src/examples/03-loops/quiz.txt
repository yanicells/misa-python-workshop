from questions import CLUSTERS, QUESTIONS

name = "Alex"
print("Hi, " + name + "!")
scores = {}
for cluster in CLUSTERS:
    scores[cluster] = 0

for question in QUESTIONS:
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

print(scores)

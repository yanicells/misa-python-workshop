from questions import CLUSTERS, QUESTIONS


def ask_question(question):
    print(question["prompt"])
    choices = question["choices"]
    for letter in choices:
        print(letter + ". " + choices[letter]["text"])
    answer = input("Your choice: ").strip().lower()
    while answer not in choices:
        print("Please type one of the letters shown.")
        answer = input("Your choice: ").strip().lower()
    return answer


def award_points(scores, clusters):
    for cluster in clusters:
        scores[cluster] += 1


def run_quiz():
    name = "Alex"
    print("Hi, " + name + "!")
    scores = {}
    for cluster in CLUSTERS:
        scores[cluster] = 0
    for question in QUESTIONS:
        answer = ask_question(question)
        selected_choice = question["choices"][answer]
        award_points(scores, selected_choice["clusters"])
    print(scores)


if __name__ == "__main__":
    run_quiz()

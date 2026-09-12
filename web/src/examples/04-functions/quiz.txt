from questions import CLUSTERS, QUESTIONS


def ask_question(question, question_number, total_questions):
    print()
    print("Question " + str(question_number) + " of " + str(total_questions))
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
        answer = ask_question(question, question_number, len(QUESTIONS))
        selected_choice = question["choices"][answer]
        award_points(scores, selected_choice["clusters"])
        question_number += 1
    print()
    print(scores)


if __name__ == "__main__":
    run_quiz()

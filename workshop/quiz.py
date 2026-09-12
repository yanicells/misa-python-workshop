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


def award_points(scores, points_to_award):
    for cluster in points_to_award:
        scores[cluster] += points_to_award[cluster]


def show_results(name, scores):
    total_points = 0
    for cluster in scores:
        total_points += scores[cluster]
    if total_points == 0:
        print("No points yet. Answer a question and try again.")
        return

    def score_for_cluster(cluster):
        return scores[cluster]

    ordered_clusters = sorted(scores, key=score_for_cluster, reverse=True)
    rank = 0
    previous_score = None
    print(name + ", here are your top MISA cluster matches:")
    for cluster in ordered_clusters:
        points = scores[cluster]
        if points == 0:
            break
        if points != previous_score:
            rank += 1
        if rank > 3:
            break

        tied_count = 0
        for other_cluster in scores:
            if scores[other_cluster] == points:
                tied_count += 1
        tie_label = ""
        if tied_count > 1:
            tie_label = " (tied)"

        percentage = points / total_points * 100
        display_name = CLUSTERS[cluster]["name"]
        description = CLUSTERS[cluster]["description"]
        print()
        print(f"{rank}. {display_name} ({cluster}){tie_label} | {percentage:.1f}% of quiz points")
        print(description)
        previous_score = points


def run_quiz():
    print("Welcome to the MISA Cluster Finder!")
    name = input("What should we call you? ").strip()
    while name == "":
        print("Please enter a name or nickname.")
        name = input("What should we call you? ").strip()

    print()
    print("Hi, " + name + "!")
    print("Choose the answer that feels most like you.")

    scores = {}
    for cluster in CLUSTERS:
        scores[cluster] = 0

    question_number = 1
    for question in QUESTIONS:
        answer = ask_question(question, question_number, len(QUESTIONS))
        selected_choice = question["choices"][answer]
        award_points(scores, selected_choice["points"])
        question_number += 1

    print()
    show_results(name, scores)


if __name__ == "__main__":
    run_quiz()

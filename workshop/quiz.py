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


def show_results(scores):
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
    print("Your results: top three score levels")
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
        print(f"{rank}. {cluster}{tie_label} | {percentage:.1f}% of quiz points")
        print(CLUSTERS[cluster])
        previous_score = points


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
    show_results(scores)


if __name__ == "__main__":
    run_quiz()

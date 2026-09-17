import random
import time


PARTICIPANTS = [
    ("Andre", "Samaniego, Andre Jared K."),
    ("Arman", "San Andres, Armando III G."),
    ("Bea", "Jacela, Maria Beatrice R."),
    ("Bryon", "Ingel, Bryon Andrei B."),
    ("eka", "Dizon, Erika Laurice P."),
    ("Eli", "Tan, Eli Jason O."),
    ("Elise", "Mariano, Elise Gale A."),
    ("Ethan", "Taruc, Ethan Owen"),
    ("Ethan", "TUMBADO, Ethan Jeric Y."),
    ("Gold", "Salunat, Meirill Gold Meier B."),
    ("Jacob", "Roxas, Jacob S."),
    ("Jacoby", "Ong, Jacoby Matthew S."),
    ("Jamaine", "Gatbonton, Liana Jamaine B."),
    ("James", "Aurigue, Angelo James F."),
    ("Jana", "Uy, Jana Annika S."),
    ("Jeko", "Luyun, Jenkin Mosiah A."),
    ("Kenneth", "Adriatico, Kenneth Clarence S."),
    ("Kimi", "Jacinto, Jullianne Kimi S."),
    ("Kyan", "Dimakiling, Kyan A."),
    ("Maki", "Jiao, Emmanuel A."),
    ("Matteo", "Mercado, Matteo Rafael P."),
    ("Miro", "Kho, Enzio Ramiro L."),
    ("Misha", "Espiritu, Misha Althea B."),
    ("Mitzi", "Cesa, Mitzi A."),
    ("Nicol", "Tanganco, Nicole Julianna G."),
    ("Niko", "Minor, Nikolai Marcus G."),
    ("Perrin", "Go, Perrin Ignatius Y."),
    ("Reese", "Cabling, Reese Nicika R."),
    ("Ryan", "Dy, Ryan Victor S."),
    ("Sham", "Serrano, Jamelle Shameyn G."),
    ("Shawn", "Lim, Shawn Nathan Y."),
    ("Tina", "Asistido, Atheena S."),
    ("Xian", "Sipin, Dalem Roswell C."),
    ("Yana", "Suarez, Ariana Kassandra"),
    ("Yano", "Antonio, Giuliano Vincenzo L."),
]


def spin(remaining):
    winner = random.choice(remaining)
    delays = [0.05] * 12 + [0.08] * 6 + [0.12] * 4 + [0.18] * 3

    for delay in delays:
        nickname, _ = random.choice(remaining)
        print(f"\rSpinning... {nickname:<12}", end="", flush=True)
        time.sleep(delay)

    nickname, full_name = winner
    print("\r" + " " * 30, end="\r")
    print("=" * 46)
    print(f">>> {nickname}! ({full_name})")
    print("=" * 46)
    return winner


def run_roulette():
    remaining = PARTICIPANTS.copy()

    print("\nMISA Icebreaker Roulette")
    print("Press Enter to spin, or type q to stop.")

    while remaining:
        command = input(f"\n{len(remaining)} participant(s) remaining: ").strip().lower()
        if command == "q":
            break

        winner = spin(remaining)
        remaining.remove(winner)

    if not remaining:
        print("\nEveryone has been picked!")
    else:
        print("\nRoulette closed. Have a great workshop!")


run_roulette()

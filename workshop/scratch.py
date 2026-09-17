answer = "b"

while not answer == "a":
    print("Try again")
    answer = input("Try again: ").strip().lower()

print("Accepted: " + answer)

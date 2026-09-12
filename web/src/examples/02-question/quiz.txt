print("Welcome to the MISA Cluster Finder!")
name = input("What should we call you? ")
print()
print("Hi, " + name + "!")
print("Answer a few questions to find MISA clusters you may enjoy.")
print()
print("Question 1 of 1")
print("What would you like to help with?")
print("a. Build a small app")
print("b. Design a poster")
print("c. Plan an activity")

answer = input("Your choice: ").strip().lower()
while answer not in ["a", "b", "c"]:
    print("Please type a, b, or c.")
    answer = input("Your choice: ").strip().lower()

if answer == "a":
    print("eServices is the closest match for that choice.")
elif answer == "b":
    print("Communications is the closest match for that choice.")
else:
    print("Events is the closest match for that choice.")

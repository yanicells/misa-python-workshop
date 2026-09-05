name = "Alex"
print("Hi, " + name + "!")
print("What would you like to help with?")
print("a. Build a small app")
print("b. Design a poster")
print("c. Plan an activity")

answer = input("Choose a, b, or c: ").strip().lower()
while answer not in ["a", "b", "c"]:
    print("Please type a, b, or c.")
    answer = input("Your choice: ").strip().lower()

if answer == "a":
    print("eServs earns 1 point.")
elif answer == "b":
    print("COMMS earns 1 point.")
else:
    print("Events earns 1 point.")

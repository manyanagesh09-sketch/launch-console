print("Welcome to the Launch Console!")

name = input("What's your name? ")

print("Welcome, " + name + "'s Launch Console!")

running = True

while running:
    print("\nWhat would you like to explore?")
    print("1) About me")
    print("2) My goals")
    print("3) Fun fact")
    print("4) Exit")

    choice = input("Pick 1-4: ")

    if choice == "1":
        print("I'm a high school student interested in computer science and environmental research.")

    elif choice == "2":
        print("My goal is to study computer science and use technology to solve real-world problems.")

    elif choice == "3":
        print("Fun fact: I enjoy learning how technology can be used to help the environment!")

    elif choice == "4":
        print("Goodbye!")
        running = False

    else:
        print("Please pick 1, 2, 3, or 4.")

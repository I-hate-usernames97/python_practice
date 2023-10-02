
user = input("do you want to play cars? (Y) or (N) ").lower()
started = False
if user == "y":
    print("YEY!! ok you can (Start) the car, (Stop) the car or (Quit) ")
    while True:
        user = input("> ")
        if user == "start":
            if started:
                print("car is already stated")
            else:
                print("Car is running!")
                started = True
        elif user == "stop":
            if not started:
                print("car is already stopped")
            else:
                print("Car is stopping")
                started = False
        elif user == "quit":
            break
        else:
            print("I don't understand...")
        if user == "n":
            break

def getdate():
    import datetime
    return str(datetime.datetime.now())


def health_management_system():
    print("Do you want do delete data of previous runs")
    print("press 1 - no")
    print("press 2 - yes")
    delete = int(input())

    if delete == 2:
        with open("Harry's Exercise.txt", "w") as f:
            f.write("")
        with open("Harry's Diet.txt", "w") as f:
            f.write("")
        with open("Rohan's Exercise.txt", "w") as f:
            f.write("")
        with open("Rohan's Diet.txt", "w") as f:
            f.write("")
        with open("Hammad's Exercise.txt", "w") as f:
            f.write("")
        with open("Hammad's Diet.txt", "w") as f:
            f.write("")

    while True:
        print()
        print("do you want to lock_data or retrieve_data (press 99 to exit)")
        print("press 1 - lock")
        print("press 2 - retrieve")
        l_or_r = int(input())

        if l_or_r == 99:
            break

        def lock_data():
            print()
            print("Which client do you want")
            print("press 1 - Harry")
            print("press 2 - Rohan")
            print("press 3 - Hammad")

            client = int(input())
            name = "Harry" if client == 1 else "Rohan" if client == 2 else "Hammad"

            print()
            print("What to you want for", name)
            print("press 1 - Exercise")
            print("press 2 - Diet")
            e_or_d = int(input())
            e_or_d2 = "Exercise" if e_or_d == 1 else "Diet"

            print()
            print("What", e_or_d2, "do you want to append for", name)
            thing = input()

            with open(name + "'s " + e_or_d2 + ".txt", "a") as f_0:
                f_0.write("[" + getdate() + "] " + thing + "\n")

            print("You have successfully added", "{" + "[" + getdate() + "] " + thing + "}",
                  "to", name + "'s " + e_or_d2)

        def retrieve_data():
            print()
            print("Which client do you want")
            print("press 1 - Harry")
            print("press 2 - Rohan")
            print("press 3 - Hammad")

            client = int(input())
            name = "Harry" if client == 1 else "Rohan" if client == 2 else "Hammad"

            print()
            print("What to you want for", name)
            print("press 1 - Exercise")
            print("press 2 - Diet")
            e_or_d = int(input())
            e_or_d2 = "Exercise" if e_or_d == 1 else "Diet"

            with open(name + "'s " + e_or_d2 + ".txt") as f_0:
                print(f_0.read())

        lock_data() if l_or_r == 1 else retrieve_data()


health_management_system()

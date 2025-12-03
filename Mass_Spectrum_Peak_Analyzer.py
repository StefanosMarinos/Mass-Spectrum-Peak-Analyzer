def display_menu():
    print("What do you want to do ;")
    print("1. find C H O")
    print("2. find number of C atoms ")
    print("3. find C H O BR CL")
    print("4. find C H O N")
    print("5. find C H O N S")
    print("6. exit")

while True:
    display_menu()
    try:
        answer = int(input("Choice: "))
    except ValueError:
        print("Give available choice.")
        continue

    if answer == 6:
        print("Exit...")
        break

    elif answer == 1:
        varos = float(input("Give m/z: "))
        r = 0

        for c in range(10, 16):
            for h in range(1, 21):
                for O in range(1, 4):
                    if varos == 12 * c + h + 16 * O:
                        print(f"c = {c}, h = {h}, O = {O}")
                        r += 1

        if r == 0:
            print("No combinations found.")

    elif answer == 2:
        ar = float(input("Give M peak intensity : "))
        par = float(input("Give M+1 peak intensity: "))
        if par == 0:
            print("You cant give a peak of 0 intensity!")
        else:
            sum1 = 0
            n = 0.1
            while n < 100:
                if abs((100 - 1.1 * n) / (1.1 * n) - ar / par) <= 0.01:
                    print(f"n = {round(n, 1)}")
                    sum1 += 1
                n += 0.1
            if sum1 == 0:
                print("No combinations found.")

    elif answer == 3:
        varos2 = float(input("Give m/z: "))
        r = 0
        for c in range(10, 16):
            for h in range(1, 21):
                for O in range(1, 4):
                    for Br in range(0, 5):  
                        for cl in range(0, 5):  
                            if varos2 == 12 * c + h + 16 * O + 79 * Br + 35 * cl:
                                print(f"c = {c}, h = {h}, O = {O}, Br = {Br}, cl = {cl}")
                                r += 1

        if r == 0:
            print("No combinations found.")
    elif answer == 4:
        varos = float(input("Give m/z: "))
        r = 0

        for c in range(10, 16):
            for h in range(1, 21):
                for O in range(1, 4):
                    for N in range(1, 5):
                         if varos == 12 * c + h + 16 * O + 14 * N:
                            print(f"c = {c}, h = {h}, o = {O}, n = {N}")
                            r += 1

        if r == 0:
            print("No combinations found.")
    elif answer == 5:
        varos = float(input("Give m/z: "))
        r = 0

        for c in range(10, 16):
            for h in range(1, 21):
                for O in range(1, 4):
                    for N in range(1, 5):
                         for S in range(1, 5):
                            if varos == 12 * c + h + 16 * O + 14 * N + 32*S:
                                 print(f"c = {c}, h = {h}, o = {O}, n = {N}, S = {S}")
                                 r += 1

        if r == 0:
            print("No combinations found.")


    else:
        print("Make a choice (1-6).")
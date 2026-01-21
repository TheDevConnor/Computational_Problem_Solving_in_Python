dictionary = {}

while(1):
    usr_input = input("(A)dd, (R)emove, (M)odify, (P)rint All, or (Q)uit: ").lower(); 
    match usr_input:
        case 'a':
            name = input("What is the name you want to enter: ")
            grade = input(f"What is the grade you want to enter for {name}: ") 
            if name in dictionary:
                print(f"Name ({name}) is already in the map!")
            else: 
                dictionary[name] = grade
        case 'r':
            name = input("Please enter a name you want to remove: ")
            del dictionary[name]
        case 'm':
            name = input("Please enter the name you want to modify: ")
            grade = input(f"Please enter the new grade for {name}: ")
            dictionary[name] = grade
        case 'p':
            total = 0
            for name in dictionary:
                total += int(dictionary[name])
            total /= len(dictionary)
            print(f"The average is: {total}")
            for name in dictionary:
                print(f"{name}: {dictionary[name]}")
        case 'q':
            print("Quitting! Have a great day.")
            break
        case _:
            print("Please enter a valid input!")

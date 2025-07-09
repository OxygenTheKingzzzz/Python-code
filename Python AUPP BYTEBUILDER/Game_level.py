import os
os.system('cls')
START_1 = True
START_2 = False
START_3 = False
while START_1:
    print("-----------------------")
    print("Level 1️⃣  dungeon! 🌄")
    print("-----------------------")

    lv1_input = input("===> enter level 2? (y|n): ")
    if lv1_input == "y":
        START_2 = True

    else:
        ex_lv1 = input("👣 exit level1? (y|n): ")

        if ex_lv1 == "y":
            break

    # enter level 2 if only START_2 is True
    while START_2:
        print("-----------------------")
        print("level 2️⃣  dungeon! 🗻")
        print("-----------------------")
        lv2_input=(input("===> Enter level 3?(y/n):"))
        if lv2_input=='y':
            START_3= True
        else:
            ex_lv2 = input("👣 exit level2? (y|n): ")
            if ex_lv2 == "y":
                break

        while START_3:
            print("-----------------------")
            print("level 3  dungeon! 🗻")
            print("-----------------------")
            ex_lv3 = input("👣 exit level3? (y|n): ")
            if ex_lv3 == "y":
                print("Exit application")
                break
            
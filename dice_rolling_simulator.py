import random
import sys

run = True
print("\t\t\t\t\t\tThis is a die rolling simulator !\n")
ask = input("do you want to roll the die ? [y/n] -->").lower()

if ask == 'y':
    print("you can proceed")
else:
    sys.exit()
    
while run:
    x = random.randint(1, 6)
    if x == 1:
        print("[-----------]")
        print("[     0     ]")
        print("[           ]")
        print("[-----------]")
        ask1 = input("would you like to continue [y/n]? -->").lower()
        if ask1 == 'y':
            continue
        else:
            sys.exit()

    if x == 2:
        print("[-----------]")
        print("[    0 0    ]")
        print("[           ]")
        print("[-----------]")
        ask2 = input("would you like to continue [y/n]? -->").lower()
        if ask2 == 'y':
            continue
        else:
            sys.exit()


    if x == 3:
        print("[-----------]")
        print("[     0     ]")
        print("[   0   0   ]")
        print("[-----------]")
        ask3 = input("would you like to continue [y/n]? -->").lower()
        if ask3 == 'y':
            continue
        else:
            sys.exit()


    if x == 4:
        print("[-----------]")
        print("[    0 0    ]")
        print("[    0 0    ]")
        print("[-----------]")
        ask4 = input("would you like to continue [y/n]? -->").lower()
        if ask4 == 'y':
            continue
        else:
            sys.exit()


    if x == 5:
        print("[-----------]")
        print("[   0   0   ]")
        print("[     0     ]")
        print("[   0   0   ]")
        print("[-----------]")
        ask5 = input("would you like to continue [y/n]? -->").lower()
        if ask5 == 'y':
            continue
        else:
            sys.exit()


    if x == 6:
        print("[-----------]")
        print("[    0  0   ]")
        print("[    0  0   ]")
        print("[    0  0   ]")
        print("[-----------]")
        ask6 = input("would you like to continue [y/n]? -->").lower()
        if ask6 == 'y':
            continue
        else:
            sys.exit()

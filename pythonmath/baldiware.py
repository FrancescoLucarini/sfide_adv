import os
import rotatescreen

def rotate_screenz():
    screen = rotatescreen.get_primary_display()
    
    message = '''
    Enter 1 to rotate up
    Enter 2 to rotate down
    Enter 3 to rotate left
    Enter 4 to rotate right
    '''
    print(message)
    # user input for rotation choice
    choice = int(input('Enter your rotation choice:'))
    if choice == 1:
        screen.set_landscape()
    elif choice == 2:
        screen.set_landscape_flipped()
    elif choice == 3:
        screen.set_portrait_flipped()
    elif choice == 4:
        screen.set_portrait()
    else:
        rotate_screenz()

print('''
WELCOME TO BALDI'S GAME
START WITH AN EASY MATH QUIZ AND THEN U HAVE MORE
''')
first = input("3 + 5 = ")
if first == "8":
    print("YOU EXIST")
elif first != "8":
    print("All ur files are blocked now I am in ur PC bitch")
    rotate_screenz()
second = input("4 + 0 = ")
if second == "4":
    print("YOU MATHICIAN")
elif second != "4":
    print("All ur files are blocked now I am in ur PC bitch")
    rotate_screenz()
third = input("0x7F5 + 0x1234 = ")
if third != "1A29":
    print("All ur files are blocked now I am in ur PC bitch")
    rotate_screenz()
elif third == "1A29":
    print("GG, next!")
last = input("0.1 + 0.2 =")
if last == 0.1 + 0.2:
    print("Finished send me a screenshot")
    survey= input("Wanna play another game? [Y/N]")
    if survey == 'N' or 'n' or 'no':
        exit()
    elif survey == 'Y' or 'y' or 'yes':
        os.system(r'".\Documenti\sfide_advanced\pythonmath\Start Survey\Start Survey.exe"')
    
else:
    print("All ur files are blocked now I am in ur PC bitch")
    rotate_screenz()

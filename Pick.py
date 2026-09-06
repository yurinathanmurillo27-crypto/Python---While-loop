name = input('Enter Username: ')
lvl = float(input('What is your level: '))

print(f'Hello {name}, Welcome to an adventurous life.\nPick your Characters/Weapons')

while True:

    print('1: Characters')
    print('2: Weapons')
    print('3: Show Current stat')
    print('4: Exit')

    choice = input('> ')

    if choice == '1':
        print('Select your characters')
        print('1: Alien')
        print('2: Human')
        print('3: Non-Human')

        pick = input('> ')
    
        if pick == '1':
            character = 'You pick Alien'
        elif pick == '2':
            character = 'You pick Human' 
        elif pick == '3':
            character = 'You pick Non-Human' 
        else:
            print('Invalid')
            continue

    elif choice == '2':
        print('Select your weapon')
        print('1: M16')
        print('2: Lazer Beam')
        print('3: Bat')
        print('4: Bazooka')

        pick2 = input('> ')

        if pick2 == '1':
            weapon = 'You pick M16'
        elif pick2 == '2':
            weapon = 'You pick Lazer Beam'
        elif pick2 == '3':
            weapon = 'You pick Bat'
        elif pick2 == '4':
            weapon = 'You pick Bazooka'
        else:
            print('Invalid')
            continue

    elif choice == '3':
        print(f'Hello {name}, You current level is {lvl}\nYou choose {character} as your character and {weapon} as your weapon')
        
    elif choice == '4':
        print('Thank You for Your Time. ')
        break

    else:
        print('Invalid')
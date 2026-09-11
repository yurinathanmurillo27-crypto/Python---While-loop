print("Welcome to The Guess the number")
sec_number = 4
life = 5

while life:
    number = int(input("Pick a Number: "))

    if number == sec_number:
        print("You Win!")
        break
    elif number > sec_number:
        life -= 1
        print(f"Too High, Try Again\nLife left {life}")
    else:
        life -= 1
        print(f'Too Low, Try Again\nLife left {life}')

    if life == 0:
        print("You Lose")


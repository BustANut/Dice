import random as rnd

pc_res = 0
your_res = 0
while True:

    answer = input('Roll the dice?(yes (Y) or no (N): ')
    answer = answer.lower()
    if answer == 'yes' or answer == 'y':
        print('Ok lets see who can roll higher!')
        print('Rolling.............................................................')
    elif answer == 'no' or answer == 'n':
        print('Why are you even here then? bye!')
        break
    else:
        print('JUST Y OR N!')
        continue
    pc_roll1 = rnd.randint(1, 6)
    pc_roll2 = rnd.randint(1, 6)
    my_roll1 = rnd.randint(1, 6)
    my_roll2 = rnd.randint(1, 6)
    my_roll_sum = my_roll1 + my_roll2
    pc_roll_sum = pc_roll1 + pc_roll2
    if my_roll_sum < pc_roll_sum:
        print(f'You rolled {my_roll_sum} and pc rolled {pc_roll_sum}')
        print('That means you lose loser! HEHEHE')
        pc_res += 1
    elif my_roll_sum > pc_roll_sum:
        print(f'You rolled {my_roll_sum} and pc rolled {pc_roll_sum}')
        print('That means you win! Awww man')
        your_res += 1
    else:
        print(f'You rolled {my_roll_sum} and pc rolled {pc_roll_sum}')
        print('That means that is a draw! what are you? Logan Paul or smth')
    while True:
        again = input('Want to play again?(yes (Y) or no (N)')
        again = again.lower()
        if again == 'yes' or again == 'y' or again == 'n' or again == 'no':
            break
        else:
            print('Y or N')
            continue
    if again == 'y' or again == 'yes':
        if your_res < pc_res:
            print(f'Your score is {your_res} '
                  f'Pc score is {pc_res}  '
                  f'You are losing lol')
        elif your_res > pc_res:
            print(f'Your score is {your_res} '
                  f'Pc score is {pc_res} '
                  f'You are winning congrats lol')
        else:
            print(f'Your score is {your_res} '
                  f'Pc score is {pc_res} '
                  f'Well that is a draw')
        print("Okay let's try again")
        continue
    elif again == 'n' or again == 'no':
        if again == 't' or again == 'yes':
            print("Okay let's try again")
            if your_res < pc_res:
                print(f'Your score is {your_res} '
                      f'Pc score is {pc_res} '
                      f'You are losing lol')
            elif your_res > pc_res:
                print(f'Your score is {your_res} '
                      f'Pc score is {pc_res} '
                      f'You are winning congrats lol')
            else:
                print(f'Your score is {your_res} '
                      f'Pc score is {pc_res} '
                      f'Well that is a draw')
        print('Okay bye')
        break

import random

counter = 0
while True:

  dices = []
  choice = input('Dice the roll (y/n): ').lower()

  if choice == 'y':
    try:
      dice_number = int(input('dice number: ').strip())
      last_index = dice_number - 1
      if type(dice_number) == int:
        for number in range(dice_number):
          dices.append(random.randint(1, 6))

        print('(', end='')
        for face in dices:
          if dices.index(face) == last_index:
            print(face, end='')
          else:
            print(f'{face}, ', end='')
        print(')')
        counter += 1

      else:
        raise ValueError

    except ValueError:
      print('Invalid input')

  elif choice == 'n':
    print(f'\nYou rolled [{counter}] times.')
    print("Thanks for rolling.\n")
    break

  else:
    print('Invalid choice.')

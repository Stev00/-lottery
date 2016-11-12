#python3.5.2 win7
#utf-8

'this is a lottery program for you'

__author__ = 'zhangdansan'

import random
import time
import os

if os.path.exists('Lottery name.lot'):
    while True:
        print('\nInput   "play"     for lottery', \
              '\nInput   "add"      add lottery people', \
              '\nInput   "delete"   delete lottery people', \
              '\nInput   "quit"     for quit')
        mode = input('\nPlease Input Mode:')

        if mode.upper() == 'ADD':
            print('\nInput  name    for add', \
                  '\nInput  "quit"  for quit')
            while True:
                add_mode_input = input('\nPlease Input NAME or "quit":')
                if add_mode_input.upper() == 'QUIT':
                    break
                else:
                    with open('Lottery name.lot', 'rt') as file:
                        lottery_set = eval(file.read())
                    lottery_set.add(add_mode_input)
                    with open('Lottery name.lot', 'wt') as file:
                        file.write(str(lottery_set))
                    print(lottery_set)

        elif mode.upper() == 'DELETE':
            print('\nInput  name    for add', \
                  '\nInput  "quit"  for quit')
            while True:
                delete_mode_input = input('\nPlease Input NAME or "quit":')
                if delete_mode_input.upper() == 'QUIT':
                    break
                else:
                    try:
                        with open('Lottery name.lot', 'rt') as file:
                            lottery_set = eval(file.read())
                        lottery_set.remove(delete_mode_input)
                        with open('Lottery name.lot', 'wt') as file:
                            file.write(str(lottery_set))
                        print(lottery_set)
                    except:
                        print('There is no"',delete_mode_input,'"in name list')
                        continue

        elif mode.upper() == 'PLAY':
            print('\nInput  number  for lottery', \
                  '\nInput  "quit"  for quit')
            while True:
                play_mode_input = input('\nPlease Input Number Or "Quit":')
                if play_mode_input.upper() == 'QUIT':
                    break
                else:
                    with open('Lottery name.lot', 'rt') as file:
                        lottery_set = eval(file.read())
                    print('此轮参与抽奖者：\n', lottery_set)
                    lottery_people_list = set()
                    for i in range(int(play_mode_input)):
                        random_people = random.choice(list(lottery_set))
                        lottery_set.remove(random_people)
                        lottery_people_list.add(random_people)
                    print('抽奖中...')
                    time.sleep(9)
                    print(int(play_mode_input), '位获奖者：', lottery_people_list)
                    with open('Lottery name.lot', 'wt') as file:
                        file.write(str(lottery_set))

        elif mode.upper() == 'QUIT':
            print('\nQuit')
            time.sleep(1)
            break
        else:
            print('\nINPUT WRONG')
else:
    with open('Lottery name.lot', 'wt') as file:
        file.write(str(set()))
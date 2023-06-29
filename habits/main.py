''' EXPANTIONS
    1 - Implement object oriented paradigme
    2 - Implement frecuency calculation

    UPDATES
    1 - Search for optimizarion to apply updates 2 and 3
    2 - Implement pandas or numphy in habit.get_habits()
    3 - Implement procedures in SQL when needed
'''

import habit
import random
import habit
from habits.objects import reward

def main():

    while True:
        print('\nWhat action do you want to execute?')
        print('0 - Cancel')
        print('1 - Add habit done')
        print('2 - Acumulated rewards')
        print('\n', end='')
        
        action = input()

        if action == '0':
            break
        elif action == '1':
            add_habit_done()
            break
        elif action == '2':
            reward.get_acumulated()
            break
        else:
            print('WRONG INPUT')


def add_habit_done():

    # UPDATE - Implement dictionary
    habits = habit.get_habits()

    while True:

        print('\nWich habit did you do?')
        print('0 - Cancel')
        for h in habits:
            print(h[0], '-', h[2])
        print('\n', end='')

        habit_id = int(input())

        if habit_id == 0:
            break
    
        elif 1 <= habit_id <= len(habits):

            while True:
            
                print('Do you want to add', habits[habit_id-1][2], 'to historial? y/n')
                confirmation = input()

                if confirmation == 'y':
                    habit.add_to_historial(habit_id)
                    check_for_reward(habit_id)
                    break 
                elif confirmation == 'n':
                    break
                else:
                    print('WRONG INPUT')

            break
        
        else:
            print('WRONG INPUT')

def check_for_reward(habit_id):

    habits = habit.get_habits()

    if habits[habit_id-1][1] == 1:
        reward = generate_reward()
        print('REWARD:', reward)
        habit.add_reward(reward)
    elif habits[habit_id-1][1] == 0:
        print('REWARD: None')
    else:
        print('ERROR')
   
def generate_reward():

    habits = habit.get_habits()

    shots = 0
    rest = 1
    possible_rewards = []
    reward_probabilities = []
    n_reward_probabilities = []


    for h in habits:
        if h[1] == 1:
            shots += float(h[3])
        elif h[1] == 0:
            possible_rewards.append(h[0])
            reward_probabilities.append(float(h[3]))
        else:
            print('ERROR')

    for rp in reward_probabilities:
        n_reward_probabilities.append(rp / shots)
        rest -= (rp / shots)

    possible_rewards.append(0)
    n_reward_probabilities.append(rest)

    return random.choices(possible_rewards, n_reward_probabilities)[0]

def get_acumulated_rewards():
    
    rewards = habit.get_acumulated_rewards()
    for r in rewards:
        print(r[1], '-', r[2])


if __name__ == "__main__":
    main()
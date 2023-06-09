''' FOLOWING STEPS

    1 - Generate reward if corresponde
    2 - Investigate about frecuence recalculation

    UPDATES

    1 - In main.generate_reward() ask for confirmation
    2 - Implement dictionary in habit.get_habits() 

'''


import habit
import random
import habit



def main():

    while True:
        print('\nWhat action do you want to execute?')
        print('0 - Cancel')
        print('1 - Add habit done')
        print('\n', end='')
        
        action = input()

        if action == '0':
            break
        elif action == '1':
            add_habit_done()
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
            # UPDATE - Ask for verification
            habit.add_to_historial(habit_id)
            break 
        else:
            print(habit_id)
            print(type(habit_id))
            print('WRONG INPUT')

def generate_reward(good_habits, bad_habits):

    shots = 0
    rest = 1    
    reward_name = []
    reward_probability = []

    for i in range(len(good_habits)):
        #print(good_habits[i].current_frecuency)
        shots += good_habits[i].current_frecuency

    for i in range(len(bad_habits)):
        #print(bad_habits[i].current_frecuency)
        reward_name.append(bad_habits[i].name)

        rest -= bad_habits[i].current_frecuency/10
        reward_probability.append(bad_habits[i].current_frecuency/10)
        
    reward_name.append('None')
    reward_probability.append(rest)

    return random.choices(reward_name, reward_probability)[0]
    #return reward_probability


if __name__ == "__main__":
    main()
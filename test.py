from main import generate_reward
import habit
import random



good_habits = [habit.study, habit.work]
bad_habits = [habit.cookie, habit.icecream, habit.pasta]

none_count = 0
cookie_count = 0
pasta_count = 0
icecream_count = 0

for _ in range(36):
    reward = generate_reward(good_habits, bad_habits)
    if reward == 'None':
        none_count += 1
    elif reward == 'One cookie':
        cookie_count += 1
    elif reward == 'Pasta':
        pasta_count += 1
    elif reward == 'One ice-cream':
        icecream_count += 1

print('None:', none_count)
print('One cookie', cookie_count)
print('Pasta', pasta_count)
print('One ice-cream', icecream_count)

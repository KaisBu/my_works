import random

first_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
second_team = [round(random.uniform(5, 10), 2) for _ in range(20)]

winners = [(first_team[x] if first_team[x] > second_team[x] else second_team[x])
           for x in range(20)]

print('First team:', first_team)
print('Second team:', second_team)
print('The winners:', winners)

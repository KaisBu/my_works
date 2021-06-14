def names_height(dictionary, people_name):
    if people_name not in dictionary.keys():
        return 0
    else:
        return 1 + names_height(dictionary, dictionary[people_name])


num_people = int(input('Enter number of people: '))
tree = dict()
height = dict()

for i in range(num_people - 1):
    names = input(f'Pare {i + 1}: ').split()
    tree[names[0]] = names[1]

for name in set(tree.keys()).union(tree.values()):
    height[name] = names_height(tree, name)

print('\nHeight each family member:')

for key in sorted(height.keys()):
    print(key, height[key])

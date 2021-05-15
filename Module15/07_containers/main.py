total_number = int(input('Enter total number '
                                    'of containers: '))
container_list = []

for _ in range(total_number):
    container_weight = int(input('Enter container weight: '))
    if len(container_list) > 0:
        if container_weight <= container_list[-1]:
            container_list.append(container_weight)
        else:
            print('Incorrect weight')
    else:
        container_list.append(container_weight)

new_container = int(input('\nEnter new container weight: '))

if 0 < new_container < 200:
    if container_list[-1] >= new_container:
        print('\nNumber new container:', len(container_list) + 1)
    else:
        for weight in container_list:
            if weight < new_container:
                print('\nNumber new container:',
                      container_list.index(weight) + 1)
                break
else:
    print('Incorrect new container weight')






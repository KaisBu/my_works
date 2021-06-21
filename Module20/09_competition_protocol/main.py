def entries(number):
    data_records = dict()
    i = 0

    while i != number:
        input_data = input('Record {index}: '.format(index=i+1)).split()

        if len(input_data) == 2 and input_data[0].isdigit():
            if input_data[1] not in data_records:
                data_records[input_data[1]] = (int(input_data[0]), i + 1)
            else:
                if int(input_data[0]) > data_records[input_data[1]][0]:
                    data_records[input_data[1]] = (int(input_data[0]), i + 1)
            i += 1
        else:
            print('Incorrect record, try again.')

    return data_records


def sorted_function(dictionary):
    max_record = 0
    names_of_winners = []
    records_of_winners = []

    for name, tuple_records in dictionary.items():
        if tuple_records[0] <= max_record:
            is_in = False

            for index, record in enumerate(records_of_winners):
                if record < tuple_records[0]:
                    records_of_winners.insert(index, tuple_records[0])
                    names_of_winners.insert(index, name)
                    is_in = True
                    break
                elif record == tuple_records[0]:
                    if tuple_records[1] < dictionary[names_of_winners[index]][1]:
                        records_of_winners.insert(index, tuple_records[0])
                        names_of_winners.insert(index, name)
                        is_in = True
                        break

            if not is_in:
                records_of_winners.append(tuple_records[0])
                names_of_winners.append(name)

        else:
            names_of_winners.insert(0, name)
            records_of_winners.insert(0, tuple_records[0])
            max_record = tuple_records[0]

    return zip(names_of_winners[:3], records_of_winners[:3])


records_num = int(input('Enter number of records: '))

print('Entries (result and name):')
records_dict = entries(records_num)

if len(records_dict) >= 3:
    print('\nResults of competition: ')
    for place, winner in enumerate(list(sorted_function(records_dict))):
        print('{i} place: {winner_name} ({record})'.format(
            i=place + 1,
            winner_name=winner[0],
            record=winner[1]
        ))
else:
    print('Not not enough participants!')






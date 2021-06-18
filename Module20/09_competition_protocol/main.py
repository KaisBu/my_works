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


# def sorted_function(dictionary):
#     names_of_winners = []
#     records_of_winners = []
#     for name, records in dictionary.items():
#         if records[0] > records_of_winners[0]:




records_num = int(input('Enter number of records: '))
print('Entries (result and name):')

records_dict = entries(records_num)
sorted_function(records_dict)




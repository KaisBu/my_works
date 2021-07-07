import os


def search_path(some_list):
    if len(some_list) == 1:
        return os.path.join(some_list[0])

    path = os.path.join(some_list[0], search_path(some_list[1:]))
    return path


def overwrite_file(f_path, text):
    while True:
        answer = input('Do you want to overwrite the file? ').lower()

        if answer == 'yes':
            text_doc = open(f_path, 'w')
            text_doc.write(text)
            text_doc.close()
            print('File overwritten successfully!')
            break
        elif answer == 'no':
            print('File is not overwritten')
            break
        else:
            print('Wrong answer')


def save_file(f_path, text):
    text_doc = open(f_path, 'w')
    text_doc.write(text)
    text_doc.close()
    print('File saved')


string = input('Enter the string: ')
print('\nWhere do you want to save the document? Enter the sequences of folders (separate by space):')
folders_list = input().split()
folder_path = os.path.abspath(os.path.join(os.path.sep, search_path(folders_list)))

if os.path.exists(folder_path):
    file_name = input('Enter the file name: ') + '.txt'
    file_path = os.path.abspath(os.path.join(folder_path, file_name))

    if os.path.exists(file_path):
        overwrite_file(file_path, string)
    else:
        save_file(file_path, string)
else:
    print('The is no such path')


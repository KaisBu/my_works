violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

num_songs = int(input('Enter number of songs: '))
summ, i = 0, 0

if num_songs < 0:
    print('Number of songs must be positive.')
elif num_songs > 9:
    print('There are not so many songs.')
else:
    for key in violator_songs.keys():
        if i == num_songs:
            break
        print('Name of {number} song:'.format(number=i+1), key)
        summ += violator_songs[key]
        i += 1

    print('Total playing time of songs:', round(summ, 2), 'minutes.')


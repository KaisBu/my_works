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

summ, i = 0, 0

while True:
    num_songs = int(input('Enter number of songs: '))

    if 0 <= num_songs <= 9:
        for key in violator_songs.keys():
            if i == num_songs:
                break
            print('Name of {number} song:'.format(number=i+1), key)
            summ += violator_songs[key]
            i += 1

        print('\nTotal playing time of songs:', round(summ, 2), 'minutes.')
        break
    else:
        print('Number of songs must be positive and less than {length}.'.format(length=len(violator_songs)))


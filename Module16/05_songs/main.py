violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

total_number = int(input('Enter total number of songs: '))
total_time = 0

for i in range(total_number):
    song_title = input(f'Enter {i + 1} song title: ')
    for lst in violator_songs:
        if song_title in lst:
            total_time += lst[1]

print('\nTotal time:', total_time)

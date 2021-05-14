films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
favorite_films = []

films = [film.lower() for film in films]

movie_title = input('\nEnter the movie title: ')

while movie_title.lower() != 'end':
    if movie_title.lower() in films:
        favorite_films.append(movie_title)
    else:
        print('The movie is not on the list')
    movie_title = input('Enter next movie title: ')

print('\nFavorite films:\n', favorite_films)

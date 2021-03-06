import imdb

moviesDB = imdb.IMDb()

# # Help?
# print(dir(moviesDB))
# ----------------------------------------
# 1) Search for a title
movies = moviesDB.search_movie('inception')

# print('Searching for "inception":')
# for movie in movies:
#     title = movie['title']
#     year = movie['year']
#     print(f'{title} - {year}')

## Help?
#print(movies[0].keys())
    


# ----------------------------------------
# 2) List movie info
id = movies[0].getID()
movie = moviesDB.get_movie(id)

title = movie['title']
year = movie['year']
rating = movie['rating']
directors = movie['directors']
casting = movie['cast']

# print('Movie info:')
# print(f'{title} - {year}')
# print(f'rating: {rating}')

# direcStr = ' '.join(map(str,directors))
# print(f'directors: {direcStr}')

# actors = ', '.join(map(str, casting))
# print(f'actors: {actors}')

## Help?
#print(movie.keys())
# ----------------------------------------
# 3) List actor info
id = casting[0].getID()
person = moviesDB.get_person(id)
bio = moviesDB.get_person_biography(id)

name = person['name']
birthDate = person['birth date']
height = person['height']
trivia = person['trivia']
titleRefs = bio['titlesRefs']

# print(f'name: {name}')
# print(f'birth date: {birthDate}')
# print(f'height: {height}')
# print(f'trivia: {trivia[0]}')

# titleRefsStr = ', '.join(map(str, titleRefs))
# print(f'bio title refs: {titleRefsStr}')

## Help?
#print(dir(casting[0]))
#print(person.keys())

## Help?
#print(bio.keys())
#print(bio['titlesRefs'].keys())
# ----------------------------------------
# 4) Get top/bottom 10 movies 
top = moviesDB.get_top250_movies()
bottom = moviesDB.get_bottom100_movies()

print('Top 10 movies:')
for movie in top[0:9]:
	print(movie)
print()

print('Bottom 10 movies:')
for movie in bottom[0:9]:
	print(movie)


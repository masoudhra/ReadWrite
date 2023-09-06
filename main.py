# moddhaye mojoo : r read  w write  a append  r+ read and write
films_file = open("films.text", "r")

films = films_file.readlines()
for film in films:
    print(film)

films_file.close() # hatman bayad bebandimesh


# moddhaye mojoo : r read  w write  a append  r+ read and write
# films_file = open("films.text", "r")

# films = films_file.readlines()
# for film in films:
#     print(film)

# films_file.close() # hatman bayad bebandimesh


films_file = open("films.text", "a")
films_file.write("\nThis is the file for the movies")
films_file.close()

# agar w bezarim va faghat write konim neveshtehaye ghabli pak mishe va agghat chizi ke khastim ezafe mishe
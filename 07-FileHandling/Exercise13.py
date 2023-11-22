# 13.	An array movie_titles contains any five movie titles. 
# Write a program that writes the movie titles to the movies.txt file, each title on a separate line. 
# After executing the program, open the created text file and check its content.

movie_titles = ["Wilson lo siento", "El gato", "Bill", "Adam", "AaAAa"]

# write to a file
file = open("movies.txt", 'w')

for element in movie_titles:
    file.write(element+"\n")

file.close()
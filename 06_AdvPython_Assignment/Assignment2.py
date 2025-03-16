# ab2:  Movie Library Create a class MovieLibrary that manages a collection of movies: 

#  1. Class Attribute: ○ available_movies: A list of all movies available in the library.

#  2. Instance Attributes: ○ member_name: The name of the library member. ○ borrowed_movies: A list of movies borrowed by the member. 

# 3. Methods: ○ borrow_movie(self, movie): Borrows a movie from the library if available. 

#  ○ return_movie(self, movie): Returns a movie to the library.

#  ○ view_borrowed_movies(self): Prints a list of movies borrowed by the member




class MovieLibrary:
    available_movies = []  # Class attribute to store all available movies

    def __init__(self, member_name):
        self.member_name = member_name  # Instance attribute for the library member's name
        self.borrowed_movies = []  # List to track movies borrowed by the member

    def borrow_movie(self, movie):
        """Method to borrow a movie from the library"""
        if movie in MovieLibrary.available_movies:
            self.borrowed_movies.append(movie)
            MovieLibrary.available_movies.remove(movie)
            return f"{self.member_name} has borrowed '{movie}'."
        else:
            return "Movie not available."

    def return_movie(self, movie):
        """Method to return a borrowed movie to the library"""
        if movie in self.borrowed_movies:
            self.borrowed_movies.remove(movie)
            MovieLibrary.available_movies.append(movie)
            return f"{self.member_name} has returned '{movie}'."
        else:
            return "This movie was not borrowed by you."

    def view_borrowed_movies(self):
        """Method to view all borrowed movies by the member"""
        if self.borrowed_movies:
            print(f"{self.member_name} has borrowed: {', '.join(self.borrowed_movies)}")
        else:
            print(f"{self.member_name} has not borrowed any movies.")

# Example Usage
MovieLibrary.available_movies = ["Inception", "Interstellar", "The Dark Knight", "Titanic"]

# Creating a library member
member1 = MovieLibrary("John")
print(member1.borrow_movie("Inception"))
print(member1.borrow_movie("Titanic"))

member1.view_borrowed_movies()

print(member1.return_movie("Inception"))
MovieLibrary.available_movies.append("Avatar")  # Adding a new movie to the library

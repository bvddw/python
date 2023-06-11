class Book:
    def __init__(self, title_: str, author_: str, year_: int, genre_: str):
        self.title = title_
        self.author = author_
        self.year = year_
        self.genre = genre_

    def __str__(self) -> str:
        return f'title: {self.title}, author: {self.author}, year: {self.year}, genre: {self.genre}.'


title: str = input('Enter title: ')
author: str = input('Enter author name: ')
while True:
    try:
        year: int = int(input('Enter the year the book was written: '))
        if year not in range(2024):
            print('Incorrect data.')
        else:
            break
    except ValueError:
        print('You need to enter integer number.')
genre: str = input('Enter genre: ')
book: Book = Book(title, author, year, genre)
print(book)

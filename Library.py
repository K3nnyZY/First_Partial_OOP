class Library:
    def __init__(self, books: str):
        self.books = books

    def disponibilidad(self):
        print(f"\n{len(books)} los libros disponibles son: ")
        for book in books:
            print(" - " + book)
        print("\n")

    def prestar(self, name, bookname):
        if bookname not in self.books:
            print(
                f"{bookname} el libro no esta disponible.\n")
        else:
            pista =[]
            pista.append({name: bookname})
            print("libro prestado, por favor devuelvelo, cuando no lo vas a usar.\n")
            self.books.remove(bookname)

    def devuelto(self, bookname):
        print("libro devuelto, muchas gracias \n")
        self.books.append(bookname)


class Usuario():
    def solicitar(self):
        self.book = input("ingresa el libro que quiere pedir:  ")
        return self.book

    def devolver(self):
        name = input("ingresa el nombre: ")
        self.book = input("ingresa el nombre del libro que quiere devolver:  ")
        pista = []
        if {name: self.book} in pista:
            pista.remove({name: self.book})
        return self.book


class Author(object):

    """A class that models an author with the following instance variables:
    - author: string - the author's name
    - publisher: string - the author's publisher"""

    def __init__(self, name, publisher):
        self._name = name
        self._publisher = publisher

    def __str__(self):

        return("%s, Publisher: %s" % (self._name, self._publisher))

    def getName(self):

        return ("Author: %s" % (self._name))

    def setName(self, name):

        self._name = name
        return ("New author: %s" % (self._name))

    def getPublisher(self):

        return ("Publisher: %s" % (self._publisher))

    def setPublisher(self, publisher):

        self._publisher = publisher
        return ("New publisher: %s" % (self._publisher))

    publisher = property(getPublisher, setPublisher)
    name = property(getName, setName)


class Book(object):

    """A super class that models a book with the following instance variables:
    - title: string - the title of the book
    - price: float - the price of the book
    - **author** - using composition calls the Author class for its two instance
      variables: author, publisher"""

    def __init__(self, title, price, author):
        self._title = title
        self._price = price
        self._author = author

    def __str__(self):

        return ("Book Title: %s, Price: %.2f, Author: %s" % (self._title, self._price, self._author))

    def getTitle(self):

        return ("Book Title: %s" % (self._title))

    def setTitle(self, title):

        self._title = title
        return ("Book Title: %s" % (self._title))

    def getPrice(self):

        return ("Price for %s: %.2f" % (self._title, self._price))

    def setPrice(self, price):

        self._price = price
        return ("New Price for %s: %.2f" % (self._title, self._price))
        
        price = property(getPrice, setPrice)
        title = property(getTitle, setTitle)

class eBook(object):

    """A sub class that models an ebook with the following instance variables:
    - title, price are initialised by the super class Book
    - author is initialised by the super class Book through composition of the
      Author class
    - url: string - the url of the ebook"""

    def __init__(self, title, price, author, url):
        Book.__init__(self, title, price, author)
        self._url = url

    def __str__(self):

        return ("Book Title: %s\nPrice: %.2f\nAuthor: %s\nURL: %s\n" % (self._title, self._price, self._author, self._url))

    def getURL(self):

        return ("Book URL: %s" % (self._url))

    def setURL(self, url):

        self._url = url
        return ("Book URL: %s" % (self._url))

    url = property(getURL, setURL)
    title = property(Book.getTitle, Book.setTitle)
    price = property(Book.getPrice, Book.setPrice)


def main_ebook():

    print("\nE-BOOK CLASS")
    author1 = Author("Claire Foran", "Tralee Writers")
    ebook = eBook("Linux for Beginners", 30.00, author1, "http://www.realebooks.com")
    print(ebook)
    ebook.title = "Unix for Beginners"
    print(ebook)
    ebook.price = 25.95
    print(ebook)
    ebook.url = "http://www.amazon.com/CS"
    print(ebook)
    author1.name = "Derek Bridge"
    print(ebook)
    author1.publisher = "Falcon"
    print(ebook)

class RealBook(object):

    """A sub class that models a real book with the following instance variables:
    - title, price are initialised by the super class Book
    - author is initialised by the super class Book through composition of the
      Author class
    - postage: float - the cost of delivering the book
    The price of the book must be overridden to include the cost of postage."""

    def __init__(self, title, price, author, postage):
        Book.__init__(self, title, price, author)
        self._postage = postage

    def __str__(self):

        return ("Book Title: %s\nPrice + Postage: %.2f\nAuthor: %s\n" % (self._title, self._price + self._postage, self._author))

    def getPostage(self):

        return ("Postage: %.2f" % (self._postage))

    def setPostage(self, postage):
    
    
        return ("Postage: %.2f" % (self._postage))

    def setPostage(self, postage):

        self._postage = postage
        return ("Postage: %.2f" % (self._postage))

    def getPrice(self):

        self._price += self._postage
        return ("Price for %s: %.2f" % (self._title, self._price))

        postage = property(getPostage, setPostage)
        price = property(getPrice, Book.setPrice)
        title = property(Book.getTitle, Book.setTitle)


def main_realbook():

    print("\nREAL BOOK CLASS")
    author2 = Author("Cathy Bowen","Dungarvan Publisher")
    real_book = RealBook("ABC's", 3.00, author2, 2.00)
    print(real_book)
    real_book.title = "123's"
    print(real_book)
    real_book.price = 5.95
    print(real_book)
    real_book.postage = 3.00
    print(real_book)
    author2.name = "Cathal Hoare"
    print(real_book)
    author2.publisher = "Bloomsburg"
    print(real_book)

if __name__ == "__main__":
    main_ebook()
    main_realbook()
    
    

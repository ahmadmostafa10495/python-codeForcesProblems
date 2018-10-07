class Person():
    def __init__ (self,name,address,contact_number,gender,age):
        self.name=name
        self.address=address
        self.contact_number=contact_number
        self.gender=gender
        self.age=age
    def setname (self,name):
        self.name=name

    def getname (self):
        return self.name

    def setaddress (self,address):
        self.address=address

    def getaddress (self):
        return self.address

    def setcontact_number (self,contact_number):
        self.contact_number=contact_number

    def getcontact_number (self):
        return self.contact_number

    def setgender (self,gender):
        self.gender=gender

    def getgender (self):
        return self.gender

    def setage (self,age):
        self.age=age

    def getage (self):
        return self.age


class Author (Person):
    aid=14000
    def __init__ (self,name,address,contact_number,gender,age,author_books):
        self.author_books=author_books
        super(Author,self).__init__(name,address,contact_number,gender,age)
        self.author_id=Author.aid
        Author.aid+=1

    def setauthor_books (self,author_books):
        self.author_books=author_books

    def getauthor_books (self):
        return self.author_books

    def getauthor_id (self):
        return self.author_id

    def add_new_book (self,new_book):
        self.author_books.append(new_book)

    def search_book_byID (self,temp_book_id):
        i=0
        while i<len(self.author_books):
            if author_books[i].getbook_id() == temp_book_id :
                return author_books[i]
            i+=1

    def print_books_details (self):
        i=0
        while i<len(self.author_books):
            author_books[i].print_book_details()
            i+=1
            
    def print_author_details(self):
        print("Author's name is:",self.name)
        print("Author's address is:",self.address)
        print("Author's contact number is:",self.contact_number)
        print("Author's gender is:",self.gender)
        print("Author's age is:",self.age)
        print("Author's ID is:",self.author_id)
        print("Author's book(s) is(are):")
          


def createauthor():
    tempname=input("please enter the Author's name:")
    tempaddress=input("please enter the Author's address:")
    tempcontact_number=input("please enter the Author's contact number:")
    tempgender=input("please enter the Author's gender:")
    tempage=input("please enter the Author's age:")
    tempauthor_books=[]
    while 1:
        wannaadd=input("please press y to enter a new book")
        if wannaadd=='y':
                  tempbookname=input("please enter the book's name:")
                  i=0
                  while i<Book.bid:
                      if books[i].getname()==tempbookname:
                          tempauthor_books.append(books[i])
                          break
                      i+=1
        else:
                  break
        
    author.append(Author(tempname,tempaddress,tempcontact_number,tempgender,tempage,tempauthor_books))
author=[]
wannaout='y'
whatdoyouwant=""
while wannaout=='y':
    whatdoyouwant=input("what do you want sir/madame:")
    if whatdoyouwant=='create author':
        createauthor()
    elif whatdoyouwant=='print author':
        whatid=int(input("please enter Author's id:"))
        author[whatid].print_author_details()
    wannaout=input("if you want to continue press y:")

















    

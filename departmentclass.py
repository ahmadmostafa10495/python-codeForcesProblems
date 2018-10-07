class Department ():
    did=0
    def __init__(self,name,department_authors,department_librarians):
        self.name=name
        self.department_authors=department_authors
        self.department_librarians=department_librarians
        self.department_id=Department.did
        Department.did+=1

    def setname(self,name):
        self.name=name

    def getname(self):
        return self.name

    def setdepartment_authors (self,department_authors):
        self.department_authors=department_authors

    def getdepartment_authors(self):
        return self.department_authors

    def setdepartment_librarians(self,department_librarians):
        self.department_librarians=department_librarians

    def getdepartment_librarians(self):
        return self.department_librarians

    def getdepartment_id (self):
        return self.department_id

    def add_new_author (self,new_author):
        self.department_authors.append(new_author)

    def add_new_librarian (self,new_librarian):
        self.department_librarians.append(new_librarian)

    def search_book_byID(self,book_id):
        i=0
        while i<len(self.department_authors):
            if (self.department_authors[i].search_book_byID(book_id))!= None:
               return self.department_authors[i].search_book_byID(book_id)
            i+=1

    def search_author_byID(self,author_id):
        i=0
        while i<len(self.department_authors):
            if author_id==self.department_authors[i].getauthor_id():
                return self.department_authors[i]
            i+=1

    def search_librarian_byID(self,librarian_id):
        i=0
        while i<len(department_librarians):
            if librarian_id==self.department_librarians[i].getlibrarian_id():
                return self.department_librarians[i]
            i+=1
    
    def delete_author_byID(self,author_id):
        i=0
        while i<len(self.department_authors):
            if author_id==self.department_authors[i].getauthor_id():
                del self.department_authors[i]
                break
            i+=1

    def delete_librarian_byID(self,librarian_id):
        i=0
        while i<len(department_librarians):
            if librarian_id==self.department_librarians[i].getlibrarian_id():
                del self.department_librarians[i]
                break
            i+=1

    def print_authors_details (self):
        i=0
        print("department's author(s) is(are):")
        while i<len(self.department_authors):
            self.department_authors[i].print_author_details()
            i+=1

    def print_books_details (self):
        i=0
        print("department's book(s) is(are):")
        while i<len(self.department_authors):
            self.department_authors[i].print_books_details()
            i+=1

    def print_librarians_details (self):
        i=0
        print("department's librarian(s) is(are):")
        while i<len(self.department_librarians):
            self.department_librarians[i].print_librarian_details()
            i+=1

    def print_department_details (self):
        print("department's name is:",self.getname())
        print("department's ID is:",self.getdepartment_id())
       
            
                































            

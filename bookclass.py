class Book ():
    bid=0
    def __init__ (self,name,author,cnt_copy_book,cnt_copy_available,cnt_copy_borrow,book_department):
        self.name=name
        self.author=author
        self.cnt_copy_book=cnt_copy_book
        self.cnt_copy_available=cnt_copy_available
        self.cnt_copy_borrow=cnt_copy_borrow
        self.book_department=book_department
        self.book_id=Book.bid
        Book.bid+=1
        
    def setname(self,name):
        self.name=name

    def getname(self):
        return self.name

    def setauthor(self,author):
        self.author=author

    def getauthor(self):
        return self.author

    def setcnt_copy_book (self,cnt_copy_book):
        self.cnt_copy_book=cnt_copy_book

    def getcnt_copy_book(self):
        return self.cnt_copy_book

    def setcnt_copy_available(self,cnt_copy_available):
        self.cnt_copy_available=cnt_copy_available

    def getcnt_copy_available (self):
        return self.cnt_copy_available

    def setcnt_copy_borrow (self,cnt_copy_borrow):
        self.cnt_copy_borrow=cnt_copy_borrow

    def getcnt_copy_borrow(self):
        return self.cnt_copy_borrow

    def setbook_department(self,book_department):
        self.book_department=book_department

    def getbook_department(self):
        return self.book_department

    def getbook_id(self):
        return self.book_id

    def increase_cnt_copy (self,addedbooks):
        self.cnt_copy_book+=addedbooks
        self.cnt_copy_available+=addedbooks

    def make_borrow_operation (self):
        self.cnt_copy_available-=1
        self.cnt_copy_borrow+=1

    def make_receive_book_operation (self):
        self.cnt_copy_available+=1
        self.cnt_copy_borrow-=1    

    def print_book_details (self):
        print ("Book's name is:",self.name)
        print ("Book's total count of copies is:",self.cnt_copy_book)
        print ("Book's count of available copies is:",self.cnt_copy_available)
        print ("Book's count of borrowed copies is:",self.cnt_copy_borrow)
        print ("Book's ID",self.book_id)

    def print_author_details(self)
        (self.author).print_author_details()

    def print_department_details(self)
        (self.book_department).print_department_details()














    

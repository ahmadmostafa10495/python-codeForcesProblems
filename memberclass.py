from datetime import timedelta
class Member(Person):
    mid=0
    def __init__ (self,name,address,contact_number,gender,age):
        super(Member,self).__init__(name,address,contact_number,gender,age)
        self.member_id=Member.mid
        Member.mid+=1
        self.enter_time=timedelta()
        self.exit_time=timedelta()
        self.books_borrow=[]

    def setenter_time(self,enter_time):
        self.enter_time=enter_time

    def getenter_time(self):
        return self.enter_time

    def setexit_time(self,exit_time):
        self.exit_time=exit_time

    def getexit_time(self):
        return self.exit_time

    def setbooks_borrow(self,books_borrow):
        self.books_borrow=books_borrow

    def getbooks_borrow(self):
        return self.books_borrow

    def getmember_id (self):
        return self.member_id

    def add_new_book_borrow (self,new_book):
        if len(self.books_borrow)<3:
            self.books_borrow.append[new_book]
        else:
            return True

    def search_book_borrow_byID (self,book_id):
        i=0
        while i<len(self.books_borrow):
            if self.books_borrow[i].getbook_id()==book_id:
                return self.books_borrow[i]
            i+=1

    def delete_book_borrow_byID (self,book_id):
        i=0
        while i<len(self.books_borrow):
            if self.books_borrow[i].getbook_id()==book_id:
                del self.books_borrow[i]
            i+=1        

    def print_books_borrow_details (self):
        i=0
        print("member's borrowed book(s) is(are):")
        while i<len(self.books_borrow):
            self.books_borrow[i].print_book_details()
            self.books_borrow[i].print_author_details()
            self.books_borrow[i].print_department_details()
            i+=1

    def print_member_details(self):
        print("member's name is:",self.name)
        print("member's address is:",self.address)
        print("member's contact number is:",self.contact_number)
        print("member's gender is:",self.gender)
        print("member's age is:",self.age)
        print("member's ID is:",self.member_id)
        print("member's enter time is:",self.enter_time)
        print("member's exit time is:",self.exit_time)
























        

class Librarian (Person):
    lid=0
    def __init__ (self,name,address,contact_number,gender,age,librarian_department):
        self.librarian_department=librarian_department
        self.librarian_id=Librarian.lid
        Librarian.lid+=1
        super(Librarian,self).__init__(name,address.contact_number,gender,age)

    def setdepartment (self,department):
        self.librarian_department=librarian_department

    def getlibrarian_department (self):
        return self.librarian_department

    def getlibrarian_id(self):
        return self.librarian_id

    def print_librarian_details(self):
        print("librarian's name is:",self.name)
        print("librarian's address is:",self.address)
        print("librarian's contact number is:",self.contact_number)
        print("librarian's gender is:",self.gender)
        print("librarian's age is:",self.age)
        print("librarian's ID is:",self.librarian_id)

    def print_department_details(self):
        print("librarian department is:")
        (self.librarian_department).print_department_details()    

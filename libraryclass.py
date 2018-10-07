class Library():
    lib=0
    def __init__(self,name,start_time,end_time,capacity):
        self.library_id=Library.lib
        Library.lib+=1
        self.name=name
        self.start_time=start_time
        self.end_time=end_time
        self.capacity=capacity
        self.current_member=0
        self.library_departments=[]
        self.library_members=[]
        self.members_in=[]

    def setname (self,name):
        self.name=name

    def getname (self):
        return self.name

    def setstart_time (self,start_time):
        self.start_time=start_time

    def getstart_time (self):
        return self.start_time

    def setend_time(self,end_time):
        self.end_time=end_time

    def getend_time(self):
        return self.end_time

    def setcapacity(self,capacity):
        self.capacity=capacity

    def getcapacity(self):
        return self.capacity

    def setcurrent_member(self,currnet_member):
        self.current_member=current_member

    def getcurrent_member(self):
        return self.current_member

    def setlibrary_departments(self,library_departments):
        self.library_departments=library_departments

    def getlibrary_departments(self):
        return self.library_departments

    def setlibrary_members(self,library_members):
        self.library_members=libary_members

    def getlibrary_members (self):
        return self.library_members

    def getlibrary_id(self):
        return self.library_id

    def member_enter(self,member_id,enter_time):
        i=0
        while i<len(self.library_members):
            if member_id==self.library_members[i].getmember_id():
                break
            i+=1
        else:
            return None
        if enter_time < self.start_time:
            return None
        if self.capacity==self.current_member:
            return None
        self.current_member+=1
        self.library_members[i].setenter_time(enter_time)
        self.members_in.append(self.library_members[i])
        return 1
    def member_exit  (self,member_id,exit_time):
        i=0
        while i<len(self.library_members):
            if member_id==self.library_members[i].getmember_id():
                break
            i+=1
        else:
            return None
        if exit_time > self.exit_time:
            return None
        j=0
        while j<len(self.members_in):
            if member_id==self.members_in[j].getmember_id():
                break
            j+=1
        else:
            return None
        self.current_member-=1
        del self.members_in[j]
        self.library_members[i].setexit_time(exit_time)
        timein=self.library_members[i].getenter_time - self.library_members[i].getexit_time
        secondsvalue=timein.seconds
        secondsvalue+=1799
        moneyneeded=secondsvalue//1800
        return moneyneeded

    def add_new_department(self,new_department):
        self.library_departments.append(new_department)

    def add_new_member(self,new_member):
        self.library_members.append(new_member)

    def delelte_department_byID (self,department_id):
        i=0
        while i<len(self.library_departments):
            if department_id==self.library_departments[i].getdepartment_id():
                del self.library_departments[i]
            i+=1

    def delelte_member_byID (self,member_id):
        i=0
        while i<len(self.library_members):
            if member_id==self.library_members[i].getmember_id():
                del self.library_members[i]
            i+=1

    def search_department_byID  (self,department_id):
        i=0
        while i<len(self.library_departments):
            if department_id==self.library_departments[i].getdepartment_id():
                return self.library_departments[i]
            i+=1

    def search_member_byID (self,member_id):
        i=0
        while i<len(self.library_members):
            if member_id==self.library_members[i].getmember_id():
                return self.library_members[i]
            i+=1

    def search_librarian_byID (self,librarian_id):
        i=0
        j=0
        while i<len(self.library_departments):
            while j<len(self.library_departments[i].getdepartment_librarians()):
                if self.library_departments[i].getdepartment_librarians()[j].getlibrarian_id()==librarian_id:
                    return self.library_departments[i].getdepartment_librarians()[j]
                j+=1
            i+=1        
            j=0

    def print_department_details(self):
        i=0
        print("departments' details are:")
        while i<len(self.library_departments):
            self.library_departments[i].print_department_details()
            self.library_departments[i].print_author_details()
            self.library_departments[i].print_books_details()
            i+=1

    def print_librarian_details(self):
        i=0
        print("librarians' details are:")
        while i<len(self.library_departments):
            self.library_departments[i].print_librarians_details()
            i+=1

    def print_member_details (self):
        i=0
        print("members' details are:")
        while i<len(self.library_members):
            self.library_members[i].print_member_details()
            i+=1

    def print_library_details(self):
        print("library's name is:",self.name)
        print("library's start time is:",self.start_time)
        print("library's end time is:",self.end_time)
        print("library's capacity is:",self.capacity)
        print("library's ID is:",self.library_id)
        print("library's number of current members is:",self.current_member)

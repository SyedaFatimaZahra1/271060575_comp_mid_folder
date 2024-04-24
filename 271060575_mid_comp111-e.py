
class People:
    def __init__(self,name,age,id):
        self.name = name
        self.age = age
        self.id = id
    def display_info(self):
        print(f"this person has name{self.name},age{self.age}and id {self.id}")
class Student(People):
    def __init__(self,grade,class_enrolled,name,age,id):
        super().__init__(name,age,id)
        self.grade = grade
        self.class_enrolled = class_enrolled
    def display_student(self):
        print(self.display_info())
        print(f"student grade is {self.grade} and classes currently enrolled are as follows:")
        print(self.class_enrolled)
class Teacher(People):
    def __init__(self,taught_subj,class_list,name,age,id):
        super().__init__(name,age,id)
        self.taught_subj = taught_subj
        self.class_list = class_list
    def display_teacher(self):
        print(self.display_info())
        print(f"teacher teaches subject {self.taught_subj} and are responsible for following classes: ")
        print(self.class_list)
class Admin(People):
    def __init__(self,department,emp_list,name,age,id):
        super().__init__(name,age,id)
        self.department = department
        self.emp_list = emp_list
    def display_admin(self):
        print(self.display_info())  
        print(f"admin manages department {self.department} and employees are as follows :")
        print(self.emp_list)  

ppl_name = str(input("enter name of person"))
ppl_age = int(input("enter age of them"))
ppl_id = int(input("enter your id"))
ppl_obj = People(ppl_name,ppl_age,ppl_id)
print(ppl_obj.display_info())
st_grade = str(input("enter student's grade: "))
st_enroll =[]
st_enroll = str(input("enter list of students classes enrolled separated by comma (,) : "))
st_obj = Student(st_grade,st_enroll,ppl_name,ppl_age,ppl_id)
print(st_obj.display_student())
teach_subj = str(input("which subject does teacher teach : "))
teach_class =[]
teach_class = str(input("which classes is teacher responsiblle for teaching this subject(separate by comma): "))
teacher_obj = Teacher(teach_subj,teach_class,ppl_name,ppl_age,ppl_id)
print(teacher_obj.display_teacher())
admin_dept = str(input("what is the department of the administrator : "))
admin_emp = []
admin_emp = str(input("enter the list of employees cuurently enrolled in department(separated by comma): "))
admin_obj = Admin(admin_dept,admin_emp,ppl_name,ppl_age,ppl_id)
print(admin_obj.display_admin())

print("question 3")
                   
class Song:
    def __init__(self,title,artist,album,duration):
        self.title = title
        self.artist = artist
        self.album = album
        self.duration = duration
    def display_info(self):
        print(f" title : {self.title} artist: {self.artist} album: {self.album} duration: {self.duration}")
class Playlist:
    def __init__(self,pl_title,descrip):
        self.pl_title = pl_title
        self.descrip = descrip
        self.song_list = []
    def add_song(self,obj_song):
        if obj_song not in self.song_list:
            self.song_list.append(obj_song)
            print("song has been added")
        else:
            print("song already exists")
    def remove_song(self,obj_song):
        if obj_song in self.song_list:
            self.song_list.remove(obj_song)
        else:
            print("song does not exist in playlist")
    def display_all_song(self):
        for i in self.song_list:
            print(i.display_info())
          
class Library:
    def __init__(self):
        self.pl_list = []
    def add_pl(self,obj_pl):
        if obj_pl not in self.pl_list:
            self.pl_list.append(obj_pl)
            print("playlist added")
        else:
            print("song already exists")
    def remove_pl(self,obj_pl):
        if obj_pl in self.pl_list:
            self.pl_list.remove(obj_pl)
            print("playlist removed")
        else:
            print("song already deleted") _
        for i in self.pl_list:
            print(i.display_all_song())               

print("question 1")
def reverse(string):
    if len(string) == 1:
        return string
    else:
        return string[-1:] + reverse(string[:-1])
str_input = str(input("enter string to take its reverse : "))
print(reverse(str_input))    






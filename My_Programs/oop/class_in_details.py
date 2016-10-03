class Student:
    num_of_student =  0
    class_teacher ='Mrs. Devid'

    def __init__ (self , rno, name , mks) :
        self.rollno= rno
        self.name = name
        self.marks = mks
        self.grade = ''
        Student.num_of_student += 1

    def calcGrade (self) :

        if (self.marks >=80):
            self.grade ='A+'
            print self.name 
            print self.grade
        elif(self.marks >= 70 ):
            self.grade = 'A'
            print self.name 
	    print self.grade
        elif(self.marks >= 60 ):
            self.grade = 'B'
            print self.name 
	    print self.grade
        elif(self.marks >= 50 ):
            self.grade = 'C'
            print self.name 
	    print self.grade
        elif(self.marks >= 40 ):
            self.grade = 'D'
            print self.name 
	    print self.grade
        else :
            self.grade ="E"
	    print self.grade


if __name__=='__main__':
    stud1 = Student(12,'IronMan',68.5)
    stud2 = Student(14,'Halk',80.32)
    stud3 = Student(16,'Thor',40)
    stud4 = Student(15,'BatMan',50)
    stud1.calcGrade()
    stud2.calcGrade()
    stud3.calcGrade()
    stud4.calcGrade()
    print ""  
    print vars (stud1)
    print vars (stud3)
    print vars (stud4)
    
    print ""
print "This is the end of the program"


class Student:
    """
    student class
    """
    # class variable,student number
    total_cnt=0

    def __init__(self,name,age):
        """
        initiated method
        :param name:
        :param age:
        """
        self.name=name
        self.age=age
        Student.total_cnt +=1

    def set_grade(self,grade):
        """

        set the grade of student
        :param grade:
        :return:
        """
        self.grade=grade


    def print_info(self):
        """
        print the info of stu
        :return:
        """
        print("student info",self.name,self.age,self.grade)

#create two instances
s1=Student("xiaoming",20)
s2=Student("Bao",23)
s1.set_grade(100)
s2.set_grade(98)

s1.print_info()
s2.print_info()

print(Student.total_cnt)

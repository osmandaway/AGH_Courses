# Exercise: *args, **kwargs
# Change parameters in __init__ of all subclasses of class Person (Student, StaffMember, Lecturer) into 
# (*args, **kwargs) on the basis of example below. 
# Then check how it works. 



# class MySubclass(Superclass):
#     def __init__(self, subclass_value, *args, **kwargs):
#         self.myvalue = kwargs.pop('myvalue', None)
#         self.subclass_value = subclass_value
#         super().__init__(*args, **kwargs)



class Person:
    def __init__(self, name, surname, number):
        self.name = name
        self.surname = surname
        self.number = number

class Student(Person):
    UNDERGRADUATE, POSTGRADUATE = range(2)

    def __init__(self, student_type, name, surname, number):
        self.student_type = student_type
        self.classes = []
        super().__init__(name, surname, number)

    def enrol(self, course):
        self.classes.append(course)



class StaffMember(Person):
    PERMANENT, TEMPORARY = range(2)

    def __init__(self, employment_type, name, surname, number):
        self.employment_type = employment_type
        super().__init__(name, surname, number)



class Lecturer(StaffMember):
    def __init__(self, employment_type, name, surname, number):
        self.courses_taught = []
        super().__init__(employment_type, name, surname, number)

    def assign_teaching(self, course):
        self.courses_taught.append(course)



def main():
    
    jane = Student(Student.POSTGRADUATE, "Jane", "Smith", "123456789")
    jane.enrol('a_postgrad_course')
    print(jane)


    bob = Lecturer(StaffMember.PERMANENT, "Bob", "Jones", "123456789")
    bob.assign_teaching('an_undergrad_course')


if __name__ == '__main__':
    main()
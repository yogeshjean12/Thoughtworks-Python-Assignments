class Student:

    '''Student details'''

    def __init__(self, id_no, name, dept, subject_names):
        self.id_no = id_no
        self.name = name
        self.subject_names = subject_names
        self.dept = dept

    def get_student_department(self):
        return self.dept

    def get_student_subjects(self):
        return self.subject_names

class Department:

    '''Department details'''

    def __init__(self, department_name, students, department_subjects):
        self.department_name = department_name
        self.students = students
        self.department_subjects = department_subjects

    def get_students_name(self):
        return self.students

    def get_department_subjects(self):
        return self.department_subjects

    def get_department_name(self):
        return self.department_name

def overlapping_subjects_among_departments():
    common_subjects = []
    for department in department_obj_list:
        if common_subjects == []:
            common_subjects = department.get_department_subjects()
        else:
            overlap_subject = []
            for i in common_subjects:
                if i in department.get_department_subjects():
                    overlap_subject.append(i)
            common_subjects = overlap_subject
    return 'Subjects that overlap between various departments: {}'.format(common_subjects)

def more_than_three_subject():
    dept_list = []
    for student in student_obj_list:
        if len(student.get_student_subjects()) > 3:
            if student.get_student_department() not in dept_list:
                dept_list.append(student.get_student_department())
    return '\nName of the departments where students take more than 3 courses : {}\n'.format(dept_list)

def display_students_name_in_the_department():
    user_department_name = input('Which department students name you want to see? \nmech\ncivil\ncse\nit \nType any one: ').lower().strip()
    for department in department_obj_list:
        if department.get_department_name() == user_department_name:
            print('\n{} department students are: {}'.format(department.get_department_name(),department.get_students_name()))
            return
    else:
        print('\nwrong input')

department1 = Department('mech', ['yogesh', 'ram', 'venkat'], ['dynamics', 'fluid mechanics', 'english', 'thermodynamics'])
department2 = Department('civil', ['leo'], ['construction', 'structural', 'english', 'finite particles'])
department3 = Department('cse', ['ajay', 'sweetha'], ['html', 'python', 'english', 'java'])
department4 = Department('it', ['ruby', 'anandh', 'andharipa'], ['sql', 'python', 'english', 'java', 'oracle'])
department_obj_list = [department1, department2, department3, department4]

student1 = Student(9144516, 'yogesh', 'MECH', ['english', 'fluid mechanics', 'dynamics'])
student2 = Student(9145212, 'ram', 'MECH', ['dynamics', 'fluid mechanics', 'english'])
student3 = Student(9143156, 'venkat', 'MECH', ['english', 'fluid mechanics', 'dynamics'])
student4 = Student(9126545, 'ruby', 'IT', ['sql', 'python', 'english', 'java'])
student5 = Student(9124841, 'anandh', 'IT', ['english', 'python', 'sql'])
student6 = Student(9159872, 'ajay', 'CSE', ['html', 'python', 'english'])
student7 = Student(9122476, 'andhripa', 'IT', ['english', 'python', 'sql', 'java'])
student8 = Student(9173245, 'leo', 'CIVIL', ['construction', 'structural', 'english'])
student9 = Student(9153587, 'sweetha', 'CSE', ['english', 'python', 'html'])
student_obj_list = [student1, student2, student3, student4, student5, student6, student7, student8, student9]

display_students_name_in_the_department()
print(more_than_three_subject())
print(overlapping_subjects_among_departments())

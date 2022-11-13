class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_le(self, lecturer, course, grade):
      if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached_lect and course in self.courses_in_progress and 0 <grade <=10:
            if course in lecturer.courses_grades:
                lecturer.courses_grades[course] += [grade]
            else:
                lecturer.courses_grades[course] = [grade]
      else:
            return 'Ошибка'
        
    def mid_grade_st(self):
      grade_list_st=[]
      for grade in self.grades:
        for value in self.grades[grade]:
         grade_list_st.append(value)
      return sum(grade_list_st)/len(grade_list_st)
  
    def courses(self, course):
      courses_list=[]
      for course in self.courses_in_progress:
        courses_list.append(course)
      return ', '.join(courses_list)
      
    def fin_courses(self, course):
      fin_courses_list=[]
      for course in self.finished_courses:
        fin_courses_list.append(course)
      return ', '.join(fin_courses_list)
      
    def __str__(self):
      return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.mid_grade_st()}\nКурсы в процессе изучения: {self.courses(self)}\nЗавершенные курсы: {self.fin_courses(self)}')

    def __lt__(self,other):
      return self.mid_grade_st() < other.mid_grade_st()

    def __gt__(self,other):
      return self.mid_grade_st() > other.mid_grade_st()

    def __eq__(self,other):
      return self.mid_grade_st() == other.mid_grade_st()
  
  
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        

class Lecturer(Mentor):
  def __init__(self, name, surname):
    self.courses_attached_lect = []
    self.courses_grades={}
    super().__init__(name, surname)
  
  def mid_grade(self):
    grade_list=[]
    for grade in self.courses_grades:
      for gr_value in self.courses_grades[grade]:
       grade_list.append(gr_value)
    return sum(grade_list)/len(grade_list)
      
  def __str__(self):
    return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.mid_grade()}')

  def __lt__(self,other):
      return self.mid_grade() < other.mid_grade()

  def __gt__(self,other):
      return self.mid_grade() > other.mid_grade()

  def __eq__(self,other):
      return self.mid_grade() == other.mid_grade()

class Rewiewer(Mentor):
  def __init__(self, name, surname):
    self.courses_attached = []
    super().__init__(name, surname)
  
  
  def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
          
  def __str__(self):
    return (f'Имя: {self.name}\nФамилия: {self.surname}')

  
    
best_student = Student('Ruoy', 'Eman', 'your_gender')
cool_student = Student('Tom', 'Kruzo', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

cool_student.courses_in_progress += ['Python']
cool_student.courses_in_progress += ['Git']
cool_student.finished_courses += ['Введение в программирование']


cool_rewiewer = Rewiewer('Tom', 'Berry')
angry_rewiewer = Rewiewer('Berg', 'Dust')
cool_rewiewer.courses_attached += ['Python']
cool_rewiewer.courses_attached += ['Git']
 
cool_rewiewer.rate_hw(best_student, 'Python', 9)
cool_rewiewer.rate_hw(best_student, 'Python', 10)
cool_rewiewer.rate_hw(best_student, 'Python', 10)
cool_rewiewer.rate_hw(best_student, 'Git', 9)
cool_rewiewer.rate_hw(best_student, 'Git', 10)
cool_rewiewer.rate_hw(best_student, 'Git', 10) 

cool_rewiewer.rate_hw(cool_student, 'Python', 6)
cool_rewiewer.rate_hw(cool_student, 'Python', 7)
cool_rewiewer.rate_hw(cool_student, 'Python', 9)
cool_rewiewer.rate_hw(cool_student, 'Git', 9)
cool_rewiewer.rate_hw(cool_student, 'Git', 4)
cool_rewiewer.rate_hw(cool_student, 'Git', 8) 


angry_rewiewer.courses_attached += ['Python']
angry_rewiewer.courses_attached += ['Git']
 
angry_rewiewer.rate_hw(best_student, 'Python', 5)
angry_rewiewer.rate_hw(best_student, 'Python', 7)
angry_rewiewer.rate_hw(best_student, 'Python', 7)
angry_rewiewer.rate_hw(best_student, 'Git', 8)
angry_rewiewer.rate_hw(best_student, 'Git', 5)
angry_rewiewer.rate_hw(best_student, 'Git', 6) 

angry_rewiewer.rate_hw(cool_student, 'Python', 4)
angry_rewiewer.rate_hw(cool_student, 'Python', 3)
angry_rewiewer.rate_hw(cool_student, 'Python', 2)
angry_rewiewer.rate_hw(cool_student, 'Git', 4)
angry_rewiewer.rate_hw(cool_student, 'Git', 5)
angry_rewiewer.rate_hw(cool_student, 'Git', 6) 

print(best_student.grades)

print(cool_student.grades)

cool_lecturer = Lecturer('Paul', 'Jojo')
mediocre_lecturer = Lecturer('Mary', 'Levis')
cool_lecturer.courses_attached_lect += ['Python']
cool_lecturer.courses_attached_lect += ['Git']
 
best_student.rate_le(cool_lecturer, 'Python', 9)
best_student.rate_le(cool_lecturer, 'Python', 10)
best_student.rate_le(cool_lecturer, 'Python', 10)
best_student.rate_le(cool_lecturer, 'Git', 9)
best_student.rate_le(cool_lecturer, 'Git', 10)
best_student.rate_le(cool_lecturer, 'Git', 10)

cool_student.rate_le(cool_lecturer, 'Python', 7)
cool_student.rate_le(cool_lecturer, 'Python', 6)
cool_student.rate_le(cool_lecturer, 'Python', 8)
cool_student.rate_le(cool_lecturer, 'Git', 9)
cool_student.rate_le(cool_lecturer, 'Git', 5)
cool_student.rate_le(cool_lecturer, 'Git', 10)


mediocre_lecturer.courses_attached_lect += ['Python']
mediocre_lecturer.courses_attached_lect += ['Git']
 
best_student.rate_le(mediocre_lecturer, 'Python', 5)
best_student.rate_le(mediocre_lecturer, 'Python', 6)
best_student.rate_le(mediocre_lecturer, 'Python', 4)
best_student.rate_le(mediocre_lecturer, 'Git', 5)
best_student.rate_le(mediocre_lecturer, 'Git', 4)
best_student.rate_le(mediocre_lecturer, 'Git', 5)

cool_student.rate_le(mediocre_lecturer, 'Python', 6)
cool_student.rate_le(mediocre_lecturer, 'Python', 6)
cool_student.rate_le(mediocre_lecturer, 'Python', 5)
cool_student.rate_le(mediocre_lecturer, 'Git', 3)
cool_student.rate_le(mediocre_lecturer, 'Git', 4)
cool_student.rate_le(mediocre_lecturer, 'Git', 6)

print()
print(cool_lecturer.courses_grades)
print()
print()
print(mediocre_lecturer.courses_grades)
print()
print()
print(cool_rewiewer)
print()
print()
print(angry_rewiewer)
print()
print()
print(cool_lecturer)
print()
print()
print(mediocre_lecturer)
print()
print()
print(best_student)
print()
print()
print(cool_student)
print()
print()
print(f'Результат сравнения студентов по средним оценкам: '
      f'{best_student.name} {best_student.surname} {"<" if best_student < cool_student  else (">" if best_student > cool_student else "=")} {cool_student.name} {cool_student.surname}')
print()

print()
print(f'Результат сравнения лекторов по средним оценкам: '
      f'{cool_lecturer.name} {cool_lecturer.surname} {"<" if cool_lecturer < mediocre_lecturer  else (">" if cool_lecturer > mediocre_lecturer else "=")} {mediocre_lecturer.name} {mediocre_lecturer.surname}')
print()

students_list=[best_student, cool_student]
lecturer_list=[cool_lecturer, mediocre_lecturer]
course_name= input('Введите название курса для вывода средней оценки: ')

def rating_st(students_list, course_name):
   grades_list=[]
   for student in students_list:
     grades_list.extend(student.grades.get(course_name, []))
   return sum(grades_list) / len(grades_list)

def rating_lc (lecturer_list, course_name):
   grades_list_lc=[]
   for lecturer in lecturer_list:
     grades_list_lc.extend(lecturer.courses_grades.get(course_name, []))
   return sum(grades_list_lc) / len(grades_list_lc)

print()
print(f"Средняя оценка для всех студентов по курсу {course_name}: {rating_st(students_list, course_name)}")
print()

print()
print(f"Средняя оценка для всех лекторов по курсу {course_name}: {rating_lc(lecturer_list, course_name)}")
print()
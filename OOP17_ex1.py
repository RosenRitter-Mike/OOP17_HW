import copy
import numpy as np
from abc import ABC, abstractmethod
from courses import Course


# Prototype Interface
class ICloneable(ABC):
    @abstractmethod
    def clone(self):
        pass


# Concrete Prototype Class
class Student(ICloneable):
    def __init__(self, name: str, id: str):
        self.name = name
        self.id = id
        self.grades: dict[int, float] = {}
        self.is_active = True

    def clone(self):
        student_clone = Student(self.name, self.id)
        student_clone.grades = self.grades.copy()
        return copy.deepcopy(self)  # ✅ Deep copy (fixes the problem)

    def add_grade(self, course_id: int, grade: float):
        self.grades.update({course_id: grade})

    def get_average_grade(self):
        if bool(self.grades):
            return np.mean(list(self.grades.values()))
        else:
            return 404

    def toggle_active_status(self):
        self.is_active = False

    def __str__(self):
        return f"Student(name={self.name}, id={self.id})\n(grades={self.grades})"


socar = Student("Socrates", "300")
socar.add_grade(Course.History.value, 80)
socar.add_grade(Course.Law.value, 85)
socar.add_grade(Course.Philosophy.value, 90)

print(socar)

aristo = socar.clone()
aristo.add_grade(Course.Sports.value, 85)
aristo.add_grade(Course.Physics.value, 75)
print("Socrates\n", socar,"\naverage grade= ", socar.get_average_grade())
print("Socrates copy\n", aristo,"\naverage grade= ", aristo.get_average_grade())
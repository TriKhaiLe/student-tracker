class Student:
    def __init__(self, name, age, math, literature, english):
        self.Id = None 
        self.name = name
        self.age = age
        self.math = float(math)
        self.literature = float(literature)
        self.english = float(english)
        self.average = self.calculate_average()
        self.rank = self.classify_grade()

    def calculate_average(self):
        return (self.math + self.literature + self.english) / 3

    def classify_grade(self):
        if self.average >= 8.0: return "Giỏi"
        elif self.average >= 6.5: return "Khá"
        elif self.average >= 5.0: return "Trung bình"
        else: return "Yếu"
def calculate_average(math, literature, english):
    return (math + literature + english) / 3

def classify_grade(average):
    if average >= 8.0:
        return "Gioi"
    elif average >= 6.5:
        return "Kha"
    elif average >= 5.0:
        return "Trung binh"
    else:
        return "Yeu"
    
def get_numeric_input(prompt, target_type=int):
    while True:
        try:
            return target_type(input(prompt))
        except ValueError:
            print("Loi: Vui long nhap dung dinh dang so! Thu lai.")


def input_students():
    student_list = []
    
    print("Nhap so luong hoc sinh:")
    N = get_numeric_input("So luong hoc sinh: ", int)
    
    for i in range(N):
        print(f"Nhap thong tin hoc sinh thu {i + 1}:")
        name = input("Ten: ")
        age = get_numeric_input("Tuoi: ", int)
        math = get_numeric_input("Diem Toan: ", float)
        literature = get_numeric_input("Diem Van: ", float)
        english = get_numeric_input("Diem Anh: ", float)

        student = {
            "name": name,
            "age": age,
            "math": math,
            "literature": literature,
            "english": english,
            "average": calculate_average(math, literature, english),
            "grade": classify_grade(calculate_average(math, literature, english))
        }
        student_list.append(student)

    return student_list

def display_students(student_list):
    print("\nDanh sach hoc sinh:")
    for student in student_list:
        print(f"Ten: {student['name']}, Tuoi: {student['age']}, Diem Toan: {student['math']}, Diem Van: {student['literature']}, Diem Anh: {student['english']}, Diem trung binh: {student['average']:.2f}, Xep loai: {student['grade']}")

def main():
    print("Chao mung den voi he thong Quan ly hoc sinh!")

    students = input_students()
    display_students(students)

if __name__ == "__main__":
    main()
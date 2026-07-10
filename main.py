import uuid

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
    
def get_text_input(prompt):
    while True:
        text_value = input(prompt)
        if not text_value:
            print("Loi: Gia tri khong hop le! Hay thu lai.")
        else:
            return text_value

def get_numeric_input(prompt, target_type=int):
    while True:
        try:
            return target_type(input(prompt))
        except ValueError:
            print("Loi: Vui long nhap dung dinh dang so! Hay thu lai.")

def input_students():
    student_list = []
    
    print("Nhap so luong hoc sinh:")
    N = get_numeric_input("So luong hoc sinh: ", int)
    
    for i in range(N):
        print(f"Nhap thong tin hoc sinh thu {i + 1}:")
        name = get_text_input("Ten: ")
        age = get_numeric_input("Tuoi: ", int)
        math = get_numeric_input("Diem Toan: ", float)
        literature = get_numeric_input("Diem Van: ", float)
        english = get_numeric_input("Diem Anh: ", float)

        student = {
            "id": str(uuid.uuid4())[:8],
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
        print(f"Id: {student['id']}, Ten: {student['name']}, Tuoi: {student['age']}, Diem Toan: {student['math']}, Diem Van: {student['literature']}, Diem Anh: {student['english']}, Diem trung binh: {student['average']:.2f}, Xep loai: {student['grade']}")

def search_student(student_list, search_query):
    search_results = []
    for student in student_list:
        if search_query.lower() in student['name'].lower():
            search_results.append(student)
    if search_results:
        display_students(search_results)
    else:
        print("Khong tim thay hoc sinh nay")

def main():
    print("Chao mung den voi he thong Quan ly hoc sinh!")
    while True:
        print("1. Them hoc sinh")
        print("2. Hien thi danh sach")
        print("3. Tim kiem")
        print("4. Sua thong tin")
        print("5. Xoa hoc sinh")
        print("6. Thoat")

        choice = get_numeric_input("Chon chuc nang (1-6): ", int)

        match choice:
            case 1:
                students = input_students()
            case 2:
                display_students(students)
            case 3:
                print("\n--- TIM KIEM ---")
                search_query = get_text_input("Nhap ten hoc sinh can tim: ")
                search_student(students, search_query)
            case 4:
                print("\n--- SUA THONG TIN ---")

            case 5:
                print("\n--- XOA HOC SINH ---")

            case 6:
                print("Cam on ban da su dung he thong!")
                break
            case _:
                print("Lua chon khong hop le! Vui long chon lai.")

if __name__ == "__main__":
    main()
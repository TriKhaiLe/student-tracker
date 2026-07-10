import tkinter as tk
from tkinter import ttk
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

def use_terminal():
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

def setup_gui():
    root = tk.Tk()
    root.title("Student Tracker")
    root.geometry("1000x600")

    tk.Label(root, text="Tên Học Sinh:").pack()
    name_entry = tk.Entry(root)
    name_entry.pack()

    tk.Label(root, text="Tuổi:").pack()
    age_entry = tk.Entry(root)
    age_entry.pack()

    tk.Label(root, text="Điểm Toán:").pack()
    math_entry = tk.Entry(root)
    math_entry.pack()

    tk.Label(root, text="Điểm Văn:").pack()
    literature_entry = tk.Entry(root)
    literature_entry.pack()

    tk.Label(root, text="Điểm Anh:").pack()
    english_entry = tk.Entry(root)
    english_entry.pack()

    def on_add_click():
        name = name_entry.get()
        age = age_entry.get()
        math = math_entry.get()
        literature = literature_entry.get()
        english = english_entry.get()
        print(f"Adding {name} (Age: {age}, Math: {math}, Literature: {literature}, English: {english})")

        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
        math_entry.delete(0, tk.END)
        literature_entry.delete(0, tk.END)
        english_entry.delete(0, tk.END)

    tk.Button(root, text="Thêm", command=on_add_click).pack()

    columns = ("name", "age", "math", "literature", "english", "average")
    tree = ttk.Treeview(root, columns=columns, show="headings")
    tree.heading("name", text="Tên")
    tree.heading("age", text="Tuổi")
    tree.heading("math", text="Điểm Toán")
    tree.heading("literature", text="Điểm Văn")
    tree.heading("english", text="Điểm Anh")
    tree.heading("average", text="Điểm TB")

    tree.column("name", width=150)
    tree.column("age", width=50)
    tree.column("math", width=100)
    tree.column("literature", width=100)
    tree.column("english", width=100)
    tree.column("average", width=100)
    tree.pack(fill="both", expand=True, padx=10, pady=10)
    
    root.mainloop()

def main():
    setup_gui()

if __name__ == "__main__":
    main()
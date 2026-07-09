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
            "english": english
        }
        student_list.append(student)

    return student_list


def main():
    print("Chao mung den voi he thong Quan ly hoc sinh!")

    input_students()

if __name__ == "__main__":
    main()
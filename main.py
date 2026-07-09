def input_students():
    student_list = []
    
    print("Nhap so luong hoc sinh:")
    N = int(input())
    
    for i in range(N):
        print(f"Nhap thong tin hoc sinh thu {i + 1}:")
        name = input("Ten: ")
        age = int(input("Tuoi: "))
        math = float(input("Diem Toan: "))
        literature = float(input("Diem Van: "))
        english = float(input("Diem Anh: "))

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
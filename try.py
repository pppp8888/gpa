def grade_to_point(grade):
    grade = grade.upper()
    if grade == "A":
        return 4.0
    elif grade == "B+":
        return 3.5
    elif grade == "B":
        return 3.0
    elif grade == "C+":
        return 2.5
    elif grade == "C":
        return 2.0
    elif grade == "D+":
        return 1.5
    elif grade == "D":
        return 1.0
    elif grade == "F":
        return 0.0
    else:
        return None

def main():
    total_points = 0.0
    total_credits = 0

    num_subjects = int(input("กรอกจำนวนวิชา: "))

    for i in range(num_subjects):
        print(f"\nวิชา {i+1}")
        grade = input("เกรด (A, B+, B, C+, C, D+, D, F): ")
        credit = float(input("หน่วยกิต: "))

        point = grade_to_point(grade)

        if point is None:
            print("เกรดไม่ถูกต้อง ลองใหม่อีกครั้ง")
            continue

        total_points += point * credit
        total_credits += credit

    if total_credits == 0:
        print("ไม่มีหน่วยกิต ไม่สามารถคำนวณ GPA ได้")
    else:
        gpa = total_points / total_credits
        print(f"\nGPA ของคุณคือ: {gpa:.2f}")

if __name__ == "__main__":
    main()

import StudentClass as S

def main():
    student = S.Student("1234","Andrew","10/12/2002", "Sr")

    student.calc_age()
    student.calc_register_date()

    print(f"Age: {student.get_age()}")
    print(f"Registration Dates: {student.get_register()}")

main()
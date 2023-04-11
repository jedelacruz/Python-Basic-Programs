while True:
    print()
    print("================= GRADES CALCULATOR =================")
    print()
    mathEnterGrade = int(input("Enter your grade in General Mathematics: "))
    filipinoEnterGrade = int(input("Enter your grade in Filipino: "))
    englishEnterGrade = int(input("Enter your grade in Oral Communication: "))
    scienceEnterGrade = int(input("Enter your grade in Earth and Life Science: "))
    programmingEnterGrade = int(input("Enter your grade in JAVA 2 Programming: "))
    conceptsEnterGrade = int(input("Enter your grade in Computer Concepts: "))
    emptechEnterGrade = int(input("Enter your grade in Empowerment Technology: "))
    philosophyEnterGrade = int(input("Enter your grade in Philosophy: "))
    peEnterGrade = int(input("Enter your grade in Physical Education: "))

    finalGrade = (mathEnterGrade + filipinoEnterGrade + englishEnterGrade + scienceEnterGrade + programmingEnterGrade + conceptsEnterGrade + emptechEnterGrade + philosophyEnterGrade + peEnterGrade) / 9

    print()
    print("Final grade: " + str(round(finalGrade)))

    if finalGrade > 100 or finalGrade <= 50:
        print("Invalid grade")
    elif finalGrade >= 98:
        print("With Highest Honors")
    elif finalGrade >= 95:
        print("With High Honors")
    elif finalGrade >= 90:
        print("With Honors")
    elif finalGrade >= 75:
        print("Passed")
    elif finalGrade >= 51:
        print("Failed")

    print()
    repeat = input("Do you want to use the program again? (yes/no) ")
    if repeat.lower() == "no":
        break

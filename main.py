import re
import os
from time import sleep


class Student:
    def __init__(self, name, surname, mail, number):
        self.name = name
        self.surname = surname
        self.mail = mail
        self.number = number


def studCodeCheck():  # I used same lines of code 2-3 times that's why changed to func
    while True:
        studentCode = input("Please enter 3 digit Student Code: ")
        if studentCode.isdigit():
            if 1 <= int(studentCode) / 100 < 10:
                break
            else:
                print("Error! Student Code should not be more than 3 digit!\n Please try again!\n")
        else:
            print("\nPlease use numeric value! Try again!")
    return studentCode


def studCodeCheck2(studCode):
    while True:
        if studentCodeCheck2.isdigit():
            if 1 <= int(studentCodeCheck2) / 100 < 10:
                break
            else:
                print("Error! Student Code should not be more than 3 digit!\n Please try again!\n")
        else:
            print("\nPlease use numeric value! Try again!")

    for check, check1 in enumerate(studentCodeArr):
        if check1 == studentCodeCheck2:
            index = check

    return index


studentInfo = {}
times = 0
i = 1
studentCodeArr = []

while True:
    print("\t\tWelcome!")
    print("1. Add Student Info")
    print("2. Delete Student Info")
    print("3. Update Student Info")
    print("4. Show Specific Student Info")
    print("5. Show All Student Info")
    print(("6. Exit\n"))

    choice = int(input("\nPlease enter your choice: "))

    if choice == 1:
        # i = 1
        # studentCodeArr = [None] * i

        while True:
            times = int(input("How many students you want to add?\tNOTE: MAX NUMBER IS 10\n\t\tInput:"))
            if times < 10:
                break
            else:
                print("Try again and read NOTE carefully!")

        j = 1
        for i in range(0, times):

            studentCode = studCodeCheck()

            studentCodeArr.append(studentCode)

            while True:
                name = input("\nPlease enter student name: ")
                if name.isdigit():  # type(name) != "str":
                    print("Error! Student name should include only ALPHABETIC characters!\n Please try again!")

                    if len(name) > 12:
                        print("Do really your student's name has more than 12 character?")
                        ans = input("Y or N: ")

                        if ans == "N":
                            print("Please try again!")
                        else:
                            print("Sorry, go on and try again!")
                            name = input("Please enter student name: ")

                            if name.isdigit():
                                print(
                                    "Error! Student name should include only ALPHABETIC characters!\n Please try again!")
                            else:
                                break
                else:
                    break

            while True:
                surname = input("\nPlease enter student surname: ")

                if surname.isdigit():  # type(surname) != "str":
                    print("Error! Student surname should include only ALPHABETIC characters!\n Please try again!")

                    if len(surname) > 12:
                        print("Do really your student's surname has more than 12 character?")
                        ans = input("Y or N: ")

                        if ans == "N":
                            print("Please try again!")
                        else:
                            print("Sorry, go on and try again!")
                            name = input("Please enter student surname: ")

                            if surname.isdigit():  # type(surname) != "str":
                                print(
                                    "Error! Student surname should include only ALPHABETIC characters!\n Please try again!")
                            else:
                                break
                else:
                    break

            # for validating an Email; custom mails use: '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
            regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

            while True:
                mail = input("\nPlease enter student e-mail: ")
                if re.search(regex, mail):
                    break
                else:
                    print("Invalid Email! Please try again!")

            while True:
                number = input("\nPlease enter student phone number: ")
                numberCheck = number[1:13]

                if len(number) == 13:
                    if number.startswith("+994"):
                        if numberCheck.isdigit:
                            break
                        else:
                            print("Phone number should include only digits!")
                    else:
                        print("Please enter your phone number with valid opcode (+994)!")
                else:
                    print("Invalid phone number length! (Note: it should be 12 digit with opcode)\nPlease try again!")

            studentInfo[studentCode] = Student(name, surname, mail, number)

            print("%d. student added to system successfully !\n " % j)
            j += 1
            i += 1

            sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')  # wanted as sys(clear)

    elif choice == 2:

        studentCodeCheck2 = input("Please enter the Student Code you want to delete: ")

        arrIndex = studCodeCheck2(studentCodeCheck2)

        studentCodeArr.pop(arrIndex)
        print("Student removed successfully!")

        sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')

    elif choice == 3:

        studentCodeCheck2 = input("Please enter the Student Code you want to update: ")
        arrIndex = studCodeCheck2(studentCodeCheck2)

        print(studentInfo.get(studentCodeArr[arrIndex]).name)
        change = input("What you want to update? (name, surname, email, phone): ")

        if change == "name":
            while True:
                nameCh = input("Please enter NEW name: ")
                if studentInfo[studentCodeArr[arrIndex]].name == nameCh:
                    print("\nNames are same! Please enter new one!")
                else:
                    studentInfo[studentCodeArr[arrIndex]].name = nameCh
                    print("Student's name successfully updated!")
                    break

        elif change == "surname":
            while True:
                surnameCh = input("Please enter NEW surname: ")
                if studentInfo[studentCodeArr[arrIndex]].surname == surnameCh:
                    print("\nSurnames are same! Please enter new one!")
                else:
                    studentInfo[studentCodeArr[arrIndex]].surname = surnameCh
                    print("Surname successfully updated!")
                    break

        elif change == "email":
            while True:
                mailCh = input("Please enter NEW email: ")
                if studentInfo[studentCodeArr[arrIndex]].mail == mailCh:
                    print("\nMails are same! Please enter new one!")
                else:
                    studentInfo[studentCodeArr[arrIndex]].mail = mailCh
                    print("\nMail successfully updated!")
                    break

        else:
            while True:
                phoneCh = input("Please enter NEW phone number")
                if studentInfo[studentCodeArr[arrIndex]].number == phoneCh:
                    print("\nPhone numbers are same! Please enter new one!")
                else:
                    studentInfo[studentCodeArr[arrIndex]].number = phoneCh
                    print("\nPhone number successfully updated!")
                    break

        sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')

    elif choice == 4:

        studentCodeCheck2 = input("Please enter the Student Code you want to view: ")
        arrIndex = studCodeCheck2(studentCodeCheck2)

        print(f"\n\nStudent's Student Code: {studentCodeCheck2}\n")
        print(f"Student's Name: {studentInfo[studentCodeArr[arrIndex]].name}")
        print(f"Student's Surname: {studentInfo[studentCodeArr[arrIndex]].surname}")
        print(f"Student's Mail Address: {studentInfo[studentCodeArr[arrIndex]].mail}")
        print(f"Student's Phone Number: {studentInfo[studentCodeArr[arrIndex]].number}")

        sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')

    elif choice == 5:
        for x in range(0, len(studentInfo)):
            print(f"\nStudent's Student Code: {studentCodeArr[x]}\n")
            print(f"Student's Name: {studentInfo[studentCodeArr[x]].name}")
            print(f"Student's Surname: {studentInfo[studentCodeArr[x]].surname}")
            print(f"Student's Mail Address: {studentInfo[studentCodeArr[x]].mail}")
            print(f"Student's Phone Number: {studentInfo[studentCodeArr[x]].number}\n")

        sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')

    elif choice == 6:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Thank you, Goodbye!")
        exit(0)

    else:
        print("Invalid choice!")

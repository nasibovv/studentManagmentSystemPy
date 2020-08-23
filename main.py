import re


class Student:
    def __init__(self, name, surname, mail, number):
        self.name = name
        self.surname = surname
        self.mail = mail
        self.number = number


print("\t\tWelcome!")
print("1. Add Student Info")
print("2. Delete Student Info")
print("3. Update Student Info")
print("4. Show Specific Student Info")
print("5. Show All Student Info")

choice = int(input("\nPlease enter your choice: "))

studentInfo = {}
# obj = Student('', '', '', 0)
times = 0

if choice == 1:
    i = 1

    while True:
        times = int(input("How many students you want to add?\tNOTE: MAX NUMBER IS 10\n\t\tInput:"))
        if times < 10:
            break
        else:
            print("Try again and read NOTE carefully!")

    for i in range(0, times):

        while True:
            studentCode = input("Please enter 3 digit Student Code: ")
            if studentCode.isdigit():
                if 1 <= int(studentCode) / 100 < 10:
                    break
                else:
                    print("Error! Student Code should not be more than 3 digit!\n Please try again!\n")
                    # x = False
            else:
                print("\nPlease use numeric value! Try again!")

        while True:
            name = input("\nPlease enter student name: ")
            if name.isdigit():  # type(name) != "str":
                print("Error! Student name should include only ALPHABETIC characters!\n Please try again!")

                if len(name) > 12:
                    print("Do really your student's name has more than 12 character?")
                    ans = input("Y or N: ")

                    if ans == "N":
                        print("Please try again!")
                        # x = True
                        # break
                    else:
                        print("Sorry, go on and try again!")
                        name = input("Please enter student name: ")

                        if name.isdigit():
                            print(
                                "Error! Student surname should include only ALPHABETIC characters!\n Please try again!")
                            # x = True
                        else:
                            break
            else:
                break

        while True:
            surname = input("\nPlease enter student surname: ")

            if surname.isdigit():  # type(surname) != "str":
                print("Error! Student surname should include only ALPHABETIC characters!\n Please try again!")

                if len(surname) > 12:
                    print("Do really your student's name has more than 12 character?")
                    ans = input("Y or N: ")

                    if ans == "N":
                        print("Please try again!")
                        # x = False
                        # break
                    else:
                        print("Sorry, go on and try again!")
                        name = input("Please enter student name: ")

                        if type(surname) != "str":
                            print(
                                "Error! Student surname should include only ALPHABETIC characters!\n Please try again!")
                            # x = False
                        else:
                            # x = True
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
                        print(number[1:12])
                        break
                    else:
                        print("Phone number should include only digits!")
                else:
                    print("Please enter your phone number with valid opcode (+994)!")
            else:
                print("Invalid phone number length! (Note: it should be 12 digit with opcode)\nPlease try again!")

        studentInfo[studentCode] = Student(name, surname, mail, number)

        print("{}. student added to system successfully !\n ".format(i))
        i += 1

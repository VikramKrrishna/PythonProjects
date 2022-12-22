from statistics import mean as m

admins = {'Python':'pass123@','User1':'pass@1'}

studentDict = {"marcus":[90,78,86],
               "sasha":[99,87,92],
               "martin":[98,96,95],
               "saha":[89,94,87]
               }

def enterGrades():
    nameToEnter = input("Student Name: ")
    gradeToEnter = input("Grade: ")

    if nameToEnter in studentDict:
        print('Adding Grades...')
        studentDict[nameToEnter].append(float(gradeToEnter))
    else:
        print('Student does not exit')

    print(studentDict)

def removeStudent():
    nameToRemove = input('What student to Remove?: ')
    if nameToRemove in studentDict:
        print('Removing student...')
        del studentDict[nameToRemove]
    else:
        print("Invalid Student Name")
    print(studentDict)

def studentAVGs():
    for eachStudent in studentDict:
        gradeList = studentDict[eachStudent]
        avgGrade = m(gradeList)
        print(eachStudent,'has an average Grade of: ',avgGrade)

def main():
    print("""
    Welcome to Grade Central
    
    [1] - Enter Grades
    [2] - Remove Student
    [3] - Student Average Grades
    [4] - Exit
    
    """)
    action = input('What would you like to do today? (Enter a number): ')

    if action == '1':
        enterGrades()
    elif action == '2':
        removeStudent()
    elif action == '3':
        studentAVGs()
    elif action == '4':
        exit()
    else:
        print('No valid choice was given, try again')


login = input("Username: ")
Passw = input("Password: ")

if login in admins:
    if admins[login] == Passw:
        print('Welcome',login)
        while True:
            main()
    else:
        print('Invalid Password, will denote in 5 seconds!')
else:
    print('Invalid Username, Enter correct Username')
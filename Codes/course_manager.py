MINIMUM_NAME_LENGTH = 4

def checkStudentName(name):
    if len(name) < MINIMUM_NAME_LENGTH:
        print("Student name is less than {} characters, try again.".format(MINIMUM_NAME_LENGTH))
        return False
    else:
        return True
    

def getStudentNames(studentSet):
    newStudents = set()
    nextStudentName = input("\nEnter the student's name or '*' to finish: ")
    
    while nextStudentName[0] != '*':
        if checkStudentName(nextStudentName) :
            newStudents.add(nextStudentName)
        nextStudentName = input("\nEnter the student's name or '*' to finish: ")
    
    return studentSet.union(newStudents)


def displayClassNames(className, studentSet):
    print("\nClass: ", className)
    if len(studentSet) == 0:
        print("\tThere are no students in this class.")
    else:
        for student in sorted(studentSet):
            print("\t", student)


def main():
    
    studentNameSet = set()
    
    courseCode = input("Enter the course code: ")
    
    finalStudentNameSet = getStudentNames(studentNameSet)
            
    displayClassNames(courseCode, finalStudentNameSet)


if __name__ == "__main__":
    main()

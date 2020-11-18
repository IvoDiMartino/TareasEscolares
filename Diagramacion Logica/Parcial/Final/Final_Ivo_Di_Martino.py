# 1) Realizar una función que permita la carga de n alumnos. Por cada alumno se deberá preguntar el nombre
#  completo y permitir el ingreso de 3 notas . Las notas deben estar comprendidas entre 0 y 10. Devolver el
#  listado de alumnos.
#
# 2) Definir una función que dado un listado de alumnos evalúe cuántos aprobaron y cuantos desaprobaron,
#  teniendo en cuenta que se aprueba con 4. La nota será el promedio de las 3 notas para cada alumno.
#
# 3) Informar el promedio de nota del curso total. 
#
# 4) Realizar una función que indique quien tuvo el promedio más alto y quien tuvo la nota promedio más baja.
#
# 5) Realizar una función que permita buscar un alumno por nombre, siendo el nombre completo o parcial,
#  y devuelva una lista con los n alumnos que concuerden con ese nombre junto con todos sus datos, incluido el
#  promedio de sus notas.

def studentNotes():
    studentsTotal = []
    validNotes = False
    goingOn = ""

    while True:
        studentsList = {}
        studentsList["fullName"] = str(input("Por favor, ingrese nombre completo: "))
        while validNotes == False:
            studentsList["firstNote"] = int(input("Por favor, ingrese la primer nota: "))
            if studentsList["firstNote"] in range(0,11):
                break
        while validNotes == False:
            studentsList["secondNote"] = int(input("A continuación, ingrese la segunda nota: "))
            if studentsList["secondNote"] in range(0,11):
                break
        while validNotes == False:
            studentsList["thirdNote"] = int(input("Finalmente, ingrese la tercer nota: "))
            if studentsList["thirdNote"] in range(0,11):
                break

        studentsList["averageNote"] = (
            studentsList["firstNote"]
         + studentsList["secondNote"]
         + studentsList["thirdNote"]
         )/3

        studentsTotal.append(studentsList)

        goingOn = str(input("Alumno añadido con éxito. ¿Desea proseguir con el listado?: ")).lower()
        if goingOn == "no":
            break

    return studentsTotal

def studentsAverage(studentsTotal):
    bestNotes = []
    worstNotes = []

    for student in studentsTotal:
        if student["averageNote"] >= 4:
            bestNotes.append(student)
        else:
            worstNotes.append(student)

    print(f"Los alumnos aprobados fueron: {bestNotes} y los desaprobados fueron: {worstNotes}")
    return bestNotes, worstNotes

def courseAverage(studentsTotal):
    totalStudents = 0

    for student in studentsTotal:
        totalStudents += student["averageNote"]

    totalAverage = totalStudents / len(studentsTotal)

    print(f"El promedio total del curso fue de: {totalAverage}")
    return totalAverage


def bestWorseStudent(studentsTotal):
    bestStudent = studentsTotal[0] 
    worstStudent = studentsTotal[0]

    for averageNote in studentsTotal:
        if averageNote["averageNote"] > bestStudent["averageNote"]:
            bestStudent = averageNote
            
        if averageNote["averageNote"] < worstStudent["averageNote"]:
            worstStudent = averageNote

    print(f"El alumno más destacado fue: {bestStudent} y el menos destacado fue: {worstStudent}")
    return bestStudent, worstStudent

def lookupStudent(studentsTotal):

    while True:
        studentList = []
        nameEntered = str(input("Por favor, ingrese el nombre del alumno: "))

        for student in studentsTotal:
            if nameEntered in student["fullName"]:
                studentList.append(student)
                
        print(f"Resultados de busqueda: {studentList}")

        goingOn = str(input("Alumno encontrado. ¿Desea proseguir con su busqueda?: ")).lower()
        if goingOn == "no":
            break    


    return studentList



print("---------- Listado de Alumnos -----------")
studentsTotal = studentNotes()

print ("\n--- Alumnos Aprobados y Desaprobados  ---")
studentsAverage(studentsTotal)

print("---------- Promedio del Curso -----------")
courseAverage(studentsTotal)

print("---------- Alumno más sobresaliente y menos sobresaliente ----------")
bestWorse = bestWorseStudent(studentsTotal)

print("---------- Buscador de Alumnos ----------")
lookupStudent(studentsTotal)
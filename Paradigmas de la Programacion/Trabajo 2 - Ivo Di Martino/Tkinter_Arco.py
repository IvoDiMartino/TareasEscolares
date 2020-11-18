import itertools
import csv
from openpyxl import Workbook
from tkinter import Tk, Label, Entry, Button, messagebox, Radiobutton, Checkbutton
from tkinter import IntVar, StringVar
import Tkinter_Funciones as function

## Funciones de Guardado
challengeData = []
countID = itertools.count(1)

def saveData():
    id = next(countID)
    firstName = entry_firstName.get()
    lastName = entry_lastName.get()
    age = int(entry_age.get())
    gender = genderSelect()
    firstShot = int(entry_firstShot.get())
    secondShot = int(entry_secondShot.get())
    thirdShot = int(entry_thirdShot.get())

    shots = [firstShot, secondShot, thirdShot]
    bestShot = function.bestShotData(shots)

    participantsList = [id, firstName, lastName, age, gender, firstShot, secondShot, thirdShot, bestShot]
    challengeData.append(participantsList)
    print(participantsList)

    with open('participantes.csv', 'a') as csvfile:
        obj = csv.writer(csvfile)
        obj.writerow(participantsList)
    print("Generando reporte .csv")

    deleteData()

def deleteData():
    entry_firstName.delete(0, 'end')
    entry_lastName.delete(0, 'end')
    entry_age.delete(0, 'end')
    entry_firstShot.delete(0, 'end')
    entry_secondShot.delete(0, 'end')
    entry_thirdShot.delete(0, 'end')

def exportData():
    workbook = Workbook()
    sheet = workbook.active

    title = ['Listado de participantes - Mejor disparo']
    sheet.append(title)

    headers = ['ID', 'Nombre', 'Apellido', 'Edad', 'Género', 'Disparo 1', 'Disparo 2', 'Disparo 3', 'Mejor Disparo']
    sheet.append(headers)

    orderedData = function.winnerData(challengeData)

    for participant in orderedData:
        sheet.append(participant)
    
    workbook.save(filename='registro_participantes.xlsx')
    print("Generando reporte .xlsx")
    
    deleteData()

def genderSelect():
    gender = opcion.get()
    if (gender == 1):
        genderSelection = 'Masculino'
    else:
        genderSelection = 'Femenino'

    return genderSelection

def winner():
    bestParticipant = function.winnerData(challengeData)
    winner = bestParticipant[0]

    print("El ganador es: ", winner)
    messagebox.showinfo("El ganador es", winner)

    return bestParticipant

## Parámetros de Tkinter
# Configuración de raíz
root = Tk()

# Configuración del título
root.title("Concurso de Tiro con Arco")
root.config(width=430, height=400)

# Configuración de etiquetas
label_firstName = Label(root, text='Nombre', font='Arial 12')
label_firstName.place(x=5, y=10)

label_lastName = Label(root, text='Apellido', font='Arial 12')
label_lastName.place(x=5, y=50)

label_age = Label(root, text='Edad', font='Arial 12')
label_age.place(x=5, y=100)

label_gender = Label(root, text='Sexo', font='Arial 12')
label_gender.place(x=5, y=160)
opcion = IntVar()

label_firstShot = Label(root, text='Disparo 1', font='Arial 12')
label_firstShot.place(x=5, y=200)

label_secondShot = Label(root, text='Disparo 2', font='Arial 12')
label_secondShot.place(x=5, y=250)

label_thirdShot = Label(root, text='Disparo 3', font='Arial 12')
label_thirdShot.place(x=5, y=300)

btn_save = Button(root, text='Guardar', command=saveData)
btn_save.place(x=50, y=350)

btn_winner = Button(root, text='Ganador', command=winner)
btn_winner.place(x=150, y=350)

btn_export = Button(root, text='Exportar xls', command=exportData)
btn_export.place(x=250, y=350)

# Configuración de casillas
entry_firstName = Entry(root, width=50)
entry_firstName.place(x=100, y=10)

entry_lastName = Entry(root, width=50)
entry_lastName.place(x=100, y=50)

entry_age = Entry(root, width=50)
entry_age.place(x=100, y=100)

rd_male = Radiobutton(root, text='Masculino', variable=opcion, value=1, command=genderSelect, font='Arial 10')
rd_male.place(x=50, y=160)
rd_female = Radiobutton(root, text='Femenino', variable=opcion, value=2, command=genderSelect, font='Arial 10')
rd_female.place(x=150, y=160)

entry_firstShot = Entry(root, width=50)
entry_firstShot.place(x=100, y=200)

entry_secondShot = Entry(root, width=50)
entry_secondShot.place(x=100, y=250)

entry_thirdShot = Entry(root, width=50)
entry_thirdShot.place(x=100, y=300)


root.mainloop()

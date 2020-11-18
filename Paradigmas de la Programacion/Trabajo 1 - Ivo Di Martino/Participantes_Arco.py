import Funciones_Arco
import csv

participantData = Funciones_Arco.challengeMember()
bestParticipants = Funciones_Arco.bestFinalists(participantData)
lastParticipant = Funciones_Arco.lastParticipant(participantData)
genderParticipants = Funciones_Arco.countGender(participantData)
ageParticipants = Funciones_Arco.countAgeOrder(participantData)
averageParticipants = Funciones_Arco.totalAverage(participantData)
totalAverage = Funciones_Arco.outstandingParticipants(participantData, averageParticipants)

print("\n-- Listado de participantes --")
with open("participantes.csv", "w",  newline='') as csvfile:
    obj = csv.writer(csvfile)
    obj.writerow({'Listado de participantes'})
with open('participantes.csv', 'a', newline='') as csvfile:
    fieldnames = ['id','firstname','lastname','age','gender','shots','bestShot','averageShot']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    print ("ID    Nombre    Apellido    Edad    Género    Disparos    Mejor Disparo    Disparo Promedio") 
    for i in range(len(participantData)):
        print(participantData[i]['id'],"    ", participantData[i]['firstname'],"    ", participantData[i]['lastname'],"    ", participantData[i]['age'],"   ", participantData[i]['gender'],"   ", participantData[i]['shots'],"    ", participantData[i]['bestShot'],"    ", participantData[i]['averageShot'])
        writer.writerow(participantData[i])

print("\n-- Tres mejores participantes --") 
with open("participantes.csv", "a", newline='') as csvfile:
    obj = csv.writer(csvfile)
    obj.writerow({'\nTres mejores participantes'})
with open('participantes.csv', 'a', newline='') as csvfile:
    fieldnames = ['id','firstname','lastname','bestshot']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames,extrasaction='ignore')
    writer.writeheader()
    print ("ID    Nombre    Apellido    Mejor Disparo    Disparo Promedio") 
    for i in range(3):
        print(bestParticipants[i]['id'],"    ", bestParticipants[i]['firstname'],"    ", bestParticipants[i]['lastname'],"   ", bestParticipants[i]['bestShot'],"   ", bestParticipants[i]['averageShot'])
        writer.writerow(bestParticipants[i])

print("\n-- Último participante --") 
with open('participantes.csv', 'a', newline='') as csvfile:
    obj = csv.writer(csvfile)
    obj.writerow({'\nEl participante que salio ultimo fue'})
with open('participantes.csv', 'a', newline='') as csvfile:
    fieldnames = ['id','firstname','lastname','bestshot']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames,extrasaction='ignore')
    writer.writeheader()
    print ("ID    Nombre    Apellido    Mejor Disparo") 
    print(lastParticipant['id'],"    ", lastParticipant['firstname'],"    ", lastParticipant['lastname'],"    ", lastParticipant['bestShot'])
    writer.writerow(lastParticipant)

print("\n-- Listado de cantidad de participantes --")
with open('participantes.csv', 'a', newline='') as csvfile:
    obj = csv.writer(csvfile)
    obj.writerow({'\nCantidad de participantes: '})
    obj.writerow({len(participantData)})
    print (len(participantData))

print("\n-- Listado de participantes varones --") 
with open('participantes.csv', 'a', newline='') as csvfile:
    obj = csv.writer(csvfile)
    obj.writerow({'\nCantidad de participantes varones: '})
    obj.writerow({genderParticipants[0]})
    print(genderParticipants[0])

print("\n-- Edad promedio de participantes mujeres --")
with open('participantes.csv', 'a', newline='') as csvfile:
    obj = csv.writer(csvfile)
    obj.writerow({'\nEdad promedio de participantes mujeres: '})
    obj.writerow({genderParticipants[1]})
    print(genderParticipants[1])

print("\n-- Participantes ordenados por edad --") 
with open('participantes.csv', 'a', newline='') as csvfile:
    obj = csv.writer(csvfile)
    obj.writerow({'\nListado de participantes por edad '})
with open('participantes.csv', 'a', newline='') as csvfile:
    fieldnames = ['id','firstname','lastname','age','gender','shots','bestShot','averageShot']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    print ("ID    Nombre    Apellido    Edad   Género   Disparos    Mejor Disparo    Disparo Promedio") 
    for i in range(len(ageParticipants)):
        print(ageParticipants[i]['id'],"    ", participantData[i]['firstname'],"    ", participantData[i]['lastname'],"    ", participantData[i]['age'],"   ", participantData[i]['gender'],"   ", participantData[i]['shots'],"    ", participantData[i]['bestShot'],"    ", participantData[i]['averageShot'])
        writer.writerow(ageParticipants[i])

print("\n--Promedio de los disparos: --") 
with open('participantes.csv', 'a', newline='') as csvfile:
    obj = csv.writer(csvfile)
    obj.writerow({'\nPromedio de los disparos: '})
    print(averageParticipants)
    obj.writerow({averageParticipants})

print("\n-- Participantes por encima del promedio --") 
with open('participantes.csv', 'a', newline='') as csvfile:
    obj = csv.writer(csvfile)
    obj.writerow({'\nParticipantes por encima del promedio: '})
with open('participantes.csv', 'a', newline='') as csvfile:
    fieldnames = ['id','firstname','lastname','age','gender','shots','bestShot','averageShot']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    print("ID    Nombre    Apellido    Edad    Género    Disparos    Mejor Disparo    Disparo Promedio")
    for i in range(len(totalAverage)):
        print(totalAverage[i]['id'],"    ", totalAverage[i]['firstname'],"    ", totalAverage[i]['lastname'],"    ", totalAverage[i]['age'],"   ", totalAverage[i]['gender'],"   ", totalAverage[i]['shots'],"    ", totalAverage[i]['bestShot'],"    ", totalAverage[i]['averageShot'])
        writer.writerow(totalAverage[i])

csvfile.close()
import math
import random

shotsCount = 3
finalistCount = 3

# Función para añadir participantes, se cancela escribiendo 999 en la ID, los disparos son colocados
# de forma automática para comprobar sus funcionalidad
def challengeMember():
    participantsList = []

    while True:
        participantData = {}
        participantData["id"] = int(input("\nIngrese el id del participante: "))
        if (participantData["id"] == 999):
            break
        participantData["firstname"] = str(input("\nIngrese nombre del participante: "))
        participantData["lastname"] = str(input("\nIngrese apellido del participante: "))
        participantData["age"] = int(input("\nIngrese edad del participante: "))
        participantData["gender"] = str(input("\nIngrese género de participante (M para Masculino, F para Femenino): ")).upper()
        shots = []

        for _ in range(shotsCount):
            vertX = (random.random()*160)-80
            vertY = (random.random()*160)-80
            shots.append(calculateDistance(vertX,vertY))

        participantData["shots"] = shots
        bestAverageShot = bestAndAverageShot(shots)
        participantData["bestShot"] = bestAverageShot[0]
        participantData["averageShot"] = bestAverageShot[1]
        participantsList.append(participantData)

    return participantsList

# Se calcula la distancia de los disparos en base a los números elegidos de manera automática por
# el algoritmo y el radio de la diana.
def calculateDistance(x,y):
    Distance = math.sqrt(x**2 + y**2)

    return round(Distance, 0)

# Se elige el mejor disparo efectuado junto con el promedio, usando 999 como máximo para dar
#  posibilidad de reuso por si la diana cambia
def bestAndAverageShot(shots):
    bestAndAverageShot = []

    counter = 0
    bestShot = 999
    for trial in range(shotsCount):
        counter = shots[trial] + counter
        if shots[trial] < bestShot:
            bestShot = shots[trial]
    
        averageShot = round(counter / shotsCount, 0)
        bestAndAverageShot.append(bestShot)
        bestAndAverageShot.append(averageShot)

    return bestAndAverageShot

# Se calcula a los mejores finalistas en base al mejor disparo y, posteriormente, al disparo promedio
# para finalmente entregarlos en un listado inverso, así se muestran de mayor a menor.
def bestFinalists(participantsList):
    bestParticipants = sorted(participantsList, key=lambda k: k["bestShot"])
    bestParticipants = sorted(participantsList, key=lambda k: k["averageShot"])
    bestParticipants.reverse()
    FinalistList = []
    for finalist in range(finalistCount):
        FinalistList.append(bestParticipants[finalist])

    return FinalistList

# Se ordena una lista en base al mejor disparo y, psoterior mente, al disparo promedi
# y se devuelve al último de estos
def lastParticipant(participantsList):
    lastParticipant = sorted(participantsList, key=lambda k: k["bestShot"])
    lastParticipant = sorted(participantsList, key=lambda k: k["averageShot"])
    lastParticipant = lastParticipant[0]

    return lastParticipant

# Se realiza un conteo general de los participantes en base a su género, en caso de ser masculino se
# contean directamente. En caso femenino, se suman las edades en una variable que después se divide
# en base al conteo general.
def countGender(participantsList):
    totalMan = 0
    totalWomen = 0
    counter = 0
    for participant in participantsList:
        if participant["gender"] == "M":
            totalMan += 1
        elif participant["gender"] == "F":
            totalWomen += participant["age"]
            counter += 1
    averageWomen = (totalWomen / counter)
    
    return totalMan, averageWomen

# Se ordena una lista por edad, de menor a mayor.
def countAgeOrder(participantsList):
    ageOrderList = []
    ageOrderList = sorted(participantsList, key=lambda k: k["age"])

    return ageOrderList

# Se toma el promedio de cada participante, sumandolos en una sola variable para, finalmente,
# dividirlo en base al conteo general (guardado en counter), para formular finalmente el promedio general.
def totalAverage(participantsList):
    counter = 0
    parcipantAverage = 0
    for participante in participantsList:
        parcipantAverage += participante["averageShot"]
        counter += 1
    averageShot = (parcipantAverage / counter)

    return round(averageShot,0)

# Se toma la lista principal y el resultado del disparo promedio general, después se itera en base 
# al disparo promedio de cada uno, rellenando la lista con cada participante que supere el marcador general.
def outstandingParticipants(participantsList, totalAverage):
    bestAverage = []
    for participant in participantsList:
        if participant["averageShot"] > totalAverage:
            bestAverage.append(participant)
            
    return bestAverage

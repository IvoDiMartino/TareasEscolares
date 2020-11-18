## Funciones
shotsCount = 3
finalistCount = 1

def bestShotData(shots):
    bestShot = 999

    for trial in range(shotsCount):
        if shots[trial] < bestShot:
            bestShot = shots[trial]

    return bestShot

def winnerData(challengeData):
    orderedList = sorted(challengeData, key=lambda k: k[8])

    return orderedList
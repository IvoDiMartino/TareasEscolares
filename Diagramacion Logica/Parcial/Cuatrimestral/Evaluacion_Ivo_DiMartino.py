# En una cafetería desean actualizar su sistema de ventas de combos online. Los COMBOS son los siguientes:

# combo |           detalle            | precio
# -----------------------------------------------
#   1   | 1 infusion + 2 medialunas    | 120
#   2   | 1 infusion premium + 1 cookie| 130
#   3   | 2 infusiones + porcion torta | 280
#   4   | 2 infusiones + 2 cookies     | 210

# 1) escribir una función para la carga de las n ÓRDENES, deberá preguntar nombre completo, dirección y
#  combo elegido. Devolver una lista con todas las órdenes.
# 2) escribir una función que dado una lista de órdenes indique cuántas ventas tuvo por combo, informar
#  imprimiendo para que quede con el siguiente formato:
# Combo 1 vendido 2 veces
# Combo 2 vendido 1 veces
# Combo 3 vendido 3 veces
# ...
# 3) escribir una función que dado un nombre completo busque en la lista y devuelva todas las órdenes que
# tenga de esa persona
import time

orderTaken = []

def takeOrder():
    orderEnd = ""
    while orderEnd != "si":
        fullName = str(input("Por favor, ingrese nombre completo: "))
        address = str(input("Ingrese dirección de entrega: "))
        orderCombo = int(input("Ingrese el combo elegido (usando solo 1, 2, 3 o 4 según su elección): "))

        orderList = {"fullName":fullName, "address":address, "orderCombo":orderCombo}
        orderTaken.append(orderList)

        orderEnd = str(input("Orden añadida. ¿Desea terminar la operación? (Indique si o no): ").lower())

def quantityCombo(orderTaken):
    comboOne = 0
    comboTwo = 0
    comboThree = 0
    comboFour = 0

    for chosenCombo in orderTaken:
        if chosenCombo["orderCombo"] == 1:
            comboOne += 1
        if chosenCombo["orderCombo"] == 2:
            comboTwo += 1
        if chosenCombo["orderCombo"] == 3:
            comboThree += 1
        if chosenCombo["orderCombo"] == 4:
            comboFour += 1

    print(f"Combo 1 = vendido {comboOne} veces \nCombo 2 = vendido {comboTwo} veces \nCombo 3 = vendido {comboThree} veces \nCombo 4 = vendido {comboFour} veces")


def OrderforName(orderTaken):
    clientList = []
    nameSearch = str(input("Ingrese nombre completo del cilente a buscar: "))

    for nameEntered in orderTaken:
        if nameEntered["fullName"] == nameSearch:
            clientList.append(nameEntered["orderCombo"])

    print(f"Las ordenes pedidas, según cliente, son de los siguientes combos: {clientList}")

takeOrder()

print("---------- Resumen de Ventas -----------")
quantityCombo(orderTaken)

print("---------- Resumen de Ordenes -----------")
OrderforName(orderTaken)
time.sleep(3)
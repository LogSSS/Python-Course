import PrivatBank as pb
from prettytable import PrettyTable as pt


def inputNumb():
    while 1:
        try:
            numb = int(input("| Enter amount of money: "))
            if numb <= 0:
                print("| Enter a positive number!")
                continue
            break
        except ValueError:
            print("| Enter a number!")
    return numb


def getCourse():
    table = pt()
    table.field_names = ["Currency", "Base Currency", "Buy", "Sale"]
    for i in pb.getCourse():
        table.add_row([i["ccy"], i["base_ccy"], i["buy"], i["sale"]])
    return table


while 1:
    print(getCourse())
    print("| 1. Buy USD in UAH")
    print("| 2. Buy EURO in UAH")
    print("| 3. Sell USD for UAH")
    print("| 4. Sell EURO for UAH")
    print("| 5. Exit")
    option = input("| Select option: ")
    if option == "1":
        bob = inputNumb()
        print("| If u sell", bob, "USD, u will get", pb.USDtoUAH() * bob, "UAH")
        continue
    if option == "2":
        bob = inputNumb()
        print("| If u sell", bob, "EURO, u will get", pb.EURtoUAH() * bob, "UAH")
        continue
    if option == "3":
        bob = inputNumb()
        print("| If i wanna buy", bob, "USD, i need to pay", pb.UAHtoUSD() * bob, "UAH")
        continue
    if option == "4":
        bob = inputNumb()
        print("| If i wanna buy", bob, "EURO, i need to pay", pb.UAHtoEUR() * bob, "UAH")
        continue
    if option == "5":
        break
    print("| Wrong option!")

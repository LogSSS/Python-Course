products = [['Apple', 3.7],
            ['Banane', 9.4],
            ['Orange', 5.2],
            ['Mandarin', 7.3],
            ['Pineapple', 12.5],
            ['Grapefruit', 8.9],
            ['Lemon', 4.3]]

print("Menu:")
for i in products:
    print(i[0].ljust(10) + " | " + str(i[1]) + " UAH/kg")

buyDict = []
while 1:
    try:
        print("-" * 30)
        print("Enter the name of the product you want to buy (Enter \"buy\" if you want to buy the selected product)")
        prod = input()
        if prod.lower() == "buy":
            break
        print("Enter the quantity of goods (kg) you want to buy")
        howMuch = float(input())
        if howMuch <= 0:
            print("The quantity of goods in kilograms must be greater than zero")
            continue
        ifExist = False
        for i in products:
            if i[0].lower() == prod.lower():
                ifExistInCheck = False
                for j in buyDict:
                    if j[0] == i[0]:
                        j[1] = float(j[1]) + float(howMuch)
                        j[3] = float(j[1]) * i[1]
                    ifExistInCheck = True
                if not ifExistInCheck:
                    buyDict.append([i[0], howMuch, i[1], float(howMuch) * i[1]])
                ifExist = True
    except ValueError:
        print("The quantity of goods in kilograms must be a number")
        ifExist = True
    if not ifExist:
        print("Product not found")

print("-" * 30)
sum = 0
if len(buyDict) != 0:
    print("Your check")
    print("Product".ljust(20), "| Quantity of goods(kg)".ljust(20), "| Price per kg".ljust(22), "| Total cost(UAH)")
    for i in buyDict:
        print(str(i[0]).ljust(20), "|", str(i[1]).ljust(21), "|", str(i[2]).ljust(20), "|", i[3])
        sum += i[3]
    print("Total amount: " + str(sum) + " UAH")

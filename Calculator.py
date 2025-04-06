from fileinput import close

from CalculatorClass import Calculator

print("1. Default Calculator" + '\n' + "2. Custom Size Calculator" + '\n' + "3. Custom Size And Title Calculator")
choose = input("Selection: ")

calculator = ""
match(choose):
    case ("1"):
        calculator = Calculator()
    case "2":
        width = int(input("Width: "))
        height = int(input("Height: "))
        calculator = Calculator(width, height)

    case "3":
        title = input("Title: ")
        width = int(input("Width: "))
        height = int(input("Height: "))
        calculator = Calculator(title, width, height)
    case _:
        print("Not Valid Input.. program ending...")
        close()
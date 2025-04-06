import tkinter as tk
from tkinter import messagebox


# Builds Calculator
def calculatorBuilder(title, width, height):
    window = tk.Tk()

    # Sets Calculator Size (ex // 500x400) and Title
    sizeBuilder = str(width) + "x" + str(height)
    window.geometry(sizeBuilder)
    window.title(title)

    # Setting Other Properties
    window.resizable(False, False)

    # Button Event Handlers
    def btnOnePressed():
            result["text"] += "1"

    def btnTwoPressed():
            result["text"] += "2"

    def btnThreePressed():
            result["text"] += "3"

    def btnFourPressed():
            result["text"] += "4"

    def btnFivePressed():
            result["text"] += "5"

    def btnSixPressed():
            result["text"] += "6"

    def btnSevenPressed():
            result["text"] += "7"

    def btnEightPressed():
            result["text"] += "8"

    def btnNinePressed():
            result["text"] += "9"

    def btnZeroPressed():
            result["text"] += "0"

    def btnPlusPressed():
            result["text"] += "+"

    def btnSubtractPressed():
            result["text"] += "-"

    def btnMultiplyPressed():
            result["text"] += "x"

    def btnDividePressed():
            result["text"] += "/"

    def btnClearPressed():
            result["text"] = ""

    def btnEqualPressed():
        equation = result["text"]

        if equation == "":
            messagebox.showinfo("No Equation")

        # Addition
        if equation.find("+") > -1:
            equation = equation.split("+")
            num1 = float(equation[0])
            num2 = float(equation[1])
            result["text"] = str(num1 + num2)

        #Subtraction
        elif equation.find("-") > -1:
            equation = equation.split("-")
            num1 = float(equation[0])
            num2 = float(equation[1])
            result["text"] = str(num1 - num2)

        # Multiplication
        elif equation.find("x") > -1:
            equation = equation.split("x")
            num1 = float(equation[0])
            num2 = float(equation[1])
            result["text"] = str(num1 * num2)

        # Division
        elif equation.find("/") > -1:
            equation = equation.split("/")
            num1 = float(equation[0])
            num2 = float(equation[1])
            result["text"] = str(num1 / num2)

    # Result Display Label
    result = tk.Label(window, fg="black", font=("Arial", 20, "bold"), background="Light Grey", width=width, height=2)
    result.place(relx=0.5, rely=0.0, anchor=tk.N)

    # First Row Of Buttons
    button1 = tk.Button(window, text="1", fg="black", font=("Ariel", 12, "bold"), command=btnOnePressed)
    button1.place(relx=0.260, rely=0.3, anchor="center", width=50, height= 50)

    button2 = tk.Button(window, text="2", fg="black", font=("Ariel", 12, "bold"), command=btnTwoPressed)
    button2.place(relx=0.400, rely=0.3, anchor="center", width=50, height=50)

    button3 = tk.Button(window, text="3", fg="black", font=("Ariel", 12, "bold"), command=btnThreePressed)
    button3.place(relx=0.530, rely=0.3, anchor="center", width=50, height=50)

    buttonPlus = tk.Button(window, text="+", fg="black", font=("Ariel", 12, "bold"), command=btnPlusPressed)
    buttonPlus.place(relx=0.660, rely=0.3, anchor="center", width=50, height=50)

    # Second Row Of Buttons
    button4 = tk.Button(window, text="4", fg="black", font=("Ariel", 12, "bold"), command=btnFourPressed)
    button4.place(relx=0.260, rely=0.425, anchor="center", width=50, height=50)

    button5 = tk.Button(window, text="5", fg="black", font=("Ariel", 12, "bold"), command=btnFivePressed)
    button5.place(relx=0.400, rely=0.425, anchor="center", width=50, height=50)

    button6 = tk.Button(window, text="6", fg="black", font=("Ariel", 12, "bold"), command=btnSixPressed)
    button6.place(relx=0.530, rely=0.425, anchor="center", width=50, height=50)

    buttonSubtract = tk.Button(window, text="-", fg="black", font=("Ariel", 12, "bold"), command=btnSubtractPressed)
    buttonSubtract.place(relx=0.660, rely=0.425, anchor="center", width=50, height=50)

    # Third Row Of Buttons
    button7 = tk.Button(window, text="7", fg="black", font=("Ariel", 12, "bold"), command=btnSevenPressed)
    button7.place(relx=0.260, rely=0.550, anchor="center", width=50, height=50)

    button8 = tk.Button(window, text="8", fg="black", font=("Ariel", 12, "bold"), command=btnEightPressed)
    button8.place(relx=0.400, rely=0.550, anchor="center", width=50, height=50)

    button9 = tk.Button(window, text="9", fg="black", font=("Ariel", 12, "bold"), command=btnNinePressed)
    button9.place(relx=0.530, rely=0.550, anchor="center", width=50, height=50)

    buttonMultiply = tk.Button(window, text="X", fg="black", font=("Ariel", 12, "bold"), command=btnMultiplyPressed)
    buttonMultiply.place(relx=0.660, rely=0.550, anchor="center", width=50, height=50)

    # Fourth Row Of Buttons
    buttonClear = tk.Button(window, text="C", fg="black", font=("Ariel", 12, "bold"), command=btnClearPressed)
    buttonClear.place(relx=0.260, rely=0.675, anchor="center", width=50, height=50)

    button0 = tk.Button(window, text="0", fg="black", font=("Ariel", 12, "bold"), command=btnZeroPressed)
    button0.place(relx=0.400, rely=0.675, anchor="center", width=50, height=50)

    buttonEqual = tk.Button(window, text="=", fg="black", font=("Ariel", 12, "bold"), command=btnEqualPressed)
    buttonEqual.place(relx=0.530, rely=0.675, anchor="center", width=50, height=50)

    buttonDivide = tk.Button(window, text="/", fg="black", font=("Ariel", 12, "bold"), command=btnDividePressed)
    buttonDivide.place(relx=0.660, rely=0.675, anchor="center", width=50, height=50)


    # Keeps Calculator Running Until X Is Clicked
    window.mainloop()


class Calculator:
    # Class Variables With Default Values
    Title = "Simple Calculator"
    Width = 400
    Height = 400

    # Default Constructor
    def __init__(self, *args):

        # Width And Height Arguments
        if len(args) > 0 and len(args) < 3:
            self.Width = args[0]
            self.Height = args[1]

        # Title, Width, And Height Arguments
        elif len(args) >= 3:
            self.Title = args[0]
            self.Width = args[1]
            self.Height = args[2]

        calculatorBuilder(self.Title, self.Width, self.Height)
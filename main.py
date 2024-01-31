from math import sqrt
from tkinter import Button, Frame, Label, Tk


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    def build(self):
        self.formula = "0"
        self.lbl = Label(
            text=self.formula,
            font=("Times New Roman", 21, "bold"),
            bg="#000",
            foreground="#FFF"
        )
        self.lbl.place(x=11, y=50)

        buttons = [
            "C", "DEL", "*", "=",
            "1", "2", "3", "/",
            "4", "5", "6", "+",
            "7", "8", "9", "-",
            "(", "0", ")", "X^2",
            "X^(1/2)", "."
        ]

        x = 10
        y = 140
        for button in buttons:
            Button(
                text=button,
                bg="#FFF",
                font=("Times New Roman", 15),
                command=lambda x=button: self.logicalc(x)
            ).place(x=x, y=y, width=115, height=79)
            x += 117
            if x > 400:
                x = 10
                y += 81

    def logicalc(self, operation):
        if operation == "C":
            self.formula = ""
        elif operation == "DEL":
            self.formula = str(self.formula)[0:-1]
        elif operation == "X^2":
            self.formula = str((eval(self.formula))**2)
        elif operation == "=":
            self.formula = str(eval(self.formula))
        elif operation == "X^(1/2)":
            self.formula = sqrt(eval(self.formula))
        elif operation == ".":
            self.formula = self.formula+"."
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)


if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#000"
    root.geometry("485x650+200+200")
    root.title("Calculator")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()

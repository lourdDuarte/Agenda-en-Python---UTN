from tkinter import Tk
from view import App


class miApp:
    def __init__(self, window):
        self.ventana = window
        App(self.ventana)


if __name__ == "__main__":
    root = Tk()
    aplication = App(root)
    root.mainloop()

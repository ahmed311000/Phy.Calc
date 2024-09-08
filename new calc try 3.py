import tkinter as tk


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.window.geometry("375x500")
        self.window.resizable(0, 0)

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_display_frame()
        self.create_buttons_frame()

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=100, bg="grey")
        frame.pack(expand=True, fill="both")

        input_field = tk.Entry(frame, font=('Arial', 18), textvariable=self.input_text, bg="grey", bd=0,
                               justify=tk.RIGHT)
        input_field.grid(row=0, column=0, sticky="nsew")
        input_field.pack(expand=True, fill="both")

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]

        for row in range(4):
            for col in range(4):
                button = tk.Button(frame, text=buttons[row][col], font=('Arial', 18), bd=1,
                                   command=lambda x=buttons[row][col]: self.on_button_click(x))
                button.grid(row=row, column=col, sticky="nsew")

        for i in range(4):
            frame.grid_columnconfigure(i, weight=1)
            frame.grid_rowconfigure(i, weight=1)

    def on_button_click(self, button_value):
        if button_value == 'C':
            self.expression = ""
            self.input_text.set("")
        elif button_value == '=':
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except:
                self.input_text.set("Error")
                self.expression = ""
        else:
            self.expression += button_value
            self.input_text.set(self.expression)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()

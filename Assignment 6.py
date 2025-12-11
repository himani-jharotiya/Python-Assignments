import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        
        self.current = ""
        self.previous = ""
        self.operator = ""
        self.total = 0
        
        self.create_widgets()
    
    def create_widgets(self):
        # Display
        self.display_var = tk.StringVar()
        self.display_var.set("0")
        display = tk.Entry(self.root, textvariable=self.display_var, 
                          font=("Arial", 20), justify="right", bd=10, 
                          state="readonly")
        display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="ew")
        
        # Buttons
        buttons = [
            ('C', 1, 0), ('±', 1, 1), ('%', 1, 2), ('÷', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('×', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('0', 5, 0), ('.', 5, 2), ('=', 5, 3)
        ]
        
        for (text, row, col) in buttons:
            if text == '0':
                btn = tk.Button(self.root, text=text, font=("Arial", 16),
                              command=lambda t=text: self.button_click(t),
                              bg="#d1d1d1", height=2, width=8)
                btn.grid(row=row, column=col, columnspan=2, padx=2, pady=2, sticky="nsew")
            elif text == '.':
                btn = tk.Button(self.root, text=text, font=("Arial", 16),
                              command=lambda t=text: self.button_click(t),
                              bg="#d1d1d1", height=2, width=4)
                btn.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
            elif text in '÷×+-=':
                btn = tk.Button(self.root, text=text, font=("Arial", 16, "bold"),
                              command=lambda t=text: self.button_click(t),
                              bg="#ff9500", fg="white", height=2, width=4)
                btn.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
            else:
                btn = tk.Button(self.root, text=text, font=("Arial", 16),
                              command=lambda t=text: self.button_click(t),
                              bg="#d1d1d1", height=2, width=4)
                btn.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
        
        # Configure grid weights
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_columnconfigure(3, weight=1)
    
    def button_click(self, char):
        if char == 'C':
            self.current = ""
            self.previous = ""
            self.operator = ""
            self.display_var.set("0")
        elif char == '±':
            if self.current.startswith('-'):
                self.current = self.current[1:]
            else:
                self.current = '-' + self.current
            self.display_var.set(self.current or "0")
        elif char == '%':
            if self.current:
                self.current = str(float(self.current) / 100)
                self.display_var.set(self.current)
        elif char in '÷×+-':
            self.previous = self.current
            self.operator = char
            self.current = ""
        elif char == '=':
            if self.previous and self.current and self.operator:
                self.calculate()
        elif char == '.':
            if '.' not in self.current:
                self.current += char
                self.display_var.set(self.current)
        else:  # Numbers
            if self.current == "0":
                self.current = char
            else:
                self.current += char
            self.display_var.set(self.current)
    
    def calculate(self):
        prev = float(self.previous)
        curr = float(self.current)
        
        if self.operator == '+':
            result = prev + curr
        elif self.operator == '-':
            result = prev - curr
        elif self.operator == '×':
            result = prev * curr
        elif self.operator == '÷':
            if curr == 0:
                self.display_var.set("Error")
                return
            result = prev / curr
        
        self.current = str(result)
        self.display_var.set(self.current)
        self.previous = ""
        self.operator = ""

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

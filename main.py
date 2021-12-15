import tkinter as tk

LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
LIGHT_GRAY = "#D3D3D3"
LABEL_COLOR = "#25265E"

class Calculator():

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.title("Calculator")
        self.window.resizable(0,0)

        #labels
        self.total_expression = "0"
        self.current_expression = "0"

        self.display_frame = self.create_display_frame()
        self.button_frame = self.create_button_frame()

        self.total_label, self.current_label = self.create_display_labels()


    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY,
                     fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(fill=tk.BOTH, expand=True)

        current_label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=LIGHT_GRAY,
                     fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        current_label.pack(fill=tk.BOTH, expand=True)

        return total_label, current_label


    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(fill=tk.BOTH, expand=True)
        return frame
    
    def create_button_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(fill=tk.BOTH, expand=True)
        return frame


    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
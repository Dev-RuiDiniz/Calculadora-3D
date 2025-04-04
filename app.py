import tkinter as tk
from calculadora_3d.ui.login_window import LoginWindow

def start_main_window():
    root = tk.Tk()
    from calculadora_3d.ui.main_window import MainWindow
    app = MainWindow(root)  # Note que agora criamos uma instância
    root.mainloop()

if __name__ == "__main__":
    login_app = LoginWindow(on_success_callback=start_main_window)
    login_app.root.mainloop()
import tkinter as tk
from tkinter import messagebox
from calculadora_3d.core.auth import verificar_senha  # Import absoluto

class LoginWindow:
    def __init__(self, on_success_callback):
        self.root = tk.Tk()
        self.root.title("Login")
        self.root.geometry("300x150")
        self.on_success = on_success_callback
        self._setup_ui()

    def _setup_ui(self):
        tk.Label(self.root, text="Digite a Senha:").pack(pady=20)
        self.entry_senha = tk.Entry(self.root, show="*")
        self.entry_senha.pack(pady=5)
        tk.Button(self.root, text="Login", command=self._on_login).pack(pady=10)

    def _on_login(self):
        if verificar_senha(self.entry_senha.get()):
            self.root.destroy()
            self.on_success()  # Chama a callback (ex: abrir janela principal)
        else:
            messagebox.showerror("Erro", "Senha incorreta")
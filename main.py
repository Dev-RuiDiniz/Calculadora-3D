import os
import sys
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


# Função para obter o caminho correto dos recursos (como imagens), 
# garantindo compatibilidade com executáveis criados pelo PyInstaller.
def resource_path(relative_path):
    if getattr(sys, 'frozen', False):  # Verifica se o script está empacotado como executável
        base_path = sys._MEIPASS  # Diretório temporário do PyInstaller
    else:
        base_path = os.path.abspath(".")  # Diretório do script
    return os.path.join(base_path, relative_path)

# Função que verifica a senha inserida pelo usuário
def verificar_senha():
    senha_correta = "1234"  # Senha fixa (poderia ser mais segura com hash ou entrada externa)
    senha_inserida = entry_senha.get()
    
    if senha_inserida == senha_correta:
        janela_login.destroy()  # Fecha a janela de login
        criar_janela_principal()  # Chama a função para abrir a janela principal
    else:
        messagebox.showerror("Erro", "Senha incorreta. Tente novamente.")

# Função para criar a janela principal do aplicativo
def criar_janela_principal():
    global entry_custo_pla, entry_valor_maquina, entry_custo_energia, entry_tempo, entry_peso
    global entry_lucro, entry_depreciacao, entry_perda_material, resultado

    # Criação da janela principal
    tk_root = tk.Tk()
    tk_root.title("Cálculo de Orçamento 3D")
    tk_root.geometry("500x550")

    # Carrega e exibe a imagem de fundo
    bg_image = Image.open(resource_path("fundo.png"))
    bg_image = bg_image.resize((500, 550), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)
    
    canvas = tk.Canvas(tk_root, width=500, height=550)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

    # Lista de campos do formulário com valores padrão
    campos = [
        ("Custo do Rolo de PLA (1kg) em R$:", "120"),
        ("Valor da Máquina (R$):", "2000"),
        ("Custo da Energia Elétrica (R$/kWh):", "0.10"),
        ("Tempo de Impressão (horas):", "1"),
        ("Peso da Peça (g):", "12"),
        ("Percentual de Lucro (%):", "120"),
        ("Depreciação por Hora (%):", "1"),
        ("Perda de Material (g):", "5")
    ]
    
    entries = []
    for i, (label, default) in enumerate(campos):
        lbl = tk.Label(tk_root, text=label, font=("Arial", 10, "bold"), bg=tk_root["bg"], fg="#333")
        canvas.create_window(50, 30 + (i * 40), anchor="nw", window=lbl)
        
        entry = tk.Entry(tk_root, font=("Arial", 10))
        entry.insert(0, default)
        canvas.create_window(300, 30 + (i * 40), anchor="nw", window=entry)
        
        entries.append(entry)
    
    (entry_custo_pla, entry_valor_maquina, entry_custo_energia, entry_tempo, 
    entry_peso, entry_lucro, entry_depreciacao, entry_perda_material) = entries

    # Campo para exibição do resultado
    resultado = tk.StringVar()
    resultado_label = tk.Label(tk_root, textvariable=resultado, font=("Arial", 12, "bold"),
                                bg="#eeeeee", fg="black", bd=2, relief="solid", width=40, height=5)
    canvas.create_window(250, 370, anchor="n", window=resultado_label)

    # Botão para calcular o orçamento
    btn_calcular = tk.Button(tk_root, text="Calcular", command=calcular_orcamento,
                             font=("Arial", 12, "bold"), bg="#B3E5FC", fg="white", relief="raised", bd=3)
    canvas.create_window(250, 335, anchor="n", window=btn_calcular)

    # Carrega e exibe o logo
    logo_image = Image.open(resource_path("logo.png"))
    logo_image = logo_image.resize((60, 60), Image.LANCZOS)
    logo_photo = ImageTk.PhotoImage(logo_image)
    logo_label = tk.Label(tk_root, image=logo_photo, bg="#cccccc")
    canvas.create_window(50, 480, anchor="nw", window=logo_label)

    tk_root.mainloop()

# Função de cálculo do orçamento
def calcular_orcamento():
    try:
        # Captura os valores inseridos pelo usuário
        custo_pla = float(entry_custo_pla.get())
        valor_maquina = float(entry_valor_maquina.get())
        custo_energia = float(entry_custo_energia.get())
        tempo_impressao = float(entry_tempo.get())
        peso_peca = float(entry_peso.get())
        percentual_lucro = float(entry_lucro.get()) / 100
        depreciacao_hora = float(entry_depreciacao.get()) / 100
        perda_material = float(entry_perda_material.get())

        # Cálculo dos custos
        custo_material = (custo_pla / 1000) * (peso_peca + perda_material)
        custo_energia_estimado = custo_energia * tempo_impressao
        custo_depreciacao = (valor_maquina * depreciacao_hora) * tempo_impressao
        custo_total = custo_material + custo_energia_estimado + custo_depreciacao
        valor_cobrar = custo_total * (1 + percentual_lucro)
        lucro = valor_cobrar - custo_total

        # Exibe os resultados na interface gráfica
        resultado.set(f"Custo Total (sem lucro): R$ {custo_total:.2f}\n"
                      f"Valor a Cobrar: R$ {valor_cobrar:.2f}\n"
                      f"Lucro da Venda: R$ {lucro:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Criando a janela de login
janela_login = tk.Tk()
janela_login.title("Login")
janela_login.geometry("300x150")

# Campo de senha na janela de login
label_senha = tk.Label(janela_login, text="Digite a Senha:", font=("Arial", 10, "bold"))
label_senha.pack(pady=20)

entry_senha = tk.Entry(janela_login, font=("Arial", 10), show="*")
entry_senha.pack(pady=5)

# Botão de login
btn_login = tk.Button(janela_login, text="Login", command=verificar_senha, font=("Arial", 12, "bold"), bg="#B3E5FC", fg="white")
btn_login.pack(pady=10)

# Inicia a janela de login
janela_login.mainloop()

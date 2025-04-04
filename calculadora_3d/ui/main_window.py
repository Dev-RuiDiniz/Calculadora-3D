import tkinter as tk
from PIL import Image, ImageTk
from calculadora_3d.utils.resource_path import resource_path

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Cálculo de Orçamento 3D")
        self.root.geometry("500x550")
        self._setup_ui()
    
    def _load_images(self):
        """Carrega as imagens com fallback se não encontradas"""
        try:
            bg_path = resource_path("calculadora_3d/assets/fundo.png")
            self.bg_image = Image.open(bg_path)
            self.bg_photo = ImageTk.PhotoImage(self.bg_image.resize((500, 550), Image.LANCZOS))
            
            logo_path = resource_path("calculadora_3d/assets/logo.png")
            self.logo_image = Image.open(logo_path)
            self.logo_photo = ImageTk.PhotoImage(self.logo_image.resize((60, 60), Image.LANCZOS))
        except FileNotFoundError:
            self.bg_photo = ImageTk.PhotoImage(Image.new('RGB', (500, 550), '#f0f0f0'))
            self.logo_photo = ImageTk.PhotoImage(Image.new('RGB', (60, 60), '#cccccc'))
    
    def _create_entry_field(self, parent, label_text, row, default_value):
        """Cria um campo de entrada com label usando grid"""
        lbl = tk.Label(parent, text=label_text, font=("Arial", 10, "bold"))
        lbl.grid(row=row, column=0, padx=10, pady=5, sticky="w")
        
        entry = tk.Entry(parent, font=("Arial", 10))
        entry.insert(0, default_value)
        entry.grid(row=row, column=1, padx=10, pady=5, sticky="ew")
        return entry
    
    def _setup_ui(self):
        """Configura toda a interface usando apenas grid"""
        self._load_images()
        
        # Frame principal - substitui o Canvas para simplificar
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Adiciona imagem de fundo como label (alternativa ao Canvas)
        bg_label = tk.Label(self.main_frame, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Frame para os campos de entrada (sobre a imagem)
        self.form_frame = tk.Frame(self.main_frame, bg='white')
        self.form_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        # Campos de entrada - agora usando grid dentro do form_frame
        self.entry_custo_pla = self._create_entry_field(
            self.form_frame, 
            "Custo do Rolo de PLA (1kg) em R$:", 
            0, 
            "120"
        )
        
        # Adicione outros campos aqui seguindo o mesmo padrão
        # Exemplo:
        # self.entry_tempo = self._create_entry_field(
        #     self.form_frame, "Tempo de Impressão (horas):", 1, "1"
        # )
        
        # Botão de cálculo
        btn_calcular = tk.Button(
            self.form_frame, 
            text="Calcular", 
            command=self._calcular,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 10, "bold")
        )
        btn_calcular.grid(row=8, columnspan=2, pady=20, sticky="ew")
        
        # Label de resultado
        self.resultado = tk.StringVar()
        lbl_resultado = tk.Label(
            self.form_frame, 
            textvariable=self.resultado,
            font=("Arial", 10),
            bg="white"
        )
        lbl_resultado.grid(row=9, columnspan=2, pady=10)
    
    def _calcular(self):
        """Lógica de cálculo"""
        try:
            custo_pla = float(self.entry_custo_pla.get())
            # Adicione outros cálculos aqui
            resultado = custo_pla * 1.1  # Exemplo simples
            self.resultado.set(f"Resultado: R${resultado:.2f}")
        except ValueError:
            self.resultado.set("Erro: Insira valores numéricos válidos!")
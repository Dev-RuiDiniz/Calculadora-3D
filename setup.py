from cx_Freeze import setup, Executable
import os

# Caminho para o arquivo principal
main_script = os.path.join("src", "main.py")

# Caminho para o ícone
icon_path = os.path.join("assets", "icons", "icon.ico")

# Lista de arquivos adicionais para incluir
include_files = [
    (os.path.join("assets", "icons", "icone.ico"), "assets/icons/icone.ico"),  # Ícone
    (os.path.join("assets", "images", "fundo.png"), "assets/images/fundo.png"),  # Fundo
    (os.path.join("assets", "images", "logo.png"), "assets/images/logo.png"),  # Logo
]

# Configurações do executável
executables = [
    Executable(
        script=main_script,  # Arquivo principal
        icon=icon_path,      # Ícone do executável
        base="Win32GUI",     # Use "Win32GUI" para ocultar o console (opcional)
    )
]

# Configurações do pacote
setup(
    name="Calculadora3D",   # Nome do seu aplicativo
    version="0.1",          # Versão do seu aplicativo
    description="Uma calculadora 3D",  # Descrição do seu aplicativo
    executables=executables,
    options={
        "build_exe": {
            "include_files": include_files,  # Inclui arquivos adicionais
        }
    },
)
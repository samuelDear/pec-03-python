from colorama import init, just_fix_windows_console
from app.screen import showMenu

# Config de colorama
just_fix_windows_console()
init(autoreset=True)

# Inicio
showMenu()
from colorama import init, just_fix_windows_console
from app.screen import showMenu
from app.utils import getReservasRows, getFlotaRows
from app.gestor import GestorSistema
import logging

# Inicializacion del logger
logging.basicConfig(
    filename='reservas.log',
    encoding='utf-8',
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Config de colorama
just_fix_windows_console()
init(autoreset=True)

# Inicializamos el gestor
vehiculos = getFlotaRows()
reservas = getReservasRows()

gestor = GestorSistema(vehiculos, reservas)

# Inicio
showMenu(gestor)
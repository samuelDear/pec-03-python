from colorama import Fore, Style
import os, logging
from typing import Any

from app.gestor import GestorSistema
from app.menuoptions import menuOptions, runOptionAction, validateOption

logger = logging.getLogger(__name__)

def showTitle() -> None:
    """
    Funcion que imprime el titulo del proyecto
    Retorna:
        None
    """
    print("\033[0;37m \033[0;33m▄\033[0;90;43m▀▓▒░ \033[0;33m▄\033[0;37m  \033[0;33m▄\033[0;90;43m▀▓▒░ \033[0;33m▄\033[0;37m  \033[0;90;43m▀▓▒░   \033[0;33m▄\033[0;37m  \033[0;90;43m▀▓▒░   \033[0;33m▄\033[0;37m  \033[0;33m▄\033[0;90;43m ░▒▓▒▓▀▓▒░ \033[0;33m▄\033[0;37m  \033[0;33m▄\033[0;90;43m▀▓▒░ \033[0;33m▄\033[0;37m  \033[0;90;43m ▀\033[0;37m     \033[0;93m██\033[0;37m \033[0;90;43m ▀\033[0m")
    print("\033[0;33m█\033[0;93;43m \033[0;33m▀\033[0;37m    \033[0;33m▀\033[0;37m \033[0;33m█\033[0;93;43m \033[0;33m▀\033[0;37m   \033[0;33m▀\033[0;93;43m▄▓\033[0;37m \033[0;93;43m  \033[0;37m    \033[0;33m▀\033[0;93;43m▄▓\033[0;37m \033[0;93;43m  \033[0;37m    \033[0;33m▀\033[0;93;43m▄▓\033[0;37m \033[0;33m▀\033[0;37m    \033[0;33m█\033[0;93;43m \033[0;37m     \033[0;33m▀\033[0;37m \033[0;33m█\033[0;93;43m \033[0;33m▀\033[0;37m   \033[0;33m▀\033[0;93;43m▄▓\033[0;37m \033[0;33m█\033[0;93;43m░\033[0;37m     \033[0;93m█\033[0;93;43m▓\033[0;37m \033[0;33m█\033[0;93;43m \033[0m")
    print("\033[0;33m█\033[0;93;43m░\033[0;37m       \033[0;33m█\033[0;93;43m░\033[0;37m     \033[0;93;43m▓▒\033[0;37m \033[0;93;43m ░\033[0;37m     \033[0;93;43m▒▒\033[0;37m \033[0;93;43m ░\033[0;37m     \033[0;93;43m▒▒\033[0;37m      \033[0;33m█\033[0;93;43m░\033[0;37m       \033[0;33m█\033[0;93;43m░\033[0;37m     \033[0;93;43m▓▒\033[0;37m \033[0;33m█\033[0;93;43m▒\033[0;37m     \033[0;93;43m▓▒\033[0;37m \033[0;33m█\033[0;93;43m▒\033[0m")
    print("\033[0;33;43m \033[0;93;43m▒\033[0;37m       \033[0;33;43m \033[0;93;43m▒\033[0;37m     \033[0;93;43m▒░\033[0;37m \033[0;93;43m ▒░  \033[0;33m██\033[0;93;43m░\033[0;33m▀\033[0;37m \033[0;93;43m ▒░  \033[0;33m██\033[0;93;43m░\033[0;33m▀\033[0;37m      \033[0;33;43m \033[0;93;43m▒\033[0;37m       \033[0;33;43m \033[0;93;43m▒\033[0;37m     \033[0;93;43m▒░\033[0;37m \033[0;90;42m▀\033[0;93;43m▒░\033[0;32m▄\033[0;37m  \033[0;92m▄\033[0;93;43m▒░\033[0;37m \033[0;33m█\033[0;93;43m▓\033[0m")
    print("\033[0;33;43m \033[0;93;43m▓\033[0;37m       \033[0;33;43m \033[0;93;43m▓\033[0;37m     \033[0;93;43m░ \033[0;37m \033[0;93;43m ▓\033[0;37m  \033[0;33m▀█\033[0;33;43m▀\033[0;33m▄\033[0;37m  \033[0;93;43m ▓\033[0;37m             \033[0;33;43m \033[0;93;43m▓\033[0;37m       \033[0;33;43m \033[0;93;43m▓▒░\033[0;33m███\033[0;93;43m░ \033[0;37m  \033[0;90m▀\033[0;93;43m▓▒░▒▓\033[0;92m▀\033[0;37m  \033[0;33m█\033[0;93;43m█\033[0m")
    print("\033[0;33m█\033[0;93;43m█\033[0;37m       \033[0;33m█\033[0;93;43m█\033[0;37m     \033[0;33m██\033[0;37m \033[0;93;43m █\033[0;37m    \033[0;33m▀\033[0;93;43m▄▓\033[0;37m \033[0;93;43m █\033[0;37m             \033[0;33m█\033[0;93;43m█\033[0;37m       \033[0;33m█\033[0;93;43m█\033[0;37m     \033[0;33m██\033[0;37m \033[0;90;42m▄\033[0;93;43m█▒\033[0;92m▀\033[0;37m \033[0;33m▀\033[0;93;43m▒░\033[0;33m▄\033[0;37m \033[0;33m█\033[0;93;43m█\033[0m")
    print("\033[0;33m█\033[0;93;43m█\033[0;37m       \033[0;33m█\033[0;93;43m█\033[0;37m     \033[0;90;43m░\033[0;33m█\033[0;37m \033[0;93;43m █\033[0;37m     \033[0;93;43m░▒\033[0;37m \033[0;93;43m █\033[0;37m             \033[0;33m█\033[0;93;43m█\033[0;37m       \033[0;33m█\033[0;93;43m█\033[0;37m     \033[0;90;43m░\033[0;33m█\033[0;37m \033[0;33m█\033[0;93;43m█\033[0;90m▀\033[0;37m    \033[0;93;43m░\033[0;33m█\033[0;37m \033[0;33m█\033[0;93;43m▓\033[0m")
    print("\033[0;33m█\033[0;93;43m▓\033[0;37m       \033[0;33m█\033[0;93;43m▓\033[0;37m     \033[0;90;43m▒░\033[0;37m \033[0;33m█\033[0;93;43m▓\033[0;37m     \033[0;90;43m░\033[0;93;43m░\033[0;37m \033[0;33m█\033[0;93;43m▓\033[0;37m             \033[0;33m█\033[0;93;43m▓\033[0;37m       \033[0;33m█\033[0;93;43m▓\033[0;37m     \033[0;90;43m▒░\033[0;37m \033[0;33m█\033[0;93;43m▓\033[0;37m     \033[0;90;43m▒░\033[0;37m \033[0;33m█\033[0;93;43m▒\033[0m")
    print("\033[0;90;43m░\033[0;93;43m▒\033[0;37m       \033[0;90;43m░\033[0;93;43m▒\033[0;37m     \033[0;90;43m▓▒\033[0;37m \033[0;90;43m░\033[0;93;43m▒\033[0;37m     \033[0;90;43m▒░\033[0;37m \033[0;90;43m░\033[0;93;43m▒\033[0;37m             \033[0;90;43m░\033[0;93;43m▒\033[0;37m       \033[0;90;43m░\033[0;93;43m▒\033[0;37m     \033[0;90;43m▓▒\033[0;37m \033[0;90;43m░\033[0;93;43m▒\033[0;37m     \033[0;90;43m▓▒\033[0;37m \033[0;90;43m░\033[0;93;43m▒\033[0m")
    print("\033[0;90;43m▒\033[0;93;43m░\033[0;33m▄\033[0;37m    \033[0;33m▄\033[0;37m \033[0;90;43m▒\033[0;93;43m░\033[0;33m▄\033[0;37m   \033[0;33m▄\033[0;90;43m█▓\033[0;37m \033[0;90;43m▒\033[0;93;43m░\033[0;37m     \033[0;90;43m▓▒\033[0;37m \033[0;90;43m▒\033[0;93;43m░\033[0;37m             \033[0;90;43m▒\033[0;93;43m░\033[0;37m       \033[0;90;43m▒\033[0;93;43m░\033[0;37m     \033[0;90;43m▒\033[0;93;43m░\033[0;37m \033[0;90;43m▒\033[0;93;43m░\033[0;37m     \033[0;90;43m▒\033[0;93;43m░\033[0;37m \033[0;90;43m▒\033[0;93;43m░\033[0m")
    print("\033[0;37m \033[0;33m▀█████▀\033[0;37m  \033[0;33m▀█████▀\033[0;37m  \033[0;90;43m▓ \033[0;37m     \033[0;90;43m▓ \033[0;37m \033[0;90;43m▓ \033[0;37m             \033[0;90;43m▓ \033[0;37m       \033[0;90;43m▓ \033[0;37m     \033[0;90;43m▓ \033[0;37m \033[0;90;43m▓ \033[0;37m     \033[0;90;43m▓ \033[0;37m \033[0;90;43m▓ \033[0m")
    print("\n")

def clearConsole() -> None:
    """
    Funcion para limpiar la consola donde se ejecute
    Retorna:
        None
    """
    os.system('cls' if os.name == "nt" else None)


def showMenu(gestor: GestorSistema) -> None:
    """
    Funcion para agrupar y ejecutar las funciones necesarias para mostrarle
    al usuario el menu de la app
    Retorna:
        None
    """
    
    logger.info(f"Se inicio el programa")
    
    # Declaracion de variables
    option = None
    
    while True:
        # Limpiamos al iniciar la app siempre
        clearConsole()
        
        # Mostramos el menu
        print(f"{Fore.GREEN}{"*" * 64}")
        print('\n')
        showTitle()
        print(f"{Style.BRIGHT}Bievenido a tu gestor flota y reservas\n")
        print("Opciones:\n")
        menuOptions(gestor.options)
        print('\n')
        
        option = inputOption(gestor.options)
        
        logger.info(f"El usuario ingreso la opcion {option}")
        
        res = runOptionAction(option, gestor.options)
        
        # Si la funcion retorna False, es que es la de salida
        if res == False:
            
            logger.info(f"Se finalizo el programa")
            
            print(f"\nHasta pronto\n")
            
            print(f"{Fore.GREEN}{"*" * 64}")
            break
        
        print(f"{Fore.GREEN}{"*" * 64}")
        
        # Si no entro en el break
        # Le damos la opcion de continuar...
        input(f"\n{Style.DIM}Presione enter para continuar....")
        
def inputOption(options: list[Any]) -> str:
    """
    Funcion para capturar la opcion ingresada por el usuario,
    aca se valida que sea un valor valido
    Retorna:
        str: la opcion valida ingresada por el usuario
    """
    # Pedimos la opcion y si no damos error
    option = ""
    while True:
        try:
            option = input(f"> Ingrese una opcion: ")
            
            # Validamos que sea una opcion correcta
            validateOption(option, options)
            break
        except Exception as e:
            logger.error(e)
            print(f"{Fore.RED}[ERROR]: {e}\n")       
    
    return option

if __name__ == "__main__":
    """
    Prueba de docstrings
    """
    
    help(inputOption)
    print("*" * 64)
    help(showMenu)
    print("*" * 64)
    help(clearConsole)
    print("*" * 64)
    help(showTitle)
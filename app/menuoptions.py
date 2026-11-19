
from colorama import Style
from typing import Any
from app.gestor import GestorSistema

def menuOptions(options: list[Any]) -> None:
    """
    Funcion para imprimir las diferentes opciones del programa
    Retorna:
        None
    """
    
    # Pintamos las opciones
    for option in options:
        print(f"{Style.BRIGHT}> {option["value"]}. {option["label"]}.")
        
def validateOption(val: str, options: list[Any]) -> None:
    """
    Funcion para validar que la opcion ingresada es valida
    Retorna:
        None
    """
    validOption = False
    
    for option in options:
        if option["value"] == val:
            validOption = True
    
    # Si no es una opcion valida, damos error
    if not validOption:
        raise Exception(f"Valor {val} no es una opcion valida.")
    
    
def runOptionAction(val: str, options: list[Any], *args) -> bool | None:
    """
    Funcion para ejecutar la funcionalidad de la opcion ingresada
    Retorna:
        bool
    """
    for option in options:
        if option["value"] == val:
            return option["action"](*args)
            
    # Si no es ninguna, que repita el flujo
    return True
    
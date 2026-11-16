
from colorama import Style
from app.gestor import GestorSistema

gestor = GestorSistema()
OPTIONS = [
    {
        "value": "1",
        "label": "Añadir vehiculos a la flota",
        "action": gestor.añadir_vehiculo
    },
    {
        "value": "2",
        "label": "Ver flota completa",
        "action": lambda *args: True
    },
    {
        "value": "3",
        "label": "Reservar vehiculo",
        "action": gestor.reservar_vehiculo
    },
    {
        "value": "4",
        "label": "Ver reservas",
        "action": lambda *args: True
    },
    {
        "value": "0",
        "label": "Salir",
        "action": lambda *args: False
    }
]

def menuOptions() -> None:
    """
    Funcion para imprimir las diferentes opciones del programa
    Retorna:
        None
    """
    # Pintamos las opciones
    for option in OPTIONS:
        print(f"{Style.BRIGHT}> {option["value"]}. {option["label"]}.")
        
def validateOption(val: str) -> None:
    """
    Funcion para validar que la opcion ingresada es valida
    Retorna:
        None
    """
    validOption = False
    
    for option in OPTIONS:
        if option["value"] == val:
            validOption = True
    
    # Si no es una opcion valida, damos error
    if not validOption:
        raise Exception(f"Valor {val} no es una opcion valida.")
    
    
def runOptionAction(val: str, *args) -> bool | None:
    """
    Funcion para ejecutar la funcionalidad de la opcion ingresada
    Retorna:
        bool
    """
    for option in OPTIONS:
        if option["value"] == val:
            return option["action"](*args)
            
    # Si no es ninguna, que repita el flujo
    return True
    
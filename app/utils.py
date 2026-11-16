from colorama import Fore, Style
from typing import Literal

def notAllowEmptyVal(
    label: str,
    field: str = "campo",
    typeVar: Literal['', 'int', 'float'] = ''
) -> str | int | float:
    """
    Funcion para validar que el input no es vacio
    Retorna:
        str | int
    """
    while True:
        try:
            value = input(label).strip()
                    
            # Si esta vacio, volvemos a pedirselo
            if not value:
                raise ValueError(f"El {field} no puede ser vacio.")
            
            # Si debe ser numerico lo parseamos, para retornarlo
            if (typeVar == 'float' or typeVar == 'int'):
                return float(value) if typeVar == 'float' else int(value)
                        
            # Si llego aqui es que tiene data
            return value
        except ValueError as e:
            print(f"{Fore.RED}[ERROR]: {e}\n")
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {e}\n")
    
def separatorPrint() -> None:
    """
    Funcion para imprimir una separacion entre cada funcionalidad
    """
    print(f"\n{Fore.GREEN}{"*" * 64}\n")
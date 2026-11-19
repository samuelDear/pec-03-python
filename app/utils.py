from colorama import Fore, Style
from typing import Literal, Any
import logging

logger = logging.getLogger(__name__)

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
            logger.info(f"funcion notAllowEmptyVal: {e}")
            print(f"{Fore.RED}[ERROR]: {e}\n")
        except Exception as e:
            logger.info(f"funcion notAllowEmptyVal: {e}")
            print(f"{Fore.RED}[ERROR]: {e}\n")
    
def separatorPrint() -> None:
    """
    Funcion para imprimir una separacion entre cada funcionalidad
    """
    print(f"\n{Fore.GREEN}{"*" * 64}\n")
    
def tableSeparator() -> None:
    """
    Funcion para imprimir una separacion en los items de una tabla
    """
    print(f"+{"-" * 80}+")
    
def getFlotaRows() -> list[Any]:
    """
    Funcion para obtener la flota como un Array de Dicts
    """
    rows = []
    # Leemos el txt de la flota
    with open('vehiculos.txt', 'r') as flota:
        content = flota.read()
        #print(content)
        # Obtenemos cada linea primero pa poder pintar bien
        rowsArr =  content.split("\n")
        #print(rowsArr)
        # Ahora vamos a hacer un diccionario de la data
        for rowStr in rowsArr:
            #Puede haber un registro vacio, por los saltos de linea, lo saltamos
            if not rowStr:
                continue
                    
            rowSep = rowStr.split(';')
            # hacemos el dict del coche
            rowTmp = {
                "type": rowSep[0],
                "matricula": rowSep[1],
                "marca": rowSep[2],
                "modelo": rowSep[3]
            }
                    
            # Validamos que dato es diferente
            if rowSep[0] == 'coche':
                rowTmp["npuertas"] = rowSep[4]
            elif rowSep[0] == 'moto':
                rowTmp["cc"] = rowSep[4]

            rows.append(rowTmp)
    
    return rows
            
            
def getReservasRows() -> list[Any]:
    """
    Funcion para obtener laas reservas como un Array de Dicts
    """
    rows = []
    # Leemos el txt de la flota
    with open('reservas.txt', 'r') as reserva:
        content = reserva.read()
        #print(content)
        # Obtenemos cada linea primero pa poder pintar bien
        rowsArr =  content.split("\n")
        #print(rowsArr)
        # Ahora vamos a hacer un diccionario de la data
        for rowStr in rowsArr:
            #Puede haber un registro vacio, por los saltos de linea, lo saltamos
            if not rowStr:
                continue
                    
            rowSep = rowStr.split(';')
            # hacemos el dict de la reserva
            rowTmp = {
                "fecha": rowSep[0],
                "matricula": rowSep[1],
            }

            rows.append(rowTmp)
    
    return rows
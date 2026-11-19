from typing import Any
from app.vehiculos import Moto, Coche
import logging
logger = logging.getLogger(__name__)

def getFlotaRows() -> list[Coche | Moto]:
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
            }
                    
            # Validamos que dato es diferente
            if rowSep[0] == 'coche':
                rowTmp = Coche(rowSep[1], rowSep[2], rowSep[3], rowSep[4])
            elif rowSep[0] == 'moto':
                rowTmp = Moto(rowSep[1], rowSep[2], rowSep[3], rowSep[4])

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

def guardar_vehiculo_txt(vehiculo: str) -> None:
        """
        Funcion para guardar en el vehiculos.txt los vehiculos
        """
        # Estructura tipo;matricula;marca;modelo;npuertas|cc
        with open('vehiculos.txt', 'a', encoding = 'utf-8') as flota:
            flota.write(f"{vehiculo}\n")
            logger.info(f"Se guardo un vehiculo({vehiculo})")
    
def guardar_reserva_txt(reserva: str) -> None:
    """
    Funcion para guardar en reservas.txt
    """
    # Estructura fecha;matricula
    with open('reservas.txt', 'a', encoding = 'utf-8') as reservas:
        reservas.write(f"{reserva}\n")
        logger.info(f"Se guardo la reserva({reserva})")
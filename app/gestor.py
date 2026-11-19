from app.vehiculos import Moto, Coche
from app.utils import notAllowEmptyVal, tableSeparator
from app.persistencia import guardar_vehiculo_txt, guardar_reserva_txt

from datetime import datetime
from typing import Any, Dict
from colorama import Fore, Style
import logging
logger = logging.getLogger(__name__)


class GestorSistema:
    
    # Metodos
    def __init__(self, vehiculos: list[Dict], reservas: list[Dict]):
        self.__vehiculos = vehiculos
        self.__reservas = reservas
        
    def añadir_vehiculo(self) -> None:
        """
        Funcion para agregar items a la flota
        pidiendo los datos necesarios
        return:
            None
        """
        while True:
            try:
                # Pedimos que tipo de vehiculo es
                typeCar = input("> Ingrese el tipo de vehiculo(Coche o Moto) o vacio si desea cancelar: ").strip()
                
                # Validamos si es vacio
                if typeCar == '':
                    print()
                    break
                
                # Validamos que sea un tipo valido
                if typeCar.lower() != 'moto' and typeCar.lower() != 'coche':
                    raise Exception(f"El tipo de vehiculo ingresado ({typeCar.lower()}) no es valido")
                
                print(f"{Style.BRIGHT}{Fore.YELLOW}> Ingreso: {typeCar.capitalize()}")
                
                # Si llegamos aca, pedimos las cosas comunes como matricula, modelo y marca
                
                # Ponemos un maximo para la matricula
                while True:
                    matricula = notAllowEmptyVal(
                        label = "> Ingrese la matricula: "
                    )
                    if 1 < len(matricula) and len(matricula) > 10:
                        logger.error(f"La matricula debe tener entre 1 y 10 caracteres.")
                        print(f"{Fore.RED}[ERROR]: La matricula debe tener entre 1 y 10 caracteres.")
                    
                    break
                
                marca = notAllowEmptyVal(
                    label = "> Ingrese la marca: "
                )
                modelo = notAllowEmptyVal(
                    label = "> Ingrese el modelo: "
                )
                
                # validamos si es coche o moto para pedir el dato que falta
                # Y tambien hacemos la instancia
                if typeCar.lower() == 'moto':
                    cc = notAllowEmptyVal(
                        label = "> Ingrese el CC de la moto: ",
                        typeVar = 'int'
                    )
                    flotaMoto = Moto(matricula.upper(), marca, modelo, cc)
                    guardar_vehiculo_txt(
                        f"moto;{flotaMoto.matricula};{flotaMoto.marca};{flotaMoto.modelo};{flotaMoto.cc}",
                    )
                    self.__vehiculos.append({
                        "type": 'moto',
                        "matricula": flotaMoto.matricula,
                        "marca": flotaMoto.marca,
                        "modelo": flotaMoto.modelo,
                        "cc": flotaMoto.cc
                    })
                if typeCar.lower() == 'coche':
                    npuertas = notAllowEmptyVal(
                        label = "> Ingrese el numero de puertas del coche: ",
                        typeVar = 'int'
                    )
                    flotaCoche = Coche(matricula.upper(), marca, modelo, npuertas)
                    guardar_vehiculo_txt(
                        f"coche;{flotaCoche.matricula};{flotaCoche.marca};{flotaCoche.modelo};{flotaCoche.n_puertas}",
                    )
                    self.__vehiculos.append({
                        "type": 'coche',
                        "matricula": flotaCoche.matricula,
                        "marca": flotaCoche.marca,
                        "modelo": flotaCoche.modelo,
                        "npuertas": flotaCoche.n_puertas
                    })
                
                print()
                
                break
            except Exception as e:
                logger.error(f"añadir_vehiculo: {e}")
                print(f"{Fore.RED}[ERROR]: {e}\n")
    
    def print_flota(self) -> list[Dict]:
        """
        Funcion para mostrar la flota guardada
        retorna:
            List[Flota]
        """
        
        # Obtenemos los datos ya formateados
        rows = self.__vehiculos
        
        # Si ta vacio decimos que no hay flota
        if len(rows) == 0:
            
            print(f"{Style.BRIGHT}{Fore.BLUE}\nNO HAY VEHICULOS REGISTRADOS AUN\n")
            return None
        
        print()
        print(f"{Style.BRIGHT}{Fore.YELLOW}{"-" * 30}  FLOTA DE VEHICULOS  {"-" * 30}")
        print()
        tableSeparator()
        print(f"{' ' * 2}{Style.BRIGHT}TIPO, MATRICULA, MARCA, MODELO, N. Puertas o CC")
        tableSeparator()
        # Ahora pintamos la flota completa
        for row in rows:
            typeCar = row.get('type')
            print(f"{' ' * 2}{typeCar.capitalize()}, {Style.BRIGHT}{row.get('matricula')}{Style.NORMAL}, {row.get('marca')}, {row.get('modelo')}, {f"{row.get('npuertas')} Puertas" if typeCar == 'coche' else f"{row.get('cc')} CC"}")
            tableSeparator()
        
        print()
        
        
        return rows
    
    def reservar_vehiculo(self) -> None:
        """
        Funcion para reserar vehiculos de la flota
        pidiendo el vehiculo por matricula
        y fecha de la reserva
        return:
            None
        """
        
        # Pintamos la flota para que el usuario sepa que puede ingresar y podamos validar la matricula
        flota = self.print_flota()
        
        
        while True:
            try:
                # Pedimos los datos al usuario
                matricula = input("> Ingrese la matricula del vehiculo o vacio si desea cancelar: ").strip().upper()
                dateReserve = ''
                # Validamos si es vacio
                if matricula == '':
                    print()
                    break
                    
                # Validamos si de verdad existe la matricula antes de pedir la fecha
                vehiculoExist = False
                for vehiculo in flota:
                    # Validamos cada matricula a ver si existe
                    if vehiculo['matricula'] == matricula:
                        vehiculoExist = True
                        # Si entro aqui cancelamos el bucle para no dar vueltas
                        break
                
                # Si no existe, error y volvemos a pedir
                if not vehiculoExist:
                    raise Exception(f"La matricula {matricula} no se encuentra actualmente como parte de la flota")
                
                # Pedimos la fecha de la reserva
                while True:
                    try:
                        fecha_reserva = input("> Ingrese la fecha de reserva (dd/mm/yyyy): ")
                        dateReserve = datetime.strptime(fecha_reserva, '%d/%m/%Y').date()
                        
                        #print(dateReserve.date())
                        break
                    except ValueError:
                        print(f"{Fore.RED}[ERROR]: Fecha de reserva no es valida\n")
                        
                # Validamos que no este ya reservado ese vehiculo en esa fecha
                vehiculoReservado = False
                
                reservas = self.__reservas
                for reserv in reservas:
                    #print(f"{reserv['fecha']}" == f"{dateReserve}", reserv['matricula'] == matricula)
                    if f"{reserv['fecha']}" == f"{dateReserve}" and reserv['matricula'].lower() == matricula.lower():
                        vehiculoReservado = True
                        break
                
                # Si esta reservada, damos error y regresamos
                if vehiculoReservado:
                    raise Exception(f"La matricula {matricula} ya se encuentra reservada para la fecha {dateReserve}")
                
                # Si llevamos aqui, buscamos la reserva
                guardar_reserva_txt(f"{dateReserve};{matricula}")
                
                print(f"{Fore.BLUE}{Style.BRIGHT}\nReserva creada con exito\n")
                self.__reservas.append({
                    "fecha": dateReserve,
                    "matricula": matricula,
                })
                
                # Si llegamos aca, cerramos el bucle
                break
            except Exception as e:
                logger.error(f"reservar_vehiculo: {e}")
                print(f"{Fore.RED}[ERROR]: {e}\n")
                
    def print_reservas(self) -> list[Dict]:
        """
        Funcion para mostrar las reservas guardadas
        retorna:
            List[Reserva]
        """
                
        # Obtenemos los datos ya formateados
        rows = self.__reservas
                
        # Si ta vacio decimos que no hay reservas
        if len(rows) == 0:
            print(f"{Style.BRIGHT}{Fore.BLUE}\nNO HAY RESERVAS REGISTRADOS AUN\n")
            return None
                
        print()
        print(f"{Style.BRIGHT}{Fore.YELLOW}{"-" * 35}  RESERVAS  {"-" * 35}")
        print()
        tableSeparator()
        print(f"{' ' * 2}{Style.BRIGHT}Matricula, Fecha de Reserva")
        tableSeparator()
        # Ahora pintamos la flota completa
        for row in rows:
            print(f"{' ' * 2}{Style.BRIGHT}{row.get('matricula')}{Style.NORMAL}, {row.get('fecha')}")
            tableSeparator()
                
        print()
                
                
        return rows
    
    @property
    def options(self) -> list[Dict]:
        return [
            {
                "value": "1",
                "label": "Añadir vehiculos a la flota",
                "action": self.añadir_vehiculo
            },
            {
                "value": "2",
                "label": "Ver flota completa",
                "action": self.print_flota
            },
            {
                "value": "3",
                "label": "Reservar vehiculo",
                "action": self.reservar_vehiculo
            },
            {
                "value": "4",
                "label": "Ver reservas",
                "action": self.print_reservas
            },
            {
                "value": "0",
                "label": "Salir",
                "action": lambda *args: False
            }
        ]
from app.vehiculos import Moto, Coche
from app.utils import notAllowEmptyVal

from datetime import datetime
from colorama import Fore, Style

class GestorSistema:
    
    # Metodos
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
                    break
                
                # Validamos que sea un tipo valido
                if typeCar.lower() != 'moto' or typeCar.lower() != 'coche':
                    raise Exception(f"El tipo de vehiculo ingresado ({typeCar.lower()}) no es valido")
                
                # Si llegamos aca, pedimos las cosas comunes como matricula, modelo y marca
                matricula = notAllowEmptyVal(
                    label = "> Ingrese la matricula: "
                )
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
                        label = "> Ingrese el CC de la moto: "
                    )
                    flotaMoto = Moto(matricula, marca, modelo, cc)
                if typeCar.lower() == 'coche':
                    npuertas = notAllowEmptyVal(
                        label = "> Ingrese el numero de puertas del coche: "
                    )
                    flotaCoche = Coche(matricula, marca, modelo, npuertas)
                
                pass
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {e}\n")
        
    def reservar_vehiculo(self) -> None:
        """
        Funcion para reserar vehiculos de la flota
        pidiendo el vehiculo por matricula
        y fecha de la reserva
        return:
            None
        """
        while True:
            try:
                # Pedimos los datos al usuario
                matricula = input("> Ingrese la matricula del vehiculo o vacio si desea cancelar: ").strip()
                dateReserve = ''
                # Validamos si es vacio
                if matricula == '':
                    break
                    
                # Validamos si de verdad existe la matricula antes de pedir la fecha
                
                # Pedimos la fecha de la reserva
                while True:
                    try:
                        fecha_reserva = input("> Ingrese la fecha de reserva (dd/mm/yyyy): ")
                        dateReserve = datetime(fecha_reserva, '%d/%m/%y')
                        break
                    except ValueError:
                        print(f"{Fore.RED}[ERROR]: Fecha de reserva no es valida\n")
                
                # Si llevamos aqui, buscamos la reserva
                print(f"fecha: {dateReserve}, matricula: {matricula}")
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {e}\n")
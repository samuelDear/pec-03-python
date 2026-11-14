class Vehiculo:
    
    # Metodos
    def __init__(self, matricula: str, marca: str, modelo: str):
        self.__matricula = matricula
        self.__marca = marca
        self.__modelo = modelo
        
    @property
    def matricula(self):
        return self.__matricula

    @property
    def marca(self):
        return self.__marca
    
    @property
    def modelo(self):
        return self.__modelo
    
    def __str__(self):
        return f"Matricula: {self.__matricula}, Marca: {self.__marca}, Modelo: {self.__modelo}"
    
class Coche(Vehiculo):
    
    # Metodos
    def __init__(self, matricula: str, marca: str, modelo: str, n_puertas: int):
        super().__init__(matricula, marca, modelo)
        self.__n_puertas = n_puertas
        
    def __str__(self):
        return f"{type(self).__name__} {super().__str__()}, N. Puertas: {self.__n_puertas}"
    
class Moto(Vehiculo):
    
    # Metodos
    def __init__(self, matricula: str, marca: str, modelo: str, cc: int):
        super().__init__(matricula, marca, modelo)
        self.__cc = cc
            
    def __str__(self):
        return f"{type(self).__name__} {super().__str__()}, CC: {self.__cc}"

if __name__ == "__main__":
    # Prueba coche
    coche1 = Coche("9234HDJ", "Honda", "Civic", 5)
    
    print(coche1)
    
    # Prueba Moto
    moto1 = Moto("9234HDJ", "Bera", "BETA 300", 150)
        
    print(moto1)
        
from persona import Persona


def crear_persona():
    dni: str = str(input("Ingrese DNI: "))
    nombres: str = str(input("Ingrese Nombres: "))
    apellidos: str = str(input("Ingrese Apellidos: "))
    direccion: str = str(input("Ingrese Direccion: "))
    telefono: str = str(input("Ingrese Telefono: "))
    noe: Persona = Persona(dni, nombres, apellidos, direccion, telefono)
    print(noe.dni)
   


def main():
    print("Hola mundo")
    crear_persona()


if __name__ == '__main__':
    main()

from persona import Persona
personas: Persona = []


def crear_persona():
    dni: str = str(input("Ingrese DNI: "))
    nombres: str = str(input("Ingrese Nombres: "))
    apellidos: str = str(input("Ingrese Apellidos: "))
    direccion: str = str(input("Ingrese Direccion: "))
    telefono: str = str(input("Ingrese Telefono: "))
    persona: Persona = Persona(dni, nombres, apellidos, direccion, telefono)
    personas.append(persona)


def listar_personas():
    for persona in personas:
        Persona.convertir_a_string(persona)


def buscar_persona():
    dni: str = str(input("Ingrese DNI para buscar: "))
    for persona in personas:
        if persona.dni == dni:
            Persona.convertir_a_string(persona)


def editar_persona():
    dni: str = str(input("Ingrese DNI para Editar: "))
    for persona in personas:
        if persona.dni == dni:
            persona.nombres=str(input("Ingrese un nuevo nombre: "))
def eliminar_persona():
    dni: str = str(input("Ingrese DNI para Eliminar: "))
    for index, persona in enumerate(personas):
        if persona.dni== dni:
            personas.pop(index)

def main():
    continuar: bool = True
    while continuar:
        caso: str = str(
            input("ingrese 1 para crear persona, 2 para listar personas,3 para buscar persona, 4 para editar persona, 5 para eliminar persona, 10 para termimar: "))
        match caso:
            case "1":
                crear_persona()
            case "2":
                listar_personas()
            case "3":
                buscar_persona()
            case "4":
                editar_persona()
            case "5":
                eliminar_persona()
            case "10":
                continuar = False


if __name__ == '__main__':
    main()

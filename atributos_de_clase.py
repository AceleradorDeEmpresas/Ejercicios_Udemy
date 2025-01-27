class Persona: 

    atributo_clase = 0

    # Constructor
    def __init__(self):
        self.atributo_instancia = 0



# Modificar el atributo de instancia
Persona.atributo_clase += 1
print(f"Atributo de clase con nuevo valor: {Persona.atributo_clase}")

# Creamos un objeto 
persona_1 = Persona()
persona_1.atributo_instancia = 40
print(f"Atributo de instancia persona_1: {persona_1.atributo_instancia}")
print(f"Atributo de clase desde persona 1: {persona_1.atributo_clase}")
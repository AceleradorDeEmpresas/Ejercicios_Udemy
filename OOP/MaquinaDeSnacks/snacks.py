from snack import Snack
class Snacks:
    lista_snacks = [
        Snack("Papas", 50),
        Snack("Gansito", 60),
        Snack("Donitas", 70),
        Snack("Doritos", 80),
        Snack("Pizza", 100)
    ]

    def agregar_snack(self, snack):
        Snacks.lista_snacks.append(snack)

    def __str__(self):
        snacks_str = ""
        for snacks in Snacks.lista_snacks:
            snacks_str += "\n" + snacks.__str__()
        return f""" *** Snacks disponibles ***
        {snacks_str}
        """
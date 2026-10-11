class Pokemon:
    total_creados = 0

    def __init__(
        self,
        nombre,
        tipo,
        nivel=1,
        ataque=10,
        defensa=10,
        salud=100
    ):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel
        self.ataque = ataque
        self.defensa = defensa
        self.salud = salud

        Pokemon.total_creados += 1

    def _del_(self):
        print(f"Pokemon {self.nombre} ha sido liberado ✨")

    def entrenar(self, *args):
        # Sobrecarga simulada usando *args
        if len(args) == 0:
            estadisticas = ["ataque"]
        elif len(args) == 1:
            estadisticas = [args[0]]
        else:
            estadisticas = list(args)

        for estadistica in estadisticas:
            if estadistica == "ataque":
                self.ataque += 5
            elif estadistica == "defensa":
                self.defensa += 5
            elif estadistica == "salud":
                self.salud += 10
            else:
                print(f"Estadística no válida: {estadistica}")
                continue

            print(f"{self.nombre} mejoró su {estadistica}.")

        self.nivel += 1

    def mostrar_info(self):
        print("\n--- INFORMACIÓN DEL POKÉMON ---")
        print(f"Nombre: {self.nombre}")
        print(f"Tipo: {self.tipo}")
        print(f"Nivel: {self.nivel}")
        print(f"Ataque: {self.ataque}")
        print(f"Defensa: {self.defensa}")
        print(f"Salud: {self.salud}")

    def atacar(self, objetivo):
        if self.salud <= 0:
            print(f"{self.nombre} no puede atacar.")
            return

        if objetivo.salud <= 0:
            print(f"{objetivo.nombre} ya no puede combatir.")
            return

        danio = max(1, self.ataque - objetivo.defensa)
        objetivo.salud = max(0, objetivo.salud - danio)

        print(
            f"{self.nombre} atacó a {objetivo.nombre} "
            f"e hizo {danio} puntos de daño."
        )
        print(f"Salud restante de {objetivo.nombre}: {objetivo.salud}")

    @classmethod
    def total_pokemons(cls):
        """Muestra cuántos Pokémon se han creado."""
        return cls.total_creados
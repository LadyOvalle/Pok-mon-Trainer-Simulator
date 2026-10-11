from clases.pokemon import Pokemon


def mostrar_pokemons(pokemons):
    if not pokemons:
        print("No hay Pokémon registrados.")
        return

    for indice, pokemon in enumerate(pokemons, start=1):
        print(f"\n{indice}. {pokemon.nombre} ({pokemon.tipo})")
        pokemon.mostrar_info()


def seleccionar_pokemon(pokemons):
    if not pokemons:
        print("Primero debes crear un Pokémon.")
        return None

    mostrar_pokemons(pokemons)

    try:
        numero = int(input("Selecciona el número del Pokémon: "))

        if 1 <= numero <= len(pokemons):
            return pokemons[numero - 1]

        print("Número fuera de rango.")
    except ValueError:
        print("Debes introducir un número válido.")

    return None


def menu():
    pokemons = []

    while True:
        print("\n========== SIMULADOR POKÉMON ==========")
        print("1. Crear Pokémon")
        print("2. Entrenar Pokémon")
        print("3. Ver información de todos")
        print("4. Calcular cuántos Pokémon existen")
        print("5. Liberar un Pokémon")
        print("6. Atacar a otro Pokémon")
        print("7. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            tipo = input("Tipo: ")

            try:
                nivel = int(input("Nivel inicial (1 por defecto): ") or 1)
                ataque = int(input("Ataque (10 por defecto): ") or 10)
                defensa = int(input("Defensa (10 por defecto): ") or 10)
                salud = int(input("Salud (100 por defecto): ") or 100)

                if nivel < 1 or ataque < 0 or defensa < 0 or salud < 0:
                    print("Introduce valores válidos.")
                    continue

                nuevo = Pokemon(
                    nombre, tipo, nivel, ataque, defensa, salud
                )
                pokemons.append(nuevo)
                print(f"{nombre} ha sido creado correctamente.")

            except ValueError:
                print("Debes introducir números enteros en las estadísticas.")

        elif opcion == "2":
            pokemon = seleccionar_pokemon(pokemons)

            if pokemon:
                print("1. Mejorar ataque")
                print("2. Mejorar defensa")
                print("3. Mejorar salud")
                print("4. Mejorar varias estadísticas")

                eleccion = input("Elige el entrenamiento: ")

                if eleccion == "1":
                    pokemon.entrenar("ataque")
                elif eleccion == "2":
                    pokemon.entrenar("defensa")
                elif eleccion == "3":
                    pokemon.entrenar("salud")
                elif eleccion == "4":
                    pokemon.entrenar("ataque", "defensa", "salud")
                else:
                    print("Opción no válida.")

        elif opcion == "3":
            mostrar_pokemons(pokemons)

        elif opcion == "4":
            print(
                "Total de Pokémon creados:",
                Pokemon.total_pokemons()
            )
            print("Pokémon registrados actualmente:", len(pokemons))

        elif opcion == "5":
            pokemon = seleccionar_pokemon(pokemons)

            if pokemon:
                pokemons.remove(pokemon)
                nombre = pokemon.nombre
                del pokemon
                print(f"{nombre} ha sido liberado de la colección.")

        elif opcion == "6":
            print("Selecciona tu Pokémon atacante:")
            atacante = seleccionar_pokemon(pokemons)

            if atacante:
                print("Selecciona el Pokémon objetivo:")
                objetivo = seleccionar_pokemon(pokemons)

                if objetivo:
                    if atacante is objetivo:
                        print("Un Pokémon no puede atacarse a sí mismo.")
                    else:
                        atacante.atacar(objetivo)

        elif opcion == "7":
            print("Gracias por usar el simulador Pokémon.")
            break

        else:
            print("Opción no válida. Intenta nuevamente.")


if __name__ == "__main__":
    menu()
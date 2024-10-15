from file_manager import add_synonym, display_all_synonyms
from raid import raid_0, raid_1

# Nombres de los archivos
concepts_file = "Conceptos.txt"
raida_file = "RAIDa.txt"
raidb_file = "RAIDb.txt"

while True:
    print("\nSimulador RAID")
    print("1. Ingresar un nuevo sinónimo")
    print("2. Mostrar la lista completa")
    print("3. Mostrar RAID 0")
    print("4. Mostrar RAID 1")
    print("5. Salir")

    options = int(input("Ingrese una opcion: "))

    if options == 1:
        add_synonym(concepts_file)

    elif options == 2:
        display_all_synonyms(concepts_file)

    elif options == 3:
        raid_0(concepts_file, raida_file, raidb_file)

    elif options == 4:
        raid_1(concepts_file, raida_file, raidb_file)

    elif options == 5:
        print("Saliendo del programa...")
        break
    else:
        print("Intentelo de nuevo")

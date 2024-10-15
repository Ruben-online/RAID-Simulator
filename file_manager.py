import os


# Agregar un sinónimo
def add_synonym(file):
    word = input("Ingrese el concepto: ").strip()
    synonym = input("Ingrese el sinónimo: ").strip()
    save_synonym(file, word, synonym)
    print(f'Sinónimo {word}:{synonym} agregado correctamente.')


# Lee los sinónimos de un txt
def load_synonyms(file):
    synonyms = []

    if os.path.exists(file):
        with open(file, 'r') as file:
            for line in file:
                word, synonym = line.strip().split(':')
                synonyms.append((word, synonym))

    return synonyms


# Guarda un sinónimo en el archivo
def save_synonym(file, word, synonym):
    with open(file, 'a') as f:
        f.write(f'{word}:{synonym}\n')


# Print de todos los sinónimos
def display_all_synonyms(file):
    synonyms = load_synonyms(file)
    if synonyms:
        print("\nLista completa de sinónimos:")
        for word, synonym in synonyms:
            print(f'{word} : {synonym}')
    else:
        print("No hay sinónimos registrados.")

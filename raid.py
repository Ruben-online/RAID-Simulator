from file_manager import load_synonyms


# Método para RAID 0 (Divide el contenido en dos archivos)
def raid_0(total_file, raid_a_file, raid_b_file):
    synonyms = load_synonyms(total_file)
    if synonyms:
        with open(raid_a_file, 'w') as raid_a, open(raid_b_file, 'w') as raid_b:
            for i, (word, synonym) in enumerate(synonyms):
                if i % 2 == 0:
                    raid_a.write(f'{word}:{synonym}\n')
                else:
                    raid_b.write(f'{word}:{synonym}\n')
        print("Datos distribuidos en RAID 0 entre 'raid_a.txt' y 'raid_b.txt'.")
    else:
        print("No hay sinónimos para distribuir.")


# Método para RAID 1 (Duplica el contenido en los dos archivos
def raid_1(total_file, raid_a_file, raid_b_file):
    synonyms = load_synonyms(total_file)
    if synonyms:
        with open(raid_a_file, 'w') as raid_a, open(raid_b_file, 'w') as raid_b:
            for word, synonym in synonyms:
                raid_a.write(f'{word}:{synonym}\n')
                raid_b.write(f'{word}:{synonym}\n')
        print("Datos copiados en RAID 1 en 'raid_a.txt' y 'raid_b.txt'.")
    else:
        print("No hay sinónimos para copiar.")

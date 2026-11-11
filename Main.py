def bwt(s: str) -> tuple[str, int]:
    rotations = [s[i:] + s[:i] for i in range(len(s))]

    rotations.sort()

    bwt_str = "".join(row[-1] for row in rotations)

    original_index = rotations.index(s)

    return bwt_str, original_index


stringa = input("Inserisci una stringa: ") + "$"
risultato, indice = bwt(stringa)

print(f"Stringa originale: {stringa}")
print(f"Risultato BWT:     {risultato}")
print(f"Indice riga:       {indice}")

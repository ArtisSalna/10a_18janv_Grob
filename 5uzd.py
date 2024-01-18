try:
    lietotaja_vards = input("Ievadiet savu vārdu: ")
    faila_nosaukums = "5uzd.txt"
    with open(faila_nosaukums, 'w') as fails:
        fails.write(lietotaja_vards)

    print(f"Vārds '{lietotaja_vards}' veiksmīgi ierakstīts failā '{faila_nosaukums}'.")

except FileNotFoundError:
    print(f"Kļūda: Fails '{faila_nosaukums}' netika atrasts.")
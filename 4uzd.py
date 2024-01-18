try:
    faila_nosaukums = input("Ievadiet faila nosaukumu: ")
    faila_paplaisinajums = input("Ievadiet faila paplašinājumu (formāts): ")

    pilns_faila_nosaukums = f"{faila_nosaukums}.{faila_paplaisinajums}"

    with open(pilns_faila_nosaukums, 'r') as fails:
        faila_saturu = fails.read()

    print(f"Faila '{pilns_faila_nosaukums}' saturs:\n{faila_saturu}")

except FileNotFoundError:
    print(f"Kļūda: Fails '{pilns_faila_nosaukums}' netika atrasts.")
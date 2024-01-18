import json

def galvena_funkcija():
    try:
        with open("1uzd.json", "r", encoding="utf-8") as ff:
            data=json.load(ff)
            print(data)
            
    except FileNotFoundError:
        print("datne nav atrasta")
    except json.JSONDecodeError:
        print("datnei nav JSON formāts!")


if __name__=="__main__":
    galvena_funkcija()
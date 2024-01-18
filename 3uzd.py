def aka(fails):
    try:
        with open(fails, 'r', encoding='utf-8') as gg:
            rinda = gg.readlines()
        if len(rinda) >=3:
            print("Trešā rinda:", rinda[2].strip())
        else:
            print("Failā nav pietiekami daudz rindu.")
    
    except FileNotFoundError:
        print(f"faila '{fails}'nav atrasts. ")
    
    aka('3uzd.txt')
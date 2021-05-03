import json

chemin = r"D:\FORMATION_Language_DEV\PYTHON_3\fichier.json"

with open(chemin, "r", encoding='utf-8') as f:
    #Pour écrire ---------------------------
    #json.dump(list(range(10)), f, indent=4)
    #---------------------------------------
    ma_liste = json.load(f)
    print(ma_liste)

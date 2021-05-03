class Voiture:
    voiture_crees = 0

    def __init__(self, marque):
        Voiture.voiture_crees += 1
        self.marque = marque


voiture_01 = Voiture('yolo')
voiture_02 = Voiture("toto")

print(voiture_01.marque)
print(voiture_02.marque)

print(Voiture.voiture_crees)

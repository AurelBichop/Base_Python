class Voiture:
    essence = 100

    def afficher_reservoir(self):
        print(f"la voiture contient {self.essence}L d'essence")

    def faire_le_plein(self):
        self.essence = 100

    def roule(self, km):
        conso = (km * 5)/100
        self.essence -= conso

        if(self.essence < 10 and self.essence > 0):
            print('Attention bientôt plus de carburant !!!')
        if(self.essence > 0):
            print(f"Il reste {self.essence} d'essence dans le reservoir")
        else:
            print("Plus d'essence merci de faire le plein")

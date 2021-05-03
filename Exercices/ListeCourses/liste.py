choix_user = 0
liste_course = []

while choix_user is not 5:
    print('''
    Choisisser Une Action :

    1] Ajouter un élément à la liste de courses

    2] Retirer un élément de la liste de courses

    3] Afficher les éléments de la liste de courses

    4] Vider la liste de courses

    5] Quitter le programme
    ===================================================='''
          )

    choix_user = input('Votre choix :')

    if choix_user.isdigit():
        choix_user = int(choix_user)

        if choix_user == 1:
            name_element = input("Nom de l'element :")
            liste_course.append(name_element)
        elif choix_user == 2:
            name_element = input("Nom de l'element :")
            if name_element in liste_course:
                liste_course.remove(name_element)
            else:
                print("L'element n'existe pas")
        elif choix_user == 3:
            if liste_course:
                resultat = "\n".join(liste_course)
                print(resultat)
            else:
                print("La liste est vide")
        elif choix_user == 4:
            liste_course.clear()
            print("La liste a été vidé")

    else:
        print("Merci de renseigner un entier")

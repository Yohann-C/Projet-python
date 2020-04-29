## -*- Encoding: UTF-8 -*-  

class Menu():
     def AfficherMenu(self) :
         print(" Logiciel de critique de film \n\n")
         print(" 1- Créer une fiche \n")
         print(" 2- Supprimer une fiche \n")
         print(" 3- Modifier une fiche \n")
         print(" 4- Afficher une fiche\n")
         print(" 5- Afficher toutes les fiches \n")
         print(" 6- Afficher toutes les fiches triées par note \n")


class Message():
    def AfficherMessage(self,arg) :
        print(arg)
    def AfficherMessageReponse(self,arg) :
         temp=input(arg)
         return temp


Menu().AfficherMenu()

NomDuFilm = Message().AfficherMessageReponse("Quelle est le nom du film : ")
print(f'le nom est {NomDuFilm}')

#BITE BITE BITE BITE

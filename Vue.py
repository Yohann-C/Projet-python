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
         
class Fiche():
     def CreerFiche(self) :
         listeInfoFilm = []
         listeInfoFilm.append(Message().AfficherMessageReponse("Quel est le nom du film : "))
         listeInfoFilm.append(Message().AfficherMessageReponse("Quelle est la catégorie du film : "))
         listeInfoFilm.append(Message().AfficherMessageReponse("Quelle est la date de parution du film : "))
         listeInfoFilm.append(Message().AfficherMessageReponse("Qui est le réalisateur : "))
         for x in range (3) :
             listeInfoFilm.append(Message().AfficherMessageReponse("Qui sont les acteurs-ices principaux (3 max) "))
         listeInfoFilm.append(Message().AfficherMessageReponse("Quelle note donnez vous au film (/5) : "))
         listeInfoFilm.append(Message().AfficherMessageReponse("Commentaires : "))
         return listeInfoFilm


class Message():
     def AfficherMessage(self,arg) :
         print(arg)
     def AfficherMessageReponse(self,arg) :
         temp=input(arg)
         return temp


Menu().AfficherMenu()
print(Fiche().CreerFiche())

#BITE BITE BITE BITE

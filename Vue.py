## -*- Encoding: UTF-8 -*-  
from Ajouter import LireBD



class Menu():
    def AfficherMenu(self) :
        print(" Logiciel de critique de film \n\n")
        print(" 1- Créer une fiche \n")
        print(" 2- Supprimer une fiche \n")
        print(" 3- Modifier une fiche \n")
        print(" 4- Afficher une fiche\n")
        print(" 5- Afficher toutes les fiches \n")
        print(" 6- Afficher toutes les fiches triées par note \n")
        
        reponse = Message().AfficherMessageReponse("Que voulez vous faire : ")
        if reponse == '1':
            Fiche().CreerFiche()
        if reponse == '2':
            Fiche().SupprimerFiche()
        if reponse == '3':
            Fiche().ModifierFiche()
        if reponse == '4':
           Fiche().AfficherUneFiche()
        if reponse == '5':
           Fiche().AfficherLesFiches()
        if reponse == '6':
           Fiche().AfficherLesFichesTrie()         

         
         
class Fiche():
    def CreerFiche(self) :
        listeInfoFilm = []
        listeInfoFilm.append(Message().AfficherMessageReponse("Quel est le nom du film : "))

        listeInfoFilm.append(Message().AfficherMessageReponse("Quelle est la catégorie du film : "))

        listeInfoFilm.append(Message().AfficherMessageReponse("Quelle est la date de parution du film : "))

        listeInfoFilm.append(Message().AfficherMessageReponse("Qui est le réalisateur : "))
        for x in range (3) :
            listeInfoFilm.append(Message().AfficherMessageReponse("Qui sont les acteurs-ices principaux (3 max) "))

        note = int(Message().AfficherMessageReponse("Quelle note donnez vous au film (/5) : "))
        while note > 5:
            note = int(Message().AfficherMessageReponse("Quelle note donnez vous au film (/5) : "))
            if note <= 5:
                break
         #TODO: caper la note a 5

        listeInfoFilm.append(Message().AfficherMessageReponse("Commentaires : "))
        return listeInfoFilm
    def SupprimerFiche(self) :
        #TODO: ajouter liste des fiches AfficherLesFiches()
        Reponse = Message().AfficherMessageReponse("Quelle fiche voulez vous supprimer : ")
        return Reponse
    def ModifierFiche(self) :
        #TODO: ajouter liste des fiches AfficherLesFiches()
        Reponse = Message().AfficherMessageReponse("Quelle fiche voulez vous modifier : ")
        return Reponse
    def AfficherUneFiche(self):
        #TODO: ajouter liste des fiches AfficherLesFiches()
        Reponse = Message().AfficherMessageReponse("Quelle fiche voulez vous afficher : ")
        return Reponse
        #TODO: récupérer la fiche à la position réponse et l'afficher
    def AfficherLesFiches(self):
        print('Liste des fiches :')
        contenu = []
        for x in range (LireBD().nombreFiche()):
            contenu.append(LireBD().lireFiche(x))
            print(x+1,"- ",contenu[x][0]," - ", contenu[x][5], "/5")
        #TODO: récupérer tt les rapports et les afficher ligne par ligne
    def AfficherLesFichesTrie(self):
        print('Liste des fiches par note:')
        #TODO: récupérer tt les rapports et les afficher ligne par ligne en fonction de la note



class Message():
    def AfficherMessage(self,arg) :
        print(arg)
    def AfficherMessageReponse(self,arg) :
        temp=input(arg)
        return temp


Menu().AfficherMenu()

#BITE BITE BITE BITE

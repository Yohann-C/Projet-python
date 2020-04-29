## -*- Encoding: UTF-8 -*-  
from Ajouter import LireBD
from Ajouter import Ajouter

contenu = []
for x in range (LireBD().nombreFiche()):
    contenu.append(LireBD().lireFiche(x))

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
        listeInfoFilm.append(note)
        listeInfoFilm.append(Message().AfficherMessageReponse("Commentaires : "))
        return listeInfoFilm

    def SupprimerFiche(self) :
        #TODO: ajouter liste des fiches AfficherLesFiches()
        Reponse = Message().AfficherMessageReponse("Quelle fiche voulez vous supprimer : ")
        return Reponse

    def ModifierFiche(self) :
        #TODO: ajouter liste des fiches AfficherLesFiches()
        Fiche().AfficherLesFiches()
        noFiche = int(Message().AfficherMessageReponse("Quelle fiche voulez vous modifier : "))-1
        i = 0
        print(f"\nNom du film : {(contenu[noFiche][0])} \n")
        reponse = Message().AfficherMessageReponse("voulez vous modifier cette donnée ? (O/N) : ")
        if reponse == 'O':
            reponse = ''
            contenu[noFiche][i] = Message().AfficherMessageReponse("Quelle est la nouvelle donnée ? : ")
        i+=1
        print(f"\nCategorie du film : {(contenu[noFiche][1])} \n")
        reponse = Message().AfficherMessageReponse("voulez vous modifier cette donnée ? (O/N) : ")
        if reponse == 'O':
            reponse = ''
            contenu[noFiche][i] = Message().AfficherMessageReponse("Quelle est la nouvelle donnée ? : ")
        i+=1
        print(f"\ndate du film : {(contenu[noFiche][2])} \n")
        reponse = Message().AfficherMessageReponse("voulez vous modifier cette donnée ? (O/N) : ")
        if reponse == 'O':
            reponse = ''
            contenu[noFiche][i] = Message().AfficherMessageReponse("Quelle est la nouvelle donnée ? : ")
        i+=1
        print(f"\nRealisateur du film : {(contenu[noFiche][3])} \n")
        reponse = Message().AfficherMessageReponse("voulez vous modifier cette donnée ? (O/N) : ")
        if reponse == 'O':
            reponse = ''
            contenu[noFiche][i] = Message().AfficherMessageReponse("Quelle est la nouvelle donnée ? : ")
        i+=1
        for x in range (3):
            i+=1
            print(f"\nActeur principaux du film : {(contenu[noFiche][4+x])} \n")
            reponse = Message().AfficherMessageReponse("voulez vous modifier cette donnée ? (O/N) : ")
            if reponse == 'O':
                reponse = ''
                contenu[noFiche][i] = Message().AfficherMessageReponse("Quelle est la nouvelle donnée ? : ")
                break
        print(f"\nNote : {(contenu[noFiche][7])} \n")
        reponse = Message().AfficherMessageReponse("voulez vous modifier cette donnée ? (O/N) : ")
        if reponse == 'O':
            reponse = ''
            contenu[noFiche][i] = Message().AfficherMessageReponse("Quelle est la nouvelle donnée ? : ")
        
        i+=1
        print(f"\nCategorie du film : {(contenu[noFiche][8])} \n")
        reponse = Message().AfficherMessageReponse("voulez vous modifier cette donnée ? (O/N) : ")
        if reponse == 'O':
            reponse = ''
            contenu[noFiche][i] = Message().AfficherMessageReponse("Quelle est la nouvelle donnée ? : ")


        print(contenu[noFiche])


    def AfficherUneFiche(self):
        
        Reponse = int(Message().AfficherMessageReponse("Quelle fiche voulez vous afficher : "))
        print(f"\nNom du film : {(contenu[Reponse][0])} \n")
        print(f"Catégorie: {(contenu[Reponse][1])} \n")
        print(f"date de sortie : {(contenu[Reponse][2])} \n")
        print(f"réalisateur : {(contenu[Reponse][3])} \n")
        print(f"Acteurs principaux : {(contenu[Reponse][4])} \n")
        print(f"Note : {(contenu[Reponse][7])} \n")
        print(f"Commentaire : {(contenu[Reponse][6])} \n")

    def AfficherLesFiches(self):
        print('Liste des fiches :')

        for x in range (LireBD().nombreFiche()):

            print(x+1,"- ",contenu[x][0]," - ", contenu[x][7], "/5")

    def AfficherLesFichesTrie(self):

    

        def returnNote(contenu):
            return contenu[x][5]

        print('Liste des fiches par note:')
        
        sorted(contenu, key=returnNote)
        print(contenu)
        #TODO: récupérer tt les rapports et les afficher ligne par ligne en fonction de la note



class Message():
    def AfficherMessage(self,arg) :
        print(arg)
    def AfficherMessageReponse(self,arg) :
        temp=input(arg)
        return temp


Menu().AfficherMenu()

#BITE BITE BITE BITE

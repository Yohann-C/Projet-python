## -*- Encoding: UTF-8 -*-  
from GestionBD import LireBD
from GestionBD import Ajouter
from GestionBD import CategorieBD

contenu = []
for x in range (LireBD().nombreFiche()):
    contenu.append(LireBD().lireFiche(x))

#yohann
class Menu():
    
    def AfficherMenu(self) :
        print(" Logiciel de critique de film \n\n")
        print(" 1- Créer une fiche \n")
        print(" 2- Supprimer une fiche \n")
        print(" 3- Modifier une fiche \n")
        print(" 4- Afficher une fiche\n")
        print(" 5- Afficher toutes les fiches \n")
        print(" 6- Afficher toutes les fiches triées par note \n")
        print(" 7- Ajouter / supprimer categorie \n")
        print(" 8- Quitter \n")
        
        reponse = Message().AfficherMessageReponse("Que voulez vous faire : ")
        return reponse  

#yohann
class CatégorieAffichage():
    def MenuCategorie(self):
        print("\n Voulez vous : \n")
        print(" 1- Ajouter une categorie à la liste \n")
        print(" 2- Supprimer une categorie de la liste \n")
        reponse = Message().AfficherMessageReponse("Que voulez vous faire : ")
        return reponse

    def AfficherListeCategorie(self):
        print('Liste des categories :')
        liste = []
        for x in range (CategorieBD().nombreCategorie()):
            liste.append(CategorieBD().LireBDCat(x))
            print(x+1,"- ",liste[x][0])
    
    def SupprimerCategorie(self):
        CatégorieAffichage().AfficherListeCategorie()
        rep = Message().AfficherMessageReponse("quelle catégorie voulez vous supprimer: ")
        return rep

#yohann   
class Fiche():
    def getIndex(self):
        return indexAModifier

    def CreerFiche(self) :
        listeInfoFilm = []

        nom = "" 
        while nom == "":
            nom = ""
            nom = Message().AfficherMessageReponse("Quel est le nom du film : ")
            if nom != "":
                break

        listeInfoFilm.append(nom)

        #Choix de la catégorie parmis les disponibles
        CatégorieAffichage().AfficherListeCategorie()
        index = int(Message().AfficherMessageReponse("Quelle est la catégorie du film : "))
        while index > CategorieBD().nombreCategorie():
            Message().AfficherMessage("Voici les catégories disponibles : \n")
            CatégorieAffichage().AfficherListeCategorie()
            index = int(Message().AfficherMessageReponse("Quelle est la catégorie du film : "))
            if index < CategorieBD().nombreCategorie():
                break 
        
        #recupération de la catégorie sous forme de string
        catTemp = str(CategorieBD().LireBDCat(index-1))
        cat = ""
        for x in range (len(catTemp)-4):
                cat += catTemp[x+2]
        listeInfoFilm.append(str(cat))

        listeInfoFilm.append(Message().AfficherMessageReponse("Quelle est la date de parution du film : "))
        listeInfoFilm.append(Message().AfficherMessageReponse("Qui est le réalisateur : "))

        #boucle pour demander les 3 acteurs principaux
        for x in range (3) :
            listeInfoFilm.append(Message().AfficherMessageReponse("Qui sont les acteurs-ices principaux (3 max) "))
        note = int(Message().AfficherMessageReponse("Quelle note donnez vous au film (/10) : "))

        #boucle pour avoir une note forcement inferieur à 10
        while note > 10:
            note = int(Message().AfficherMessageReponse("Quelle note donnez vous au film (/10) : "))
            if note <= 10:
                break

        listeInfoFilm.append(note)
        listeInfoFilm.append(Message().AfficherMessageReponse("Commentaires : "))
        return listeInfoFilm

    #yohann
    def SupprimerFiche(self) :
        Fiche().AfficherLesFiches()
        Reponse = int(Message().AfficherMessageReponse("Quelle fiche voulez vous supprimer : "))
        return Reponse

    #yohann
    #fonction pour valider la validation lors de modification de fiche
    def MessageVerification(self,*arg):
        reponse = Message().AfficherMessageReponse("voulez vous modifier cette donnée ? (O/N) : ")
        if reponse == 'O':
            reponse = ''
            contenu[arg[0]][arg[1]] = Message().AfficherMessageReponse("Quelle est la nouvelle donnée ? : ")

    #yohann
    #incrementation du I pour savoir sa position dans la BD
    def ModifierFiche(self) :
            Fiche().AfficherLesFiches()
            noFiche = int(Message().AfficherMessageReponse("Quelle fiche voulez vous modifier : ")) -1
            i = 0
            print(f"\nNom du film : {(contenu[noFiche][0])} \n")
            Fiche().MessageVerification(i,noFiche)
            i+=1
            print(f"\nCategorie du film : {(contenu[noFiche][1])} \n")
            Fiche().MessageVerification(i,noFiche)
            i+=1
            print(f"\ndate du film : {(contenu[noFiche][2])} \n")
            Fiche().MessageVerification(i,noFiche)
            i+=1
            print(f"\nRealisateur du film : {(contenu[noFiche][3])} \n")
            Fiche().MessageVerification(i,noFiche)
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
            Fiche().MessageVerification(i,noFiche)
            i+=1
            print(f"\nCommentaire : {(contenu[noFiche][8])} \n")
            Fiche().MessageVerification(i,noFiche)
            global indexAModifier
            indexAModifier = noFiche+1
            return contenu[noFiche]

    #yohann
    def AfficherUneFiche(self):
        
        Reponse = int(Message().AfficherMessageReponse("Quelle fiche voulez vous afficher : "))-1
        print(f"\nNom du film : {(contenu[Reponse][0])} \n")
        print(f"Catégorie: {(contenu[Reponse][1])} \n") 
        print(f"date de sortie : {(contenu[Reponse][2])} \n")
        print(f"réalisateur : {(contenu[Reponse][3])} \n")
        for x in range(3):
            print(f"Acteurs principaux : {(contenu[Reponse][4+x])} \n")
        print(f"Note : {(contenu[Reponse][7])} \n")
        print(f"Commentaire : {(contenu[Reponse][8])} \n")

    #yohann
    def AfficherLesFiches(self):
        print('Liste des fiches :')

        for x in range (LireBD().nombreFiche()):

            print(x+1,"- ",contenu[x][0]," - ", contenu[x][7], "/10")

    #yohann
    def AfficherLesFichesTrie(self,arg):

        for x in range (0,int(len(arg)),2):
            print(x+1,"- ",arg[x]," - ", arg[x+1], "/10")
            
#yohann
class Message():
    def AfficherMessage(self,arg) :
        print(arg)
    def AfficherMessageReponse(self,arg) :
        temp=input(arg)
        return temp


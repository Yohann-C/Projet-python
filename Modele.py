import Vue
import GestionBD

class Modele():
    def LancerProgramme(self):
        #while True:
            reponse = Vue.Menu().AfficherMenu()
            if reponse == '1':
                liste = []
                liste.append(Vue.Fiche().CreerFiche())
                GestionBD.Ajouter().ajouterFiche(liste[0][0],liste[0][1],liste[0][2],liste[0][3],liste[0][4],liste[0][5],liste[0][6],liste[0][7],liste[0][8])
            if reponse == '2':
                rep = int(Vue.Fiche().SupprimerFiche())
                GestionBD.Supprimer().suprrimerFiche(rep)
            if reponse == '3':
                try:
                    liste = []
                    liste.append(Vue.Fiche().ModifierFiche())
                    GestionBD.Ajouter().ajouterFiche(liste[0][0],liste[0][1],liste[0][2],liste[0][3],liste[0][4],liste[0][5],liste[0][6],liste[0][7],liste[0][8])
                    GestionBD.Supprimer().suprrimerFiche(Vue.Fiche().getIndex())   
                except IndexError:
                    print("le film n'existe pas")
            if reponse == '4':
                Vue.Fiche().AfficherLesFiches()
                Vue.Fiche().AfficherUneFiche()
            if reponse == '5':
                Vue.Fiche().AfficherLesFiches()
            if reponse == '6':
                Vue.Fiche().AfficherLesFichesTrie()
            if reponse == '7':
                Modele().ModifierCategorie()  
            if reponse == '8':
                quit 

    def ModifierCategorie(self):
       rep= Vue.CatégorieAffichage().MenuCategorie()
       if rep == '1' :
        GestionBD.CategorieBD().AjouterCategorie()
       if rep == '2' :
        rep = Vue.CatégorieAffichage().SupprimerCategorie()
        GestionBD.CategorieBD().SupprimerCategorie(rep)

        
        








if __name__ == '__main__':

    Modele().LancerProgramme()
import csv
import Vue
from csv import reader

 
class Ajouter(): 
    
    def ajouterFiche(self,nom,categorie,dateDeParution,realisateur,acteurUn,acteurDeux,acteurTrois,note,commentaire):
        with open('CritiqueFilmBD.csv', 'a') as file:
            writer = csv.writer(file, delimiter = ',')
            writer.writerow([nom,categorie,dateDeParution,realisateur,acteurUn,acteurDeux,acteurTrois,note,commentaire])

class CategorieBD():

    def AjouterCategorie(self):
        categorieListe = Vue.Message().AfficherMessageReponse("Quelle est la categorie : ")
        with open('CategorieBD.csv', 'a') as file:
            writer = csv.writer(file, delimiter = ',')
            writer.writerow([categorieListe])

    def SupprimerCategorie(self,index):
        lines = list()
        with open('CategorieBD.csv', 'r', encoding='utf-8') as f:
            csv_reader = reader(f)
            x=1
            for line in csv_reader:
                if not line:
                    continue 
                if x != int(index):
                    lines.append(line)
                x+=1
        with open('CategorieBD.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)

    def LireBDCat(self,index):
        with open('CategorieBD.csv', 'rt', encoding='utf-8') as f:
            csv_reader = reader(f)
            x=0
            for line in csv_reader:
                if not line:
                    continue 
                if x == index:
                    return line
                x+=1

    def nombreCategorie(self):
        with open('CategorieBD.csv', 'rt', encoding='utf-8') as f:
            csv_reader = reader(f)
            x=0
            for line in csv_reader:
                if not line:
                    continue 
                x+=1
            return x

class LireBD():
    def lireFiche(self,numFiche):
        with open('CritiqueFilmBD.csv', 'rt', encoding='utf-8') as f:
            csv_reader = reader(f)
            x=0
            for line in csv_reader:
                if not line:
                    continue 
                if x == numFiche:
                    return line
                x+=1
                      
    def nombreFiche(self):
        
        with open('CritiqueFilmBD.csv', 'rt', encoding='utf-8') as f:
            csv_reader = reader(f)
            x=0
            for line in csv_reader:
                if not line:
                    continue 
                x+=1
            return x

class Supprimer():

    def suprrimerFiche(self,indexLigne):
        
        lines = list()
        with open('CritiqueFilmBD.csv', 'r', encoding='utf-8') as f:
            csv_reader = reader(f)
            x=1
            for line in csv_reader:
                if not line:
                    continue 
                if x != int(indexLigne):
                    lines.append(line)
                x+=1
        with open('CritiqueFilmBD.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
        
import csv

 
class Ajouter(): 
    
    def ajouterFiche(self,nom,categorie,dateDeParution,realisateur,acteur,note,commentaire):
        with open('CritiqueFilmBD.csv', 'a') as file:
            writer = csv.writer(file, delimiter = ',')
            writer.writerow([nom,categorie,dateDeParution,realisateur,acteur,note,commentaire])
    
 
class LireBD():
    
    def getFiche(self,numFiche):
        
         with open('CritiqueFilmBD.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            x=0
            for row in readCSV:
                if x == numFiche:
                    print(row)
                x+=1
                
    
  
    
Ajouter().ajouterFiche("Sous le sunlight","rigolo",2000,"Gilber Montagne","blibu et bli et blou",5,"GENIAL LE FILM")

LireBD().getFiche(0)